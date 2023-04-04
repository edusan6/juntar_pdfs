import sys
import PyPDF2
from datetime import date, timedelta

def merge_pdfs(file_list, output_file):
    merger = PyPDF2.PdfMerger()

    for file in file_list:
        with open(file, 'rb') as f:
            merger.append(PyPDF2.PdfReader(f))

    with open(output_file, 'wb') as f:
        merger.write(f)

def generate_monthly_files(start_date, end_date):
    current_date = start_date
    file_list = []

    while current_date <= end_date:
        file_name = f"{current_date.year}-{current_date.month:02d}.pdf"
        file_path = f"C:\\Users\\edusa\\OneDrive\\Área de Trabalho\\Delta\\RECIBOS\\{file_name}"
        file_list.append(file_path)
        current_date += timedelta(days=32)
        current_date = current_date.replace(day=1)

    return file_list

if __name__ == '__main__':
    # Gerar lista de arquivos PDF para juntar
    start_date = date(2019, 12, 1)
    end_date = date(2023, 2, 1)
    pdf_files = generate_monthly_files(start_date, end_date)

    # Nome do arquivo de saída
    output_pdf = "C:\\Users\\edusa\\OneDrive\\Área de Trabalho\\Delta\\RECIBOS\\arquivos_juntos.pdf"

    # Juntar os arquivos PDF
    merge_pdfs(pdf_files, output_pdf)

    print("Arquivos PDF juntados com sucesso!")
