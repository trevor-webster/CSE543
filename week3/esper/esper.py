import argparse
import os
import time
import sys
import string

# Handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt", help='Decrypt a file', required=False)
parser.add_argument("-e", "--encrypt", help='Encrypt a file', required=False)
parser.add_argument("-o", "--outfile", help='Output file', required=False)

args = parser.parse_args()

encrypting = True

try:
    ciphertext = open(args.decrypt, "rb").read()
    try:
        plaintext = open(args.encrypt, "rb").read()
        print("You can't specify both -e and -d")
        exit(1)
    except Exception:
        encrypting = False
except Exception:
    try:
        plaintext = open(args.encrypt, "rb").read()
    except Exception:
        print("Input file error (did you specify -e or -d?)")
        exit(1)

def lrot(n, d):
    return ((n << d) & 0xff) | (n >> (8 - d))

def rrot(n, d):
    return ((n >> d) ) | ((n << (8 - d)& 0xff))


# decrypts only bytes, doesn't apply encoding
def decrypt(ciphertext, key, keyrotate):
    plaintext2 = []    
    keyxor2 = []
    for i in range(0,len(key)):
        keyxor2.append(ord(key[i]))

    for i in range(0, len(ciphertext)):
        plaintext2.append(rrot((ciphertext[i] ^ keyxor2[i % len(keyxor2)]), keyrotate))
   
    return plaintext2

if encrypting:
    #
    # Esper cipher
    #
    
    # Get the key
    key = 'rORTrfA'
    keyrotate = 2
    keyxor = []
    
    # Rotate the key
    for i in range(0,len(key)):
        keyxor.append(ord(key[i]))
    print("The key is %s rotated by %d bits." % (key, keyrotate))
    print(f"keyxor {keyxor}")
    ciphertext = []
    for i in range(0, len(plaintext)):
        ciphertext.append(lrot(plaintext[i], keyrotate) ^ keyxor[i % len(keyxor)])

    
    with open(args.outfile, "wb") as output:
        output.write(bytes(ciphertext))
        output.close()
else:
    key = 'rORTrfA'
    keyrotate = 2
    plaintext2 = decrypt(ciphertext,key,keyrotate)    
    plaintext2 = ''.join(map(lambda a : chr(a), plaintext2)   )    
    print(f"Decryption {plaintext2}") 
    plaintext2 = bytes(plaintext2,'utf-8')
    with open(args.outfile, "wb") as output:
        output.write(plaintext2)
        output.close()
    
    exit(0)

