from pydub import AudioSegment
from os import path


def convert_audio(filename, outputFormat):
    audio = AudioSegment.from_wav(path.join('/tmp', filename))
    raw_name = filename
    if '.' in filename:
        # gets filename without file extension
        raw_name = ''.join(filename.split('.')[:-1])
    
    output_name = f"{raw_name}.{outputFormat}"
    print(f'convert {filename} to {outputFormat} as {output_name}')

    try:
        audio.export(output_name, format=outputFormat)
    except:
        print('error on exporting')

    return output_name

# unit test for poor projects
if __name__ == "__main__":
    convert_audio("Track11.m4a", "bora", "wav")
    # add assert