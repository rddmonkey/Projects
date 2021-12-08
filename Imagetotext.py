from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"Capture - Copy.PNG"

img = Image.open(image_path)

with Image.open(image_path) as im:
    im_top = im.crop((440, 120, 1070, 310))
    im_bot = im.crop((200,100,1070,350))

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(im_top)
text2 = pytesseract.image_to_string(image_path)

textlist = list(text2)
ans = ""


for i in range(len(textlist)):
    if textlist[i] == "\n":
        textlist[i] = " "
    if textlist[i].isalpha() or textlist[i].isspace:
        ans += textlist[i]

print(ans.strip())
