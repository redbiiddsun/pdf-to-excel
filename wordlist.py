import PyPDF2
import re
from typing import List

class Wordlist:
    
    def __init__(self, dir: str) -> None:
        self.dir = dir
        self.file = PyPDF2.PdfReader(dir)

    def getAllPageNumber(self) -> int:
        return len(self.file.pages)
    
    def getWordList() -> List:
        print("")

    def removeSpecialChar(list) -> List:
        tempList  = re.split(r'\s+|\n', list)
        return [item for item in tempList if not item.isdigit()]
    
def main():
    tdemp = Wordlist(2)
    print(tdemp.dir)
    
if __name__ == "__main__":
    main()

