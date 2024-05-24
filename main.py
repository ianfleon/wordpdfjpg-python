from docx2pdf import convert
import pypdfium2 as pdfium
import os

# Assign directory
sourceDocx = "dist"

# Check Dirs Exist
if os.path.isdir('result/pdf') != True:
	os.makedirs("result/pdf")

if os.path.isdir('result/jpg') != True:
	os.mkdir("result/jpg")

# print(os.getcwd())
# exit()

# Main Start Function
def runConverter(docxFile):

	print("DOCX2PDF: " + docxFile)

	# Get new name from docx file name
	newName = docxFile.split(".docx")[0]

	pdfFilePath = os.getcwd() + "/result/"

	docxToPdf(inputfile = docxFile, outputfile = pdfDir newName + ".pdf")

	exit()

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

def docxToPdf(inputfile, outputfile):
	try:
		conv = convert(inputfile, outputfile)
		if conv == None:
			print("DONE DOCX TO PDF!")
		else:
			print("ERROR DOCX TO PDF")
	except:
		print("ERR!")

# Iterate over files in directory
for name in os.listdir(sourceDocx):
	# print(name)
	runConverter(docxFile = sourceDocx + "/" + name)

# convert("input.docx")
# print(convert("surat.docx", "output.png"))
# convert("my_docx_folder/")

# def pdfToJpg(inputfile, outputfile):
	
# 	pdf = pdfium.PdfDocument(inputfile)
# 	page = pdf.get_page(0)
# 	pil_image = page.render(scale = 300/72).to_pil()
# 	image_name = outputfile
# 	pil_image.save(image_name)



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