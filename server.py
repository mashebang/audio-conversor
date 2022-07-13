from flask import Flask, request, send_file
from conversor import convert_audio
from os import path

app = Flask(__name__)

@app.get("/")
def index():
    return """
        <p>Hello, World!</p>
        <form action="/convert" method="POST" enctype="multipart/form-data">
            <h1>selecione o arquivo
            <fieldset>
                <label>arquivo</label>
                <input name="file" type="file" />
            </fieldset>
            <select name="audio-format">
                <option value="wav">WAV</option>
                <option value="mp3">MP3</option>
                <option value="ogg">OGG</option>
            </select>
            <button type="submit">Converter</button>
        </form>
    """

save_path = '/temp'

@app.route("/convert")
def convert():
    audio_format = request.form['audio-format']
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    exported_filename = convert_audio(filename, audio_format)
    return send_file(exported_filename, f'converted_{exported_filename}')