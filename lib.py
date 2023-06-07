# import tabula
# import pandas as pd

# def convertAllInDirectory(dir, format):
#     try:
#         tabula.convert_into_by_batch(dir, output_format=format, pages='all')
#     except Exception as e:
#         print(e)

# def convertFileIntoSeparate(dir, format):
#     try:
#         tabula.convert_into_by_batch(dir, output_format=format, pages='all')
#     except Exception as e:
#         print(e)



# # convertAllInDirectory("/mnt/c/Users/Phanasorn/Desktop/PJ/test", "csv")    
# tabula.convert_into("/mnt/c/Users/Phanasorn/Desktop/PJ/test/MOCK_DATA_SEVERALPAGE.pdf", "output.csv", output_format="csv", pages='all')

import aspose.pdf as ap

input_pdf =  "mnt/c/Users/Phanasorn/Desktop/PJ/test/Pre-Freshy_2022.pdf"
output_pdf = "convert_pdf_to_xlsx.xlsx"
    # Open PDF document
print("WASD")
document = ap.Document(input_pdf)

save_option = ap.ExcelSaveOptions()

    # Save the file into MS Excel format
document.save(output_pdf, save_option)


