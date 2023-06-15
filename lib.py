import sys
import PyPDF2
import tabula
import pandas as pd
import difflib
import re
import numpy


def convertAllInDirectory(dir, format):
    try:
        tabula.convert_into_by_batch(dir, output_format=format, pages='all')
    except Exception as e:
        print(e)



def correct_wordlist(dir):
    try:
        reader = PyPDF2.PdfReader(dir)
        number_of_pages = len(reader.pages)

        allText = []

        for page_num in range(number_of_pages):

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

dirs = r"/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/test2.pdf"

df = tabula.read_pdf(dirs, pages='all', stream = True)
wordlist = correct_wordlist(dirs)
list = []

for i in df:
    list.append(i.values.tolist())

def find_similar_word(word, word_list):
    try:
        matches = difflib.get_close_matches(word, word_list, n=1)
        return word if len(matches) == 0 else matches[0]
    except Exception as e:
        return word
    

for i in range(len(list)):
    for x in range(len(list[i])):
        for k in range(len(list[i][x])):
            if(str(list[i][x][k]).isnumeric() == True):
                continue
            else:
                # print("text")
                list[i][x][k] = find_similar_word(list[i][x][k], wordlist)
            # print(list[i][x][k])

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
