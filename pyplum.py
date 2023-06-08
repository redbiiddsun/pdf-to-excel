import pdfplumber
import pandas as pd
from pythainlp.util import normalize
from pythainlp import correct

def extract_table_from_pdf(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]

        # Extract the table using the extract_table() method
        table = page.extract_tables()

        # Remove Empty Column
        for i in table:
            while("" in i):
                i.remove("")

    return table

def extract_tables_from_pdf_all(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            temp = extract_table_from_pdf(pdf_path, page)
            print(temp)
        




list = extract_table_from_pdf("/mnt/c/Users/Phanasorn/Desktop/pdf-to-excel/test/Pre-Freshy_2022.pdf",1)




# for i in range(len(list)):
#     for x in range(len(list[i])):
#         # print(list[i][x])
#         list[i][x] = list[i][x].replace(" ", "")
#         text = list[i][x]
#         text = normalize(text)
#         list[i][x] = text


print(list)

# df = pd.DataFrame(list)

# df.to_csv('out.csv',index=False)