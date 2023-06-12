from PyPDF2 import PdfReader
import PyPDF2
import tabulate

reader = PdfReader(r"C:\Users\tgsav\OneDrive\Desktop\pdf-to-excel\test\test2.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)


def extract_pdf_table(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PdfReader(pdf_path)
    
    # Extract text from the PDF
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[0]
        text += page.extract_text()
        
    print(text) 
    # Split text into lines and identify table structure
    # lines = text.split('\n')
    # table = []
    # for line in lines:
    #     # Identify table rows based on a pattern or line structure
    #     # Example: Check if line starts with a specific character or if it contains multiple columns separated by a delimiter
    #     if line.startswith('A') and '\t' in line:
    #         row = line.split('\t')
    #         table.append(row)
    
    # return table


print(extract_pdf_table(r"C:\Users\tgsav\OneDrive\Desktop\pdf-to-excel\test\test2.pdf"))