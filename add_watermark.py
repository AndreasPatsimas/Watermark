import PyPDF2

with open("super.pdf", mode="rb") as super_file:
    super_pdf = PyPDF2.PdfFileReader(super_file)
    with open("wtr.pdf", mode="rb") as watermark_file:
        watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
        watermark_page = watermark_pdf.getPage(0)
        output = PyPDF2.PdfFileWriter()
        for super_page in list(super_pdf.pages):
            super_page.mergePage(watermark_page)
            output.addPage(super_page)
        with open("wtr_super.pdf", mode="wb") as wtr_super_file:
            output.write(wtr_super_file)
