# import module
from pdf2image import convert_from_path
from pypdf import PdfReader
from getAns import getAns
import fitz
# creating a pdf reader object
def createQuestionsImg(path):
    reader = PdfReader(path)

    # printing number of pages in pdf file
    print(len(reader.pages))

    import fitz
    pgno = 1
    sub = 'ch'

    pdf = fitz.open(path)

    for pgno in range(1,len(reader.pages)-1):
        page = pdf[pgno]

        # getting a specific page from the pdf file
        starting_page = 1


        # Store Pdf with convert_from_path function
        images = convert_from_path('example2.pdf')

            # Save pages as images in the pdf
        text = page.get_text("text").split()
        if 'Section' in text:
            i = 180
        else:
            print("heeee")
            i = 100
        if i == 180:
            rect = fitz.Rect(0,50,50,2000)
        else:
            rect = fitz.Rect(0, 40, 50, 2000)

        qs_nums = page.get_text("text",clip = rect).split()
        print(qs_nums)
        if 'PHYSICS' in text:
            sub = 'ph'
        elif 'MATHEMATICS' in text:
            sub = 'ma'

        x =[]
        im = images[pgno]

        while i < 2339:
            for ii in range(105,125):
                if im.getpixel((ii,i))[0] < 50:
                    x.append(i)
                    i = i+20
                    break
            i = i+1
        x.append(x[-1] + 300)
        print(x)

        i = 0
        while i <= len(qs_nums)-1:
            img = im.crop((0,x[i]-15,1654,x[i+1]))
            img.save(sub + str(qs_nums[i]) + ".jpg")
            i = i+1

#im.crop((0,0,120,1410)).show()


