from sqlite3.dbapi2 import Error
from PIL import Image, ImageDraw, ImageFont
import base64
import io
from modulos import db

def cearfoto(texto,numero,fecha):
    data = io.BytesIO()
    try:
        imagen = Image.open(f'static/images/temples/{numero}.jpg')
        db.guarda_luna(texto,numero)
        
        
    except Error as e:
        imagen = Image.open(f'static/images/temples/01000101 01101100 01101100 01101111 01110011 00100000 01110011 01100101 00100000 01100001 01110000 01110010 01101111 01111000 01101001 01101101 01100001 01101110.jpg')
        texto = ""
        fecha = ""
        print(e)
        
    tamanio = 80
    w = 0
    dibujar = ImageDraw.Draw(imagen)
    
    while (1):
        myfont = ImageFont.truetype("static/fonts/moon_get-Heavy.ttf",int(tamanio))
        w, h = dibujar.textsize(texto, font=myfont)
        
        if w <= 1920 or tamanio == 1:
            break;
        tamanio-=1
        
    dibujar.text(((1920-w)/2, 880), texto, font=myfont)
    
    myfont = ImageFont.truetype("static/fonts/Montserrat-Light.ttf",int(40))
    w, h = dibujar.textsize(fecha, font=myfont)
    dibujar.text(((1920-w-15), 1080-h-15), fecha, font=myfont)
    

    imagen.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    
    return encoded_img_data