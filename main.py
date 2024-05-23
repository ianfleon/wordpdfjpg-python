from docx2pdf import convert
import pypdfium2 as pdfium
import os.path

# convert("input.docx")
# print(convert("surat.docx", "output.png"))
# convert("my_docx_folder/")

def docxToPdf(inputfile, outputfile):
	try:
		conv = convert(inputfile, outputfile)
		if conv == None:
			print("DONE DOCX TO PDF!")
		else:
			print("ERROR DOCX TO PDF")
	except:
		print("ERR!")
	

def pdfToJpg(inputfile, outputfile):
	pdf = pdfium.PdfDocument(inputfile)
	page = pdf.get_page(0)
	pil_image = page.render(scale = 300/72).to_pil()
	image_name = outputfile
	pil_image.save(image_name)

# Init File Name
docxFileName = "surat.docx"
pdfFileName = "file-dokumen.pdf";

docxToPdf(inputfile=docxFileName, outputfile=pdfFileName)

if os.path.isfile(pdfFileName):
	try:
		wwwa = pdfToJpg(inputfile=pdfFileName, outputfile="file-gambar.jpg")
		if wwwa == None:
			print ("DONE PDF TO IMG!")
		else:
			print("ERROR PDF TO IMG")
	except:
		print("PDF2IMG: ERROR!!!")
else:
	print("ERROR CONVERT!!!")