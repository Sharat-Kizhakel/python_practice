import hashlib
from utility.hash_util import hash_block
from wallet import Wallet


class Verification:
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) +
                 str(last_hash)+str(proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        print(guess_hash)
        return guess_hash[0:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain):

        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue  # genesis block shouldnt be checked
            if block.previous_hash != hash_block(blockchain[index-1]):
                return False
            # to remove the last transaction which is a reward transaction
            if not cls.valid_proof(block.transaction[:-1], block.previous_hash, block.proof):
                print('Invalid Proof of Work')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
      # checkfund being used to avoid redundant checks of balance when its already in open transction
        if check_funds:
            balance_sender = get_balance(transaction.sender)
            if balance_sender >= transaction.amount and Wallet.verify_transaction(transaction):
                return True
            else:
                return False
        else:
            return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_all_transaction(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tran, get_balance, False) for tran in open_transactions])
