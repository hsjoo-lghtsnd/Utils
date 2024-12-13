import os
import argparse
import importlib
import subprocess
import sys

'''
Writer: Hosung Joo (zxcqa123@postech.ac.kr)
2024. 12. 13
Version 1.0
'''


def check_pypdf2():
    try:
        # Check if PyPDF2 is installed and the correct version
        module = importlib.import_module("PyPDF2")
        if module.__version__ == "3.0.1":
            print("Running PyPDF2 3.0.1 ...")
        else:
            print(f"PyPDF2 version {module.__version__} is installed, but version 3.0.1 is required.")
            install_pypdf2()
    except ImportError:
        # PyPDF2 is not installed
        print("PyPDF2 is not installed.")
        install_pypdf2()

def install_pypdf2():
    user_input = input("PyPDF2 3.0.1 is not installed. Would you like to install it? (yes/no): ").strip().lower()
    if user_input in ["yes", "y"]:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2==3.0.1"])
            print("PyPDF2 3.0.1 has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print("An error occurred while trying to install PyPDF2 3.0.1:", e)
    else:
        print("Installation aborted. PyPDF2 3.0.1 is required for this script.")

def merge(target):
    
    filelist = []
    for filename in os.listdir(target):
        if filename.lower().endswith(".pdf"):
            filelist.append(filename)
    filelist.sort()
    
    if filelist:
        print(f"Combining files of {filelist}...")

        check_pypdf2()
        from PyPDF2 import PdfMerger, PdfReader
        merger = PdfMerger()
        
        for filename in filelist:
            with open(os.path.join(target, filename), "rb") as f:
                pdf_file = PdfReader(f)
                merger.append(pdf_file)
    
        output_file = target+".pdf"
        with open(output_file, 'wb') as f:
            merger.write(f)
        
        print(f"All (of {len(filelist)}) pdf files in '{target}' folder were merged to {output_file}.")
        
    else:
        print(f"there was no PDF file in \"{target}\" folder.")

def arg_parse():
    parser = argparse.ArgumentParser(prog='PDF merger v1.0 by Hosung Joo', usage='python ' + sys.argv[0] + ' -f folderName')
    parser.add_argument("-f", "--folder", dest="target", action="store", required=True, help='use -f \"folder name\" if it contains space.')
    args = parser.parse_args()
    if not args.target:
        parser.print_help()
    return args.target

def main():
    target = arg_parse()
    if target:
        merge(target)

if __name__ == '__main__':
    main()