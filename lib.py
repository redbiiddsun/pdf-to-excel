import tabula
import pandas as pd

def convertAllInDirectory(dir, format):
    try:
        tabula.convert_into_by_batch(dir, output_format=format, pages='all')
    except Exception as e:
        print(e)

def convertFileIntoSeparate(dir, format):
    try:
        tabula.convert_into_by_batch(dir, output_format=format, pages='all')
    except Exception as e:
        print(e)



convertAllInDirectory("/mnt/c/Users/tgsav/OneDrive/Desktop/pdf-to-excel/test/", "csv")    
#tabula.convert_into("/mnt/c/Users/Phanasorn/Desktop/PJ/test/MOCK_DATA_SEVERALPAGE.pdf", "output.csv", output_format="csv", pages='all')
