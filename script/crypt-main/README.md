# Crypt
Crypt is a command-line tool for encrypting and decrypting files using the Fernet symmetric encryption method from the python cryptography library. Install by running 'install.sh' on terminal.

# Setup

## Generate a System Key
Start by generating a system key:

~~~
crypt --command generate_key
~~~

This will output a key. Copy this key.

## Set the System Key
Next, set the system key by pasting the copied key in place of [PASTE]

~~~
crypt --command set_system_key --key [PASTE]
~~~

This will create a system key that can be used to encrypt and decrypt files.

# Usage

## Encryption
To encrypt a file, use the following command, replacing [PATH_TO_FILE] with the path to the file you want to encrypt:

~~~
crypt --command encrypt --filename [PATH_TO_FILE]
~~~

This will overwrite the original file with its encrypted content. You can also specify a custom key for encryption by adding the --key argument:

~~~
crypt --command encrypt --filename [PATH_TO_FILE] --key [YOUR_KEY]
~~~

## Decryption

To decrypt a file, use the following command, replacing [PATH_TO_FILE] with the path to the encrypted file:

~~~
crypt --command decrypt --filename [PATH_TO_FILE]
~~~

This will overwrite the encrypted file with its decrypted content.

Again, you can also specify a custom key for decryption by adding the --key argument:

~~~
crypt --command decrypt --filename [PATH_TO_FILE] --key [YOUR_KEY]
~~~

Please note that the key used for decryption must be the same as the key used for encryption.

