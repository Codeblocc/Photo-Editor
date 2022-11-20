import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import os

path = './Images'
pathOut = '/editedImages'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
