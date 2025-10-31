from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    fecha = datetime.date.today().strftime('%d de %B de %Y')
    musica_url = url_for('static', filename='music/camilo_dapa.mp3')
    imagenes = [
        {"src": url_for('static', filename='img/1.jpeg'), "texto": "Los recuerdos más lindos no se olvidan ✨"},
        {"src": url_for('static', filename='img/2.jpeg'), "texto": "Cada sonrisa tuya vale oro 💖"},
        {"src": url_for('static', filename='img/3.jpeg'), "texto": "Por más momentos juntos 🌸"},
        {"src": url_for('static', filename='img/4.jpeg'), "texto": "Eres una persona increíble 💫"},
    ]
    return render_template('index.html', fecha=fecha, musica_url=musica_url, imagenes=imagenes)

if __name__ == '__main__':
    app.run(debug=True)
