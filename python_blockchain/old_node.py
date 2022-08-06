from uuid import uuid4

from Crypto import Signature  # to generate unique ids
from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet
# class for user interface methods and attributes


class Node:
    # every node will have its copy of the blockchain
    def __init__(self):
        #self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        # after generating public key we create the blockchain with that id
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_input(self):
        t_receiver = input('Enter the receiver:')
        t_amount = float(input('Please enter your transaction amount:'))
        print(t_amount)
        return t_receiver, t_amount

    def get_choice(self):
        user_input = input('Enter your choice:')
        return user_input

    def output_blockchain(self):
        for block in self.blockchain.get_chain():
            print('Block')
            print(block)
        else:
            print('*'*25)

    def wait_for_input(self):
        quit_loop = True

        while quit_loop:
            print('Please enter your choice:')
            print('1. Add a new transaction')
            print('2.Output the blockchain blocks')
            print('3.Mine a new block')
            print('4.Get balance')
            print('5.Check transaction validity')
            print('6.Create Wallet')
            print('7.Load Wallet')
            print('8.Save keys')
            # print('h:To manipulate the chain')
            print('q for quitting')
            user_choice = self.get_choice()
            if user_choice == '1':
                transaction_data = self.get_input()

                receiver, amount = transaction_data
                signature = self.wallet.sign_transaction(
                    self.wallet.public_key, receiver, amount)
                if self.blockchain.new_transaction(receiver, self.wallet.public_key, signature, amount=amount):
                    print('Transaction Added')
                else:
                    print('Transaction failed')
                    # add_value(last_transaction=get_last_val(), amount=transaction_amount)
                    # print(open_transactions)

            elif user_choice == '2':
                self.output_blockchain()
            elif user_choice == '3':
                if not self.blockchain.mining():
                    print('Mining failed.NO exisiting wallet')
                # open_transactions = []
                # save_data()
            elif user_choice == 'q':
                quit_loop = False
            elif user_choice == '4':
                print(self.blockchain.get_balance())
            elif user_choice == '5':

                if Verification.verify_all_transaction(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are some invalid Transactions')
            elif user_choice == '6':
                self.wallet.create_keys()
        # after generating public key we create the blockchain with that id
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                # elif user_choice == 'h':
                #     if len(blockchain) >= 1:
                #         blockchain[0] = {
                #             'previous_': '',
                #             'index': 0,
                #             'transaction': [{'sender': 'spk', 'receiver': 'david', 'amount': 60}]
                #         }
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '8':
                self.wallet.save_keys()
            if not Verification.verify_chain(self.blockchain.get_chain()):
                print('The chain has been corrupted')
                break
            print('Balance of {}:{:1.2f}'.format(
                self.wallet.public_key, self.blockchain.get_balance(

                )))
            # input turned out to be invalid

        else:
            print('User quit')

        print('done')


node = Node()
node.wait_for_input()
