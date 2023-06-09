# from pythainlp.util import normalize
# from pythainlp import spell
# from pythainlp import correct


# text = "จ ี"

# text = correct(text)


# print(text)


import fitz
doc = fitz.open('C:\Users\tgsav\OneDrive\Desktop\pdf-to-excel/test/test2.pdf')
text = ""
for page in doc:
   text+=page.get_text()
print(text)
