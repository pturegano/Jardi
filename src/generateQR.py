# Importing library
from mimetypes import init
from turtle import fillcolor
import qrcode
import csv
from PIL import Image as PILImage

myQRCode = qrcode.QRCode()

def initiQR():
    myQRCode = qrcode.QRCode(version=1,box_size=10,border=4)
    return myQRCode

def resize(img,formatFileName):
    im = PILImage.open(formatFileName)
    im = im.resize((100,100))
    #im.show()
    im.save(formatFileName)
    return img

def formatPath(fileName):
    path = "img\\"
    extension = ".png"
    formatFileName = path + fileName + extension
    return formatFileName

def generate(data, fileName):
    myQRCode = initiQR()
    formatFileName = formatPath(fileName)
    myQRCode.add_data(data)
    myQRCode.make(fit=True)
    img = myQRCode.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
    img.save(formatFileName)
    img= resize(img,formatFileName)
    
def run():
    with open("data\WikiPages.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            print(row)
            url = row[1]
            fileName = row[0]
            generate(url,fileName)

run()
