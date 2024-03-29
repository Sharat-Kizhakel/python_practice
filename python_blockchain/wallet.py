from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import Crypto.Random
import binascii


class Wallet:
    def __init__(self, node_id):
        self.private_key = None
        self.public_key = None
        self.node_id = node_id

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key
        # saving public and private key to a file

    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet-{}.txt'.format(self.node_id), mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                return True
            except(IOError, IndexError):
                print('Saving wallet fails')
                return False

    def load_keys(self):
        try:
            with open('wallet-{}.txt'.format(self.node_id), mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]  # to avoid new line character
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
            return True
        except(IOError, IndexError):
            print('Loading the wallet failed')
            return False

    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        # getting the public key for the given private key
        public_key = private_key.publickey()
        # converting binary to hexadecimal to encode into string
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))

    def sign_transaction(self, sender, receiver, amount):
        signer = PKCS1_v1_5.new(RSA.importKey(
            binascii.unhexlify(self.private_key)))
        # payload is in this hash
        h = SHA256.new((str(sender)+str(receiver)+str(amount)).encode('utf8'))
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):

        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new(
            (str(transaction.sender)+str(transaction.receiver)+str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))
