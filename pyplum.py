import pdfplumber
import pandas as pd
from pythainlp.util import normalize
from pythainlp import correct

def extract_table_from_pdf(pdf_path, page_number, empty = True):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]

        # Extract the table using the extract_table() method
        table = page.extract_table()

        if (empty is True):
            # Remove Empty Column
            for i in table:
                while("" in i):
                    i.remove("")

            return table
        else:
            return table

list = extract_table_from_pdf("/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/test2.pdf", 0, False)

for i in range(len(list)):
    for x in range(len(list[i])):
        print(list[i][x])
        list[i][x] = list[i][x].replace(" ", "")
        text = list[i][x]
        text = normalize(text)
        list[i][x] = text

print(list)

df = pd.DataFrame(list)

print(df)

df.to_csv('out.csv',index=False)