from math import ceil

def FillLetters(text):
    newText = ''
    currentIndex = 0
    withinGroup = 0

    while currentIndex != len(text):
        if currentIndex != 0 and text[currentIndex] == newText[currentIndex - 1] and withinGroup < 2:
            newText += 'X'

        if withinGroup >= 2:
            withinGroup = 0

        newText += text[currentIndex]
        currentIndex += 1
        withinGroup += 1

    if (len(newText) % 2) != 0:
        newText += 'Z'

    print(newText)

    return newText

def Diagraph(text):
    length = ceil(len(text) / 2)
    Diagraph = ['' for i in range(length)]
    currIndex = 0
    textCount = 0

    for i in range(len(text)):
        if textCount >= 2:
            textCount = 0
            currIndex += 1

        Diagraph[currIndex] += text[i]
        textCount += 1

    return Diagraph

def GenkeyMatrix(key):
    keyMatrix = []
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    keyLetters = []
    for letter in key:
        if letter not in keyLetters:
            keyLetters.append(letter)

    for letter in alphabetList:
        if letter not in keyLetters:
            keyLetters.append(letter)

    while keyLetters != []:
        keyMatrix.append(keyLetters[:5])
        keyLetters = keyLetters[5:]

    for row in keyMatrix:
        print(row)

    return keyMatrix

def SearchkeyMatrix(letter, keyMatrix):
    for row in range(5):
        for column in range(5):
            if keyMatrix[row][column] == letter:
                return row, column
    
    return -1, -1

def EncryptColumnRule(diagraph, keyMatrix):
    newDiagraph = ''
    for i in range(len(diagraph)):
        row, column = SearchkeyMatrix(diagraph[i], keyMatrix)

        if row == 4:
            newDiagraph += keyMatrix[0][column]
        else:
            newDiagraph += keyMatrix[row + 1][column]

    return newDiagraph

def DecryptColumnRule(diagraph, keyMatrix):
    newDiagraph = ''
    for i in range(len(diagraph)):
        row, column = SearchkeyMatrix(diagraph[i], keyMatrix)

        if row == 0:
            newDiagraph += keyMatrix[4][column]
        else:
            newDiagraph += keyMatrix[row - 1][column]

    return newDiagraph

def EncryptRowRule(diagraph, keyMatrix):
    newDiagraph = ''
    for i in range(len(diagraph)):
        row, column = SearchkeyMatrix(diagraph[i], keyMatrix)

        if column == 4:
            newDiagraph += keyMatrix[row][0]
        else:
            newDiagraph += keyMatrix[row][column + 1]

    return newDiagraph

def DecryptRowRule(diagraph, keyMatrix):
    newDiagraph = ''
    for i in range(len(diagraph)):
        row, column = SearchkeyMatrix(diagraph[i], keyMatrix)

        if column == 0:
            newDiagraph += keyMatrix[row][4]
        else:
            newDiagraph += keyMatrix[row][column - 1]

    return newDiagraph

def EncryptDefaultRule(diagraph, keyMatrix):
    letterRows = [0, 0]
    letterColumns = [0, 0]

    for i in range(len(diagraph)):
        letterRows[i], letterColumns[i] = SearchkeyMatrix(diagraph[i], keyMatrix)

    newFirstLetterRow = letterRows[0]
    newFirstLetterColumn = letterColumns[1]

    newSecondLetterRow = letterRows[1]
    newSecondLetterColumn = letterColumns[0]

    newDiagraph = (keyMatrix[newFirstLetterRow][newFirstLetterColumn]) + (keyMatrix[newSecondLetterRow][newSecondLetterColumn])

    return newDiagraph

def EncryptText(text, key):
    key = key.upper()
    text = text.upper()
    words = text.split()
    keyMatrix = GenkeyMatrix(key)
    encryptedText = ''

    for word in words:
        diagraphs = Diagraph(FillLetters(word))

        for diagraph in diagraphs:
            firstRow, firstColumn = SearchkeyMatrix(diagraph[0], keyMatrix)
            secondRow, secondColumn = SearchkeyMatrix(diagraph[1], keyMatrix)
            
            # Check if in same row
            if firstRow == secondRow:
                encryptedText += EncryptRowRule(diagraph, keyMatrix)
            # Check if in same column
            elif firstColumn == secondColumn:
                encryptedText += EncryptColumnRule(diagraph, keyMatrix)
            # Default
            else:
                encryptedText += EncryptDefaultRule(diagraph, keyMatrix)

        encryptedText += ' '

    return encryptedText

def DecryptText(text, key):
    key = key.upper()
    text = text.upper()
    words = text.split()
    keyMatrix = GenkeyMatrix(key)
    decryptedText = ''

    for word in words:
        diagraphs = Diagraph(word)

        for diagraph in diagraphs:
            firstRow, firstColumn = SearchkeyMatrix(diagraph[0], keyMatrix)
            secondRow, secondColumn = SearchkeyMatrix(diagraph[1], keyMatrix)
            
            # Check if in same row
            if firstRow == secondRow:
                decryptedText += DecryptRowRule(diagraph, keyMatrix)
            # Check if in same column
            elif firstColumn == secondColumn:
                decryptedText += DecryptColumnRule(diagraph, keyMatrix)
            # Default
            else:
                decryptedText += EncryptDefaultRule(diagraph, keyMatrix)

        decryptedText += ' '

    return decryptedText

key = input("Enter a key: ")
encryptedText = EncryptText(input('Enter text: '), key)
print(encryptedText)
print(DecryptText(encryptedText, key))

