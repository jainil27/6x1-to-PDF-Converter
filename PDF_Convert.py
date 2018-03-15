from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if(len(sys.argv)==2):

    filename=sys.argv[1]
    print("\n\n\nConverting "+filename+" file into normal PDF....")
    with open(filename, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()

        numPages = input1.getNumPages()
        print ("\n\nDocument has %s pages." % numPages)

        for i in range(numPages):

            input1 = PdfFileReader(in_f)
            page1 = input1.getPage(i)
            page1.cropBox.lowerLeft = (63, 545)
            page1.cropBox.upperRight = (289, 715)        # 1
            output.addPage(page1)

            input1 = PdfFileReader(in_f)
            page2 = input1.getPage(i)
            page2.cropBox.lowerLeft = (63, 335)
            page2.cropBox.upperRight = (289, 507)        # 2
            output.addPage(page2)

            input1 = PdfFileReader(in_f)
            page3 = input1.getPage(i)
            page3.cropBox.lowerLeft = (63, 125)
            page3.cropBox.upperRight = (289, 300)       #3
            output.addPage(page3)

            input1 = PdfFileReader(in_f)
            page4 = input1.getPage(i)
            page4.cropBox.lowerLeft = (305, 545)
            page4.cropBox.upperRight = (532, 715)  # 4
            output.addPage(page4)

            input1 = PdfFileReader(in_f)
            page5 = input1.getPage(i)
            page5.cropBox.lowerLeft = (305, 334)
            page5.cropBox.upperRight = (532, 509)        # 5
            output.addPage(page5)

            input1 = PdfFileReader(in_f)
            page6 = input1.getPage(i)
            page6.cropBox.lowerLeft = (305, 125)
            page6.cropBox.upperRight = (532, 300)        # 6
            output.addPage(page6)

        newfilename=filename[:-13]+".pdf"
        with open(newfilename, "wb") as out_f:
            output.write(out_f)
        totalPages=6*numPages
        print("\n\n\nConversion Sucessful...\n\n\n New Filename : "+newfilename+"\n\n New Document has "+str(totalPages)+" Pages")

else:
    print("Invalid number of arguments, pl enter the filename.pdf as an argument")