import PyPDF2
import sys

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'E:\Facultad\Ing Informatica\Desarrollo_2026_Verano\Programacion 3\TP MST\TRABAJO PRACTICO - mst.pdf'

with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    for i, page in enumerate(reader.pages):
        print(f'--- PAGE {i+1} ---')
        print(page.extract_text())
        print('\n')
