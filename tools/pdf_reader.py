import PyPDF2

def read_pdf(file_path):
    pdf_reader = PyPDF2.PdfReader(file_path)
    
    pdf_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text