from docx2pdf import convert
import pypdfium2 as pdfium
import os

# Assign directory
directory = "dist"

# Check Dirs Exist
if os.path.isdir('result/pdf') != True:
	os.makedirs("result/pdf")

if os.path.isdir('result/jpg') != True:
	os.mkdir("result/jpg")

exit()

# Iterate over files in directory
for name in os.listdir(directory):
	print(name)

# exit()

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

def runConverter(docxFile, pdfFile):

	# Get new name from docx file name
	newName = docxFile.split(".docx")[0]

	docxToPdf(inputfile = docxFile, outputfile = newName + ".pdf")

	if os.path.isfile(pdfFileName):
		try:
			cpdf = pdfToJpg(inputfile=pdfFileName, outputfile="result/" + newName + ".jpg")
			if cpdf == None:
				print ("DONE PDF TO IMG!")
			else:
				print("ERROR PDF TO IMG")
		except:
			print("PDF2IMG: ERROR!!!")
	else:
		print("ERROR CONVERT!!!")

# Init File Name
# docxFileName = "surat.docx"
# pdfFileName = "file-dokumen.pdf"

# docxToPdf(inputfile=docxFileName, outputfile=pdfFileName)

# if os.path.isfile(pdfFileName):
# 	try:
# 		wwwa = pdfToJpg(inputfile=pdfFileName, outputfile="file-gambar.jpg")
# 		if wwwa == None:
# 			print ("DONE PDF TO IMG!")
# 		else:
# 			print("ERROR PDF TO IMG")
# 	except:
# 		print("PDF2IMG: ERROR!!!")
# else:
# 	print("ERROR CONVERT!!!")