from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    fecha = datetime.date.today().strftime('%d de %B de %Y')
    recuerdos = [
        {"src": url_for('static', filename='img/5.jpeg'), "text": "Desde secundaria notaba que íbamos a ser grandes amigos, Gracias por estar ahí en los buenos y malos momentos, de verdad 💛"},
        {"src": url_for('static', filename='img/1.jpeg'), "text": "Aunque ahora estemos lejos, la amistad sigue igual de fuerte 🌍, cada vez que escucho 'Dapa', me acuerdo de ti y de todo lo que hemos vivido 🎵"},
        {"src": url_for('static', filename='img/2.jpeg'), "text": "Eres una de esas personas que se quedan en la vida, no importa el tiempo ni la distancia, gracias por ser como eres, por tu forma de escuchar, reír y acompañar 💬"},
        {"src": url_for('static', filename='img/3.jpeg'), "text": "Deseo que cumplas todos tus sueños y que la vida te devuelva todo lo bonito que das 🎂"},
        {"src": url_for('static', filename='img/4.jpeg'), "text": "Feliz cumpleaños, Jaris 🎉 gracias por ser mi mejor amiga y por tanto cariño siempre 💛"},
    ]
    musica_url = url_for('static', filename='music/camilo_dapa.mp3')
    return render_template('index.html', fecha=fecha, recuerdos=recuerdos, musica_url=musica_url)

if __name__ == '__main__':
    app.run(debug=True)

