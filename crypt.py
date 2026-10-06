'''
Made on 10/6/2026

Ceaser cipher encrypt and decrypt
'''




# ask if user want to encrypt or decrypt

mode = str(input("Enter 'e' if you want to encrypt and 'd' if you want to decrypt"))

# input the string

text = str(input("Enter text here:\n"))
key = int(input("How many letters is it shifted?\n"))
negnum = -abs(key)

# encrypt (or decrypt) the string


def encrypt(text, shift):
    
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift -65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift -97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift -65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift -97) % 26 + 97)
        else:
            result += char

    return result


# final if statments and print results


if mode == "e":
    encryptedmes = encrypt(text, key)
    print("")
    print("Encrypted:")
    print(encryptedmes)

elif mode == "d":
    encryptedmes = decrypt(text,negnum)
    print("")
    print("Decrypted:")
    print(encryptedmes)


