'''
Short Script to generate Image Captchas used in human verification.
'''

import random
from captcha.image import ImageCaptcha
from PIL import Image

image=ImageCaptcha(height=200,width=400)

def generate_captcha(length=6):
    characters='abcdefghijklmnopqrstuvwxyz123456789'
    captcha_text=' '.join(random.choice(characters) for _ in range(length))
    return captcha_text


if __name__=="__main__":
    captcha_text=generate_captcha()
    data=image.generate(captcha_text)
    image.write(captcha_text,'CAPTCHA1.png')

    Image.open('CAPTCHA1.png')