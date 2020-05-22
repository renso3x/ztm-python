import PyPDF2
#shortcut on opening a file
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('cv.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

# get all pages
for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('wt_file.pdf', 'wb') as file:
    output.write(file)