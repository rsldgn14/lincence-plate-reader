from pytesseract import pytesseract

plate_img =

plate_text = pytesseract.image_to_string(plate_img, lang='eng', config='--psm 13')