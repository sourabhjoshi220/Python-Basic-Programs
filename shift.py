import string
alphabet=string.ascii_lowercase

alphabet="abcdefghijklmnopqrstuvwxyz"

def encrypt(string, shift=4):
    encrypt_string=""
    for c in string:
        index=alphabet.index(c)
        shifted_index=(index + shift) % len(alphabet)
        encrypted_string += alphabet[shifted_index]
    return encrypted_string
    print(encrypt("PythonLearning"))
