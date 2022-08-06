from flask import Flask, json, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.wrappers import response
from wallet import Wallet
from blockchain import Blockchain
app = Flask(__name__)
# wallet = Wallet()
# blockchain = Blockchain(wallet.public_key)
CORS(app)  # opening apps to other clients as well

# registering an endpoint in flask so it can give a response


@app.route('/', methods=['GET'])
def get_node_ui():
    return send_from_directory('ui', 'node.html')


@app.route('/network', methods=['GET'])
def get_network_ui():
    return send_from_directory('ui', 'network.html')


@app.route('/wallet', methods=['POST'])
def create_keys():
    wallet.create_keys()
    if wallet.save_keys():

        global blockchain
        blockchain = Blockchain(wallet.public_key, port)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Saving the keys failed'}
        return jsonify(response), 500


@app.route('/wallet', methods=['GET'])
def load_keys():
    if wallet.load_keys():

        global blockchain
        blockchain = Blockchain(wallet.public_key, port)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()}
        return jsonify(response), 201
    else:
        response = {
            'message': 'Loading the keys failed'}
        return jsonify(response), 500

    # whenever a request reaches '/' we accept only get req and return the body


@app.route('/balance', methods=['GET'])
def get_balance():
    balance = blockchain.get_balance()
    if balance != None:
        response = {
            'message': 'fetching balance successful',
            'funds': balance
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Loading balance failed',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/broadcast-transaction', methods=['POST'])
def broadcast_transaction():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found'}
        return jsonify(response), 400
    required = ['sender', 'receiver', 'amount', 'signature']
    if not all(key in values for key in required):
        response = {'message': 'Some data is missing'}
        return jsonify(response), 400
    success = blockchain.new_transaction(
        values['receiver'], values['sender'], values['signature'], values['amount'], is_receiving=True)
    if success:
        response = {
            'message': 'Successfully added Transaction',
            'transaction': {
                'sender': values['sender'],
                'receiver': values['receiver'],
                'amount': values['amount'],
                'signature': values['signature']},

        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed'
        }
        return jsonify(response), 500


@app.route('/broadcast-block', methods=['POST'])
def broadcast_block():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found'}
        return jsonify(response), 400
    if 'block' not in values:
        response = {'message': 'Some data is missing'}
        return jsonify(response), 400
    block = values['block']
    if block['index'] == blockchain.chain[-1].index+1:
        if blockchain.add_block(block):
            response = {'message': 'Block Added'}
            return jsonify(response), 201
        else:
            response = {'message': 'Block seems invalid'}
            return jsonify(response), 409
            # if index of incoming block on our blockchain is greater than that of exisiting block then execute the code the vice versa means some error is there
  # blockchain.chain is our blockchain(peer node) block is the incoming one
    elif block['index'] > blockchain.chain[-1].index:
        response = {
            'message': 'Blockchain seems to differ from local blockchain'}
        blockchain.resolve_conflicts = True
        return jsonify(response), 200
    else:  # the blockchain of incoming node is shorter so theres a problem
        response = {'message': 'Blockchain seems to be shorter,block not added'}
        return jsonify(response), 409


@app.route('/transaction', methods=['POST'])
def add_transaction():
    if wallet.public_key == None:
        response = {
            'message': 'No Wallet set up'
        }
        return jsonify(response), 400
    values = request.get_json()
    if not values:
        response = {'message': 'No Data Found'}
        return jsonify(response), 400
    required_fields = ['receiver', 'amount']
    if not all(field in values for field in required_fields):
        response = {'message': 'Required Data is missing'}
        return jsonify(response), 400
    receiver = values['receiver']
    amount = values['amount']
    signature = wallet.sign_transaction(wallet.public_key, receiver, amount)

    success = blockchain.new_transaction(
        receiver, wallet.public_key, signature, amount)
    print(success)
    if success:
        response = {
            'message': 'Added transaction successfully',
            'transaction': {
                'sender': wallet.public_key,
                'receiver': receiver,
                'amount': amount,
                'signature': signature},
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed'
        }
        return jsonify(response), 500


@app.route('/mine', methods=['POST'])
def mine():
    if blockchain.resolve_conflicts:
        response = {'message': 'Resolve conflicts first, block not added'}
        return jsonify(response), 409
    block = blockchain.mining()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transaction'] = [
            tx.__dict__ for tx in dict_block['transaction']]
        response = {
            'message': 'Block added successfully',
            'block': dict_block,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/resolve-conflicts', methods=['POST'])
def resolve_conflicts():
    replaced = blockchain.resolve()
    if replaced:
        response = {'message': 'Chain was replaced'}
    else:
        response = {'message': 'Local chain kept'}
    return jsonify(response), 200


@app.route('/transactions', methods=['GET'])
def get_open_transaction():
    transactions = blockchain.get_open_transactions()
    dict_transactions = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transactions), 200


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['transaction'] = [
            tx.__dict__ for tx in dict_block['transaction']]
    return jsonify(dict_chain), 200


@app.route('/node', methods=['POST'])
def add_node():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data attached'
        }
        return jsonify(response), 400
    if 'node' not in values:
        response = {
            'message': 'No Data Found'
        }
        return jsonify(response), 400
    node = values['node']
    blockchain.add_peer_node(node)
    response = {
        'message': 'Node added successfully',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 201


@app.route('/node/<node_url>', methods=['DELETE'])
def remove_node(node_url):
    # node url contains the node to be deleted eg localhost:5000
    if node_url == '' or node_url == None:
        response = {
            'message': 'No node found'
        }
        return jsonify(response), 400
    blockchain.remove_peer_node(node_url)
    response = {
        'message': 'Node removed',
        'all_nodes': blockchain.get_peer_nodes()
    }
    return jsonify(response), 200


@app.route('/nodes', methods=['GET'])
def get_nodes():
    nodes = blockchain.get_peer_nodes()
    response = {
        'all_nodes': nodes}
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    # while running node we can specify the port no eg: as python node.py -p 5001
    parser.add_argument('-p', '--port', type=int, default=5000)
    # gives us a list of parsed in arguments
    args = parser.parse_args()
    # extracting port from parsed arguments
    port = args.port
    wallet = Wallet(port)
    blockchain = Blockchain(wallet.public_key, port)
    app.run(host='0.0.0.0', port=port)
