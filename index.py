from sqlite3.dbapi2 import Error
from flask import Flask, render_template, url_for, request
from modulos.photo import cearfoto

from modulos import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", datos = db.ultimas_lunas(), total = db.Nlunas())
    

@app.route('/Luna',methods = ['POST']) 
def render_datafunction():
    
    if  request.method == 'POST':
        luna = request.form
        try:
            encoded_img_data = cearfoto(luna["Texto"],luna["Num"], luna["Fecha"])
            return render_template("Luna.html", img_data=encoded_img_data.decode('utf-8'), datos = db.ultimas_lunas(), total = db.Nlunas())
        except:
            return render_template("index.html", datos = db.ultimas_lunas(), total = db.Nlunas())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__": #! Quitar cuando se suba a produccion
    app.run(debug=True)
