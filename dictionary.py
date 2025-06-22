class Dictionary:

    def __init__(self, language):
        self._dict = []
        self._language = language

    def loadDictionary(self):
        path = ""
        if self._language == "italian":
            path = "resources/Italian.txt"
        elif self._language == "english":
            path = "resources/English.txt"
        elif self._language == "spanish":
            path = "resources/Spanish.txt"
        try:
            fileDictionary = open(path, "r", encoding="utf-8")
            for line in fileDictionary:
                word = line.strip()
                self._dict.append(word)
            fileDictionary.close()
        except IOError:
            pass

    def printAll(self):
        myStr = ""
        for word in self._dict:
            myStr += word + "\n"
        print(myStr)

    @property
    def dict(self):
        return self._dict