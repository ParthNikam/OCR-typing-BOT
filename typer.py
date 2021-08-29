import pyautogui, mouse, time, pytesseract
from PIL import Image


def process_image(iamge_name, lang_code):
    text = pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)
    text = text.split('\n')
    text = ' '.join(text)
    return text

def output_file(filename, data):
    data.replace("|", "I")
    data.replace("  ", " ")
    with open(filename, 'w') as f:
        f.write(data)


text = process_image("1.png", "eng")
print(text)
output_file("1.txt", text)

time.sleep(3)
pyautogui.write(text , interval=0.05) # change interval to change typing speeds
