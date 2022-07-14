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

@app.route("/convert", methods=['GET', 'POST'])
def convert():
    audio_format = request.form['audio-format']
    file = request.files['file']
    filename = file.filename
    print('>>>> filename', filename)
    file.save(path.join('.', filename))
    exported_filename = convert_audio(filename, audio_format)
    print('>>>> exported filename', exported_filename)

    return send_file(
        path_or_file=exported_filename,
        as_attachment=True,
        download_name=f'converted_{exported_filename}'
    )