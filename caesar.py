#caeser cipher
def EncryptCaeserCipher(key, value):
    encryptedResult = ""

    for i in range(len(value)):
        char = value[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            encryptedResult += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            encryptedResult += chr((ord(char) + key - 97) % 26 + 97)
        
    return encryptedResult

def DecryptCaeserCipher(key, encryptedKey):
    return EncryptCaeserCipher(26 - key, encryptedKey)

#vernam cipher


caeserKey = int(input("Enter key for caeser cipher: "))

encryptedKey = EncryptCaeserCipher(caeserKey, input("Enter text to encrypt: "))
print("Encrypted Key: " + encryptedKey)

print("Decrypted Key: " + DecryptCaeserCipher(caeserKey, encryptedKey))


