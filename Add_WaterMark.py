import PyPDF2

#Load the file where you want to add the watermark too
template= PyPDF2.PdfFileReader(open('PDF_File.pdf','rb'))

#Load the Water Mark pdf file
waterMark=PyPDF2.PdfFileReader(open('WaterMark_File.pdf','rb'))

# Variable to output our Water MArked File
output = PyPDF2.PdfFileWriter()

# Loop to open all pages of our PDFs files pages and  add watermark in each page

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(waterMark.getPage(0))
    output.addPage(page)
    
    # Creating WaterMarked Output Files which have watermark to it.
    
    with open('waterMarked_Output.pdf','wb') as file:
        output.write(file)
