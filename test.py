# import difflib

# def find_similar_word(word, word_list):
#     match = difflib.get_close_matches(word, word_list)
#     return match

# word_to_match = "จักรกสกร"
# word_list = ["จตรกสก ร", "ชนกนต", "สุขสวย", "constrictor", "boa", "viper", "cobra", "anaconda", "rattlesnake", "adder","pfytdhons"]

# similar_words = find_similar_word(word_to_match, word_list)
# print(similar_words)
# import tabula

# dirs = r"/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/test2.pdf"

# df = tabula.read_pdf(dirs, encoding = 'utf-8' , pages='all')


# print(df)

# df[0].to_csv('out.csv',index=False)



# def convert_to_int(user_input_str):
#     input_list_str = list(user_input_str.split(","))
#     number_list = []
#     for n in input_list_str:
#         if '-' not in n:
#             number_list.append(int(n))
#         else:
#             number_list.extend(range(int(n.split('-')[0]), int(n.split('-')[1]) + 1))
#     return number_list

# list = convert_to_int("1,10,40")

# for i in list:
#     print(type(i))
from typing import List
import sys
import PyPDF2
import tabula
import pandas as pd
import difflib
import re
from typing import List

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
        temp = ''
        allText = []

        for page_num in range(number_of_pages) if page == 'all' else convert_to_int(page):
            print(page_num)
            #Set Page number to PDFreader
            page = reader.pages[page_num]

            # Extract Text
            temp = page.extract_text()
            
            li = re.split(r'\s+|\n', temp)

            new_items = [item for item in li if not item.isdigit()]

            allText = allText + new_items
        
        return temp

    except Exception as e:
        print(e)
        sys.exit()


print(correct_wordlist(r"/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/test3.pdf", '11'))
# print(convert_to_int('10'))