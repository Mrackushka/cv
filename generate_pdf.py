import pdfkit

github_pages_url = "https://mrackushka.github.io/cv/print"
output_pdf_path = "generated-pdf.pdf"

pdfkit.from_url(github_pages_url, output_pdf_path)
