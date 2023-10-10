import os
#!pip install PyPDF2
from PyPDF2 import PdfReader, PdfMerger

# put the pdf files in the 'target' folder.
target = 'target'

merger = PdfMerger()

filelist = []
for filename in os.listdir(target):
    if filename.endswith(".pdf"):
        with open(os.path.join(target, filename), "rb") as f:
            filelist.append(filename)
            pdf_file = PdfReader(f)
            merger.append(pdf_file)
            f.close()

output_file = "merged_output.pdf"
with open(output_file, 'wb') as f:
    merger.write(f)
    f.close()

print(filelist)
print(f"All (of {len(filelist)}) pdf files in '{target}' folder were merged to {output_file}.")

