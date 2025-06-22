import dictionary as d
import richWord as rw
from richWord import RichWord


class MultiDictionary:

    def __init__(self):
        self._dizionario = dict()

    def addDictionaries(self):
        dizIt = d.Dictionary("italian")
        dizIt.loadDictionary()
        dizEn = d.Dictionary("english")
        dizEn.loadDictionary()
        dizSp = d.Dictionary("spanish")
        dizSp.loadDictionary()
        self._dizionario["italian"] = dizIt.dict
        self._dizionario["english"] = dizEn.dict
        self._dizionario["spanish"] = dizSp.dict

    def printDic(self, language):
        diz = self._dizionario.get(language)
        myStr = ""
        for word in diz:
            myStr += word + "\n"
        print(myStr)

    def searchWord(self, words, language):
        listaRichWord = []
        diz = self._dizionario.get(language)
        for word in words:
            nuovaRW = RichWord(word)
            listaRichWord.append(nuovaRW)
            if diz.__contains__(word):
                nuovaRW.corretta = True
            else:
                nuovaRW.corretta = False
        return listaRichWord

    def searchWordLinear(self, words, language):
        listaRichWord = []
        diz = self._dizionario.get(language)
        for word in words:
            nuovaRW = RichWord(word)
            listaRichWord.append(nuovaRW)
            nuovaRW.corretta = False
            for wordCorretta in diz:
                if wordCorretta == word:
                    nuovaRW.corretta = True
        return listaRichWord

    def searchWordDichotomic(self, words, language):
        listaRichWord = []
        diz = sorted(self._dizionario.get(language))
        for word in words:
            nuovaRW = RichWord(word)
            listaRichWord.append(nuovaRW)
            # Ricerca dicotomica manuale
            sinistra, destra = 0, len(diz) - 1
            while sinistra <= destra:
                medio = (sinistra + destra) // 2
                if diz[medio] == word:
                    nuovaRW.corretta = True
                    break
                elif diz[medio] < word:
                    sinistra = medio + 1
                else:
                    destra = medio - 1
            else:
                nuovaRW.corretta = False  # Se esce dal while senza trovare la parola
        return listaRichWord

