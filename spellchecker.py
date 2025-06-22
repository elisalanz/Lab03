import time

import multiDictionary as md
from richWord import RichWord

class SpellChecker:

    def __init__(self):
        self._multiDict = md.MultiDictionary()
        self._multiDict.addDictionaries()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn).lower()
        words = txtIn.split(" ")
        print("______________________________\nUsing contains")
        tic = time.time()
        listaRW = self._multiDict.searchWord(words, language)
        toc = time.time()
        str = ""
        for rw in listaRW:
            if rw.corretta == False:
                str += rw.__str__() + "\n"
        print(str + f"Time elapsed {toc - tic}")
        print("______________________________\nUsing Linear search")
        tic = time.time()
        listaRW = self._multiDict.searchWordLinear(words, language)
        toc = time.time()
        str = ""
        for rw in listaRW:
            if rw.corretta == False:
                str += rw.__str__() + "\n"
        print(str + f"Time elapsed {toc - tic}")
        print("______________________________\nUsing Dichotomic search")
        tic = time.time()
        listaRW = self._multiDict.searchWordDichotomic(words, language)
        toc = time.time()
        str = ""
        for rw in listaRW:
            if rw.corretta == False:
                str += rw.__str__() + "\n"
        print(str + f"Time elapsed {toc - tic}")
        print()


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text