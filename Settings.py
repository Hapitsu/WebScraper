def loadSettings():
    dictionary = {}
    with open('settings.txt', 'r') as settings:
        for line in settings:
            line = line.replace('\n', '')
            splitLine = line.split('=', 1)
            dictionary[splitLine[0]] = splitLine[1]
    return dictionary