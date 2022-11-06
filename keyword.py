def GenKeyMap(keyword):
    keyMap = {}
    keyword = keyword.upper()
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    keyLetters = []
    for letter in keyword:
        if letter not in keyLetters:
            keyLetters.append(letter)

    for letter in alphabetList:
        if letter not in keyLetters:
            keyLetters.append(letter)

    for i in range(len(alphabetList)):
        keyMap[alphabetList[i]] = keyLetters[i]

    return keyMap

def GetDecryptMap(map):
    newMap = {}

    for letterMap in map:
        newMap[map[letterMap]] = letterMap

    return newMap

def MapWordLetters(word, map):
    newWord = ''
    for letter in word:
        newWord += map[letter]

    return newWord

def EncryptText(text, keyword):
    keyMap = GenKeyMap(keyword)
    text = text.upper()
    words = text.split()
    newText = ''

    for word in words:
        newText += MapWordLetters(word, keyMap)

        newText += ' '
        
    return newText

def DecryptText(text, keyword):
    decryptMap = GetDecryptMap(GenKeyMap(keyword))
    text = text.upper()
    words = text.split()
    newText = ''

    for word in words:
        newText += MapWordLetters(word, decryptMap)

        newText += ' '
        
    return newText


encryptedText = EncryptText('Zombie Here', 'secret')
print(encryptedText)
print(DecryptText(encryptedText, 'secret'))

        
