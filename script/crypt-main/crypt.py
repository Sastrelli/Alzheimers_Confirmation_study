import argparse
import base64
import hashlib
import os
from select import kevent

from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()
	 
def write_key(key=None):
    '''
    Generates a key and saves it into a file
    '''
    if not key:
        key = Fernet.generate_key()
    with open(os.path.expanduser('~/.usr_scripts/cryptography/key.key'), 'wb') as key_file:
        key_file.write(key)

def load_key():
    '''
    Loads the key from the current directory named 'key.key'
    '''
    # check if key exists
    try:
        return open(os.path.expanduser('~/.usr_scripts/cryptography/key.key'), 'rb').read()
    except:
        print('Please generate a key first.\nUse --command generate_key to generate a key.')
        exit()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    print(key)
    f = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
        print('file has been encrypted.')

def decrypt(filename, key):
	"""
	Given a filename (str) and key (bytes), it decrypts the file and write it
	"""
	f = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))

	with open(filename, "rb") as file:
		# read the encrypted data
		encrypted_data = file.read()

	# decrypt data
	decrypted_data = f.decrypt(encrypted_data)

	# write the original file
	with open(filename, "wb") as file:
		file.write(decrypted_data)
		print('file has been decrypted.')

if __name__ == "__main__":
    # parse the command-line arguments
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files.')
    # read 'encrypt' or 'decrypt' from the command line
    parser.add_argument('--command', help='Command to execute. Options: generate_key, set_system_key, encrypt, decrypt')
    # read the filename from the command line
    parser.add_argument('--filename', help='The file path to encrypt/decrypt file')
    # read output filename from the command line
    parser.add_argument('--output_filename', help='The output encrypt/decrypt file path')
    # read the key (if it exists)
    parser.add_argument('--key', help='The key for encryption/decryption')
    args = parser.parse_args()

    # if generate_key command is passed
    if args.command == 'generate_key':
        # print generated key
        print('Generated key: ', generate_key().decode())
        exit()

    # if set_system_key command is passed
    if args.command == 'set_system_key':
        # set system key
        if not args.key:
            print('Please provide a key to set the system key')
            exit()
        write_key(args.key.encode())
        print('System key has been set')
        exit()

    # system_key = load_key()
    system_key = None
    
    # if encrypt command is passed
    if args.command == 'encrypt':
        # encrypt the file
        if not args.key and not system_key:
            print('Please provide a key to encrypt the file or set system key.\nUse --command generate_key to generate a key.')
            exit()
        if args.key:
            encrypt(args.filename, args.key)
            print('Provided key used for encryption')
            exit()
        if system_key:
            encrypt(args.filename, system_key)
            print('System key used for encryption')
            exit()

    # if decrypt command is passed
    if args.command == 'decrypt':
        # decrypt the file
        if not args.key and not system_key:
            print('Please provide a key to decrypt the file')
            exit()
        if args.key:
            decrypt(args.filename, args.key)
            print('Provided key used for decryption')
            exit()
        if system_key:
            decrypt(args.filename, system_key)
            print('System key used for decryption')
            exit()

    # if no command is passed
    if not args.command:
        print('Please specify a command. Type "--help" for instructions.')
        exit()
