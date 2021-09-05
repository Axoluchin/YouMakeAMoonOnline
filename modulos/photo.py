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
        
    except:
        imagen = Image.open('static/images/Error.jpg')
        texto = ""
        fecha = ""
        
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