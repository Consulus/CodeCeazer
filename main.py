SYMBOLS = 'АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Что делаем с текстом - шифруем или де-шифруем?')
        mode = input().lower()
        if mode in ["шифруем", "ш", "де-шифруем", "де"]:
            return mode
        else:
            print(
                'Введите "шифруем" или "ш" для зашифровки или "де-шифруем" или "д" для расшифровки')


def getMessage():
    print('Введите текст:')
    return input()


def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        else:
            print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'ш':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
key = getKey()
print('Преобразованный текст:')
print(getTranslatedMessage(mode, message, key))
