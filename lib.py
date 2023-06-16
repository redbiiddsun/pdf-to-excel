from typing import List
import sys
import PyPDF2
import tabula
import pandas as pd
import difflib
import re
from typing import List


def convertAllInDirectory(dir, format):
    try:
        tabula.convert_into_by_batch(dir, output_format=format, pages='all')
    except Exception as e:
        print(e)

def convert_to_int(user_input_str):
    input_list_str = list(user_input_str.split(","))
    number_list = []
    for n in input_list_str:
        if '-' not in n:
            number_list.append(int(n))
        else:
            number_list.extend(range(int(n.split('-')[0]), int(n.split('-')[1]) + 1))
    return number_list

def correct_wordlist(dir: str,page: str):
    try:
        reader = PyPDF2.PdfReader(dir)
        number_of_pages = 0

        allText = []

        for page_num in range(number_of_pages) if page == 'all' else convert_to_int(page):

            #Set Page number to PDFreader
            page = reader.pages[page_num]

            # Extract Text
            temp = page.extract_text()
            
            li = re.split(r'\s+|\n', temp)

            new_items = [item for item in li if not item.isdigit()]

            allText = allText + new_items
        
        return allText

    except Exception as e:
        print(e)
        sys.exit()

dirs = r"/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/test3.pdf"

df = tabula.read_pdf(dirs, pages='10')
wordlist = correct_wordlist(dirs, '9') # Becareful pagenum this need to be page-1
list = []

for i in df:
    list.append(i.T.reset_index().values.T.tolist())
    
def find_similar_word(word: str, word_list: List[str]):
    try:
        matches = difflib.get_close_matches(word, word_list, n=1)
        
        return word if len(matches) == 0 else matches[0]
    except Exception as e:
        return word

print(wordlist)

for i in range(len(list)):
    for x in range(len(list[i])):
        for k in range(len(list[i][x])):
            if(str(list[i][x][k]).isnumeric() == True):
                continue
            else:
                # print("text")
                # print(list[i][x][k])
                # print('------------------------')
                # print(find_similar_word(list[i][x][k], wordlist))
                list[i][x][k] = find_similar_word(list[i][x][k], wordlist)
                



print(list)


my_list = [l for li in list for l in li]
print(my_list)
df = pd.DataFrame(my_list)

print(df)
df.to_csv("output.csv", index=False)

# convertAllInDirectory("/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/", "csv")    
# tabula.convert_into("/mnt/c/Users/Phanasorn/Desktop/PJ/test/MOCK_DATA_SEVERALPAGE.pdf", "output.csv", output_format="csv", pages='all')
# print(wordlist)

# df = tabula.convert_into(dirs, "output.csv", output_format="csv")
# print(df)
