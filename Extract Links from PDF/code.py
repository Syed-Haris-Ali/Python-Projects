#Kindly install the following librarie

import pikepdf  

pdf_file = pikepdf.Pdf.open("pdf.pdf") # Your PDF File Here
urls = []

for page in pdf_file.pages:
    for annots in page.get("/Annots"):
        url = annots.get("/A").get("/ URI")
        if url is not None:
            print("[+] URL Found:", url)
            urls.append(url)
