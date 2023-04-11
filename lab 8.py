from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont


def z1(n):
    im=Image.open('23.jpg')
    #print(im.size)
    imcr=im.crop((0,160,471,600))
    imcr.save('crop 23.png')
    return ""
def z2(n):
    ot={"Новый год": 'ng.jpg',
        "День рождения": 'dr.jpg',
        "8 марта": '8.jpg',
        "23 февраля": '23.jpg'}
    print("К какому празнику вам нужна открытка? У нас есть такие:")
    for key in ot:
        print (key)
    n=input("Пожалуйста введите точно также как в списке без пробела в конце: ")
    im=Image.open(ot[n])
    im.show()
    return ""
def z3(n):
    im = Image.open('dr.jpg')
    n=input("Введите имя: ")
    draw = ImageDraw.Draw(im)
    draw.text((110, 100), n, (0, 0, 0))
    im.show()
    im.save('name dr.jpg')
    return ""
#z1(" ")
#z2(" ")
z3(" ")