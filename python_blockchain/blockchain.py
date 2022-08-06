import functools

import json
import requests
from collections import OrderedDict

from werkzeug.wrappers import response
from utility import hash_util
from utility.hash_util import hash_block
from utility.verification import Verification
from block import Block
from transaction import Transaction
from wallet import Wallet

MINING_AMOUNT = 10  # reward for miners who create a new block


class Blockchain:
    def __init__(self, hosting_node_id, node_id):
        genesis_block = Block(0, '', [], 100, 0)
        self.chain = [genesis_block]
        self.__open_transactions = []
        self.hosting_node = hosting_node_id
        self.__peer_nodes = set()  # to make sure that every node is only added once
        self.node_id = node_id
        self.resolve_conflicts = False
        self.load_data()

    @property
    def chain(self):
        return self.__chain[:]  # creating copy of the blockchain

    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_open_transactions(self):
        return self.__open_transactions[:]
# blockchain = []
# open_transactions = []
    # owner = 'Sharat'
# using a set to ensure unique participants
# Beginning this is a test
# saving data of transactions to make it persistent

    def load_data(self):
        # global blockchain
        # global open_transactions
        try:
            # loading data as required
            with open('blockchain-{}.txt'.format(self.node_id), mode='r') as f:
                file_content = f.readlines()

                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(
                        tx['sender'], tx['receiver'], tx['signature'], tx['amount']) for tx in block['transaction']]
                    # converted_tx = [OrderedDict(
                    #     [('sender', tx['sender']), ('receiver', tx['receiver']), ('amount', tx['amount'])])for tx in block['transaction']]
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)

                self.chain = updated_blockchain

                # blockchain = [{
                #     'previous_hash': block['previous_hash'],
                #     'index': block['index'],  # will increase in every addition
                #     'transaction': [OrderedDict(
                #         [('sender', tx['sender']), ('receiver', tx['receiver']), ('amount', tx['amount'])]) for tx in block['transaction']],
                #     'proof': block['proof']
                # } for block in blockchain]
                # to remove the new line character
                open_transactions = json.loads(file_content[1][:-1])
                updated_open_transaction = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['sender'], tx['receiver'], tx['signature'], tx['amount'])
                    # updated_transaction = OrderedDict([
                    #     ('sender', tx['sender']),
                    #     ('receiver', tx['receiver']),
                    #     ('amount', tx['amount'])])
                    updated_open_transaction.append(updated_transaction)
                self.__open_transactions = updated_open_transaction
                peer_nodes = json.loads(file_content[2])
                self.__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            print('Exception handled')
            # hard coding the first block
            # genesis_block = Block(0, '', [], 100, 0)
            # genesis_block = {
            #     'previous_hash': '',
            #     'index': 0,
            #     'transaction': [],
            #     'proof': 100}
           # blockchain.append(genesis_block)
           # open_transactions = []  # outstanding transactions

    # load_data()
# saving data of transactions to make it persistent

    def save_data(self):
        try:
            with open('blockchain-{}.txt'.format(self.node_id), mode='w') as f:
                # converting each block into dictionary to pass to json.dumps and every transaction list in the block needs to be made a dict so again loop through entire blockchain list create new block and again loop after that to convert every block back to a dict
                save_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transaction], block_el.proof, block_el.timestamp)
                                                           for block_el in self.__chain]]

                f.write(json.dumps(save_chain))
                f.write('\n')
                # converting each block into dictionary to pass to json.dumps here for lists
                save_transaction = [
                    tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(save_transaction))
                f.write('\n')
                f.write(json.dumps(list(self.__peer_nodes)))
        except IOError:
            print('Save failed')

    def get_last_val(self):
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def proof_work(self):  # This function is to generate the initial proof used in mining function
        last_block = self.chain[-1]
        last_hash = hash_util.hash_block(last_block)
        proof = 0  # keeps getting incremented till valid proof condition is satisifed

        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof  # returning the nonce
    # creators proof of work condition

    # 3 param for POW: transaction list,prev hash and proof of work

# function to cross-check with original proof


# def valid_proof(transactions, last_hash, proof):
#     guess = (str([tx.to_ordered_dict() for tx in transactions]) +
#              str(last_hash)+str(proof)).encode()
#     guess_hash = hashlib.sha256(guess).hexdigest()
#     print(guess_hash)
#     return guess_hash[0:2] == '00'
# our condition for proof to be valid is there should be 2 leading 0s


    def get_balance(self, sender=None):
        # getting a list of all the transactions in which given person is the sender or receiver

        # where the participant was the sender
        if sender == None:
            if self.hosting_node == None:
                return None
            participant = self.hosting_node
        else:
            participant = sender
        tran_sender = [[key.amount for key in block.transaction if key.sender == participant]
                       for block in self.chain]

        open_trans_sender = [key.amount
                             for key in self.__open_transactions if key.sender == participant]

        tran_sender.append(open_trans_sender)

        debit = functools.reduce(
            lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tran_sender, 0)

        tran_receiver = [[key.amount for key in block.transaction
                          if key.receiver == participant] for block in self.chain]

        credit = functools.reduce(lambda tx_sum, tx_amt: tx_sum +
                                  sum(tx_amt) if len(tx_amt) > 0 else tx_sum+0, tran_receiver, 0)

        return credit-debit  # get balance

    def mining(self):  # function to add mined blocks
        # initially only the genesis block is there
        if self.hosting_node == None:
            return None

        last_block = self.__chain[-1]
        # for now just a concatenation of the values of the block
        hash_code = hash_util.hash_block(block=last_block)
        proof = self.proof_work()
        reward_transaction = Transaction(
            'THEBANKER', self.hosting_node, '', MINING_AMOUNT)
        # reward_transaction = OrderedDict(
        #     [('sender', 'THBANKER'), ('receiver', owner), ('amount', MINING_AMOUNT)])
        # adding to the list of the open transactions
        # creating a copy of the transcations so if mining of a block should fail open transaction shouldnt be affected
        copy_transactions = self.__open_transactions[:]
        for tx in copy_transactions:
            if not Wallet.verify_transaction(tx):
                return None
        copy_transactions.append(reward_transaction)
        block = Block(len(self.__chain), hash_code, copy_transactions, proof)

        # block = {
        #     'previous_hash': hash_code,
        #     'index': len(blockchain),  # will increase in every addition
        #     'transaction': copy_transactions,
        #     'proof': proof
        # }
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        for node in self.__peer_nodes:
            url = 'http://{}/broadcast-block'.format(node)
            converted_block = block.__dict__.copy()
            converted_block['transaction'] = [
                tx.__dict__ for tx in converted_block['transaction']]
            try:
                response = requests.post(url, json={'block': converted_block})
                if response.status_code == 400 or response.status_code == 500:
                    print('Block declined needs resolving')
                if response.status_code == 409:
                    self.resolve_conflicts = True
            except requests.exceptions.ConnectionError:
                continue
        return block

    def new_transaction(self, receiver, sender, signature, amount=1.0, is_receiving=False):
        '''adding a new transaction
        Arguments:
            :sender:Who sends the coins
            :receiver: Who receives the coins
            :amount: The amount being transferred
        '''
        # if self.hosting_node == None:
        #     return False

        transaction = Transaction(
            sender, receiver, signature, amount)

        # transaction = OrderedDict(
        #     [('sender', sender),
        #      ('receiver', recipient),
        #      ('amount', amount)])

        # checking if transaction is valid
        print(Verification.verify_transaction(transaction, self.get_balance))
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            # participants.add(sender)
            # participants.add(recipient)
            self.save_data()
            # broadcasting to all peer nodes about the added transaction
            # if we are not the ones receiving only then 'we' need to broadcast
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/broadcast-transaction'.format(node)
                    try:
                        response = requests.post(
                            url, json={'sender': sender, 'receiver': receiver, 'amount': amount, 'signature': signature})
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined needs resolving')
                            return False
                    except requests.exceptions.ConnectionError:
                        continue
            return True
        return False

    def add_block(self, block):
        transactions = [Transaction(
            tx['sender'], tx['receiver'], tx['signature'], tx['amount']) for tx in block['transaction']]
        proof_is_valid = Verification.valid_proof(
            transactions[:-1], block['previous_hash'], block['proof'])
        # the last block's hash in the current node's blockchain should be equal to incoming nodes prev hash
        hashes_match = hash_util.hash_block(
            self.chain[-1]) == block['previous_hash']
        if not proof_is_valid or not hashes_match:
            return False
        converted_block = Block(
            block['index'], block['previous_hash'], transactions, block['proof'], block['timestamp'])
        # appending to current nodes chain
        self.__chain.append(converted_block)
        stored_transactions = self.__open_transactions[:]
        for itx in block['transaction']:
            for opentx in stored_transactions:
                if opentx.sender == itx['sender'] and opentx.receiver == itx['receiver'] and opentx.amount == itx['amount'] and opentx.signature == itx['signature']:
                    try:
                        self.__open_transactions.remove(opentx)
                    except ValueError:
                        print('Item was already removed')
        self.save_data()
        return True

    def resolve(self):
        winner_chain = self.chain
        replace = False
        # resolving the longer valid chain wins problem
        for node in self.__peer_nodes:
            url = 'http://{}/chain'.format(node)
            try:
                response = requests.get(url)
                node_chain = response.json()
                node_chain = [Block(block['index'], block['previous_hash'],  [Transaction(tx['sender'], tx['receiver'], tx['signature'], tx['amount'])
                                                                              for tx in block['transaction']],
                                    block['proof'], block['timestamp']) for block in node_chain]
                # node_chain.transaction = [Transaction(tx['sender'], tx['receiver'], tx['signature'], tx['amount'])
                #                           for tx in node_chain['transaction']]
                node_chain_length = len(node_chain)
                local_chain_length = len(self.chain)
                # local is the current port eg 5001 and node chain is initial one to which peer was added
                if node_chain_length > local_chain_length and Verification.verify_chain(node_chain):
                    winner_chain = node_chain
                    replace = True
            except requests.exceptions.ConnectionError:
                continue
        self.resolve_conflicts = False
        self.chain = winner_chain
        if replace:
            self.__open_transactions = []
        self.save_data()
        return replace

    def add_peer_node(self, node):
        self.__peer_nodes.add(node)
        self.save_data()

    def remove_peer_node(self, node):
        self.__peer_nodes.discard(node)
        self.save_data()

    def get_peer_nodes(self):
        '''returning a list of all peer nodes'''
        return list(self.__peer_nodes)
    # def add_value(amount,
    #             last_transaction):
    #     if last_transaction == None:
    #         blockchain.append([amount])
    #     else:
    #         blockchain.append([last_transaction, amount])
    #     print(blockchain)

    # def get_input():
    #     t_receiver = input('Enter the receiver:')
    #     t_amount = float(input('Please enter your transaction amount:'))
    #     print(t_amount)
    #     return t_receiver, t_amount

    # def get_choice():
    #     user_input = input('Enter your choice:')
    #     return user_input

    # def output_blockchain():
    #     for block in blockchain:
    #         print('Block')
    #         print(block)
    #     else:
    #         print('*'*25)

    # def verify_transaction(transaction):
    #     print(transaction.sender)
    #     balance_sender = get_balance(transaction.sender)
    #     if balance_sender >= transaction.amount:
    #         return True
    #     else:
    #         return False
'''the stored hash in one block gets compared with the recalculated hash of the prev block
'''


# def verify_chain():

#     for (index, block) in enumerate(blockchain):
#         if index == 0:
#             continue  # genesis block shouldnt be checked
#         if block.previous_hash != hash_util.hash_block(blockchain[index-1]):
#             return False
#         # to remove the last transaction which is a reward transaction
#         if not valid_proof(block.transaction[:-1], block.previous_hash, block.proof):
#             print('Invalid Proof of Work')
#             return False
#     return True


# def verify_all_transaction():
#     return all([verify_transaction(tran) for tran in open_transactions])


# checking if all transactions are valid
# for the remaining iterations
# quit_loop = True
# while quit_loop:
#     print('Please enter your choice:')
#     print('1. Add a new transaction')
#     print('2.Output the blockchain blocks')
#     print('3.Mine a new block')
#     print('4.Get balance')
#     print('5.Check transaction validity')
#     # print('h:To manipulate the chain')
#     print('q for quitting')
#     user_choice = get_choice()
#     if user_choice == '1':
#         transaction_data = get_input()

#         receiver, amount = transaction_data

#         if new_transaction(receiver, amount=amount):
#             print('Transaction Added')
#         else:
#             print('Transaction failed')
#             # add_value(last_transaction=get_last_val(), amount=transaction_amount)
#             # print(open_transactions)

#     elif user_choice == '2':
#         output_blockchain()
#     elif user_choice == '3':
#         if mining():
#             open_transactions = []
#             save_data()
#     elif user_choice == 'q':
#         quit_loop = False
#     elif user_choice == '4':
#         print(get_balance('Sharat'))
#     elif user_choice == '5':
#         verifier = Verification()
#         if verifier.verify_all_transaction(open_transactions, get_balance):
#             print('All transactions are valid')
#         else:
#             print('There are some invalid Transactions')

#     # elif user_choice == 'h':
#     #     if len(blockchain) >= 1:
#     #         blockchain[0] = {
#     #             'previous_hash': '',
#     #             'index': 0,
#     #             'transaction': [{'sender': 'spk', 'receiver': 'david', 'amount': 60}]
#     #         }
#     verifier = Verification()
#     if not verifier.verify_chain(blockchain):
#         print('The chain has been corrupted')
#         break
#     print('Balance of {}:{:1.2f}'.format(
#         'Sharat', get_balance(participant='Sharat')))
#     # input turned out to be invalid

# else:
#     print('User quit')


# print('done')
# add_value(get_input())
# add_value(last_transaction=get_last_val(), amount=0.9)
# add_value(10.56, get_last_val())
