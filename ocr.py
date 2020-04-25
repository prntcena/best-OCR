import pytesseract
import sys
from PIL import ImageFilter
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'  //specify the path of your tesseract engine



def prepare_image(img):
    """Transform image to greyscale and blur it"""
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != img.mode:
        img = img.convert('L')
    return img

def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img

def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return (255)


pass_factor = 40            //try changing this if you do not get the best results
def im_to_str(image):
    img = image
    img = prepare_image(img)
    img = remove_noise(img, pass_factor)
    return pytesseract.image_to_string(img)
    
    
  /////////////////////////////////////////calling the function////////////////////////////////////
  
  im_to_str(Image.open('img.jpg'))             //specify the path of image you want to get string of
