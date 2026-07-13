import os
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF file and extracts all text from it.
    """
    text = ""
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        return "Error: File not found."

    try:
        reader = PdfReader(pdf_path)
        
        # Loop through pages
        for page in reader.pages:
            page_text = page.extract_text()
            text += page_text + " "
            
    except Exception as e:
        return f"Error reading PDF: {e}"
        
    return text

# IMPORTANT: This line below must be aligned to the FAR LEFT (no indentation)
if __name__=="__main__":
    # Make sure you have a file named test.pdf in data/pdfs/
    test_path = "data/pdfs/test.pdf"
    
    print(f"Attempting to read: {test_path}")
    content = extract_text_from_pdf(test_path)
    
    print(f"Extracted Text Preview:\n{content[:100]}...")
