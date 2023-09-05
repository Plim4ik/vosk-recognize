import requests
from pydub import AudioSegment
import os
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize

def read_links():
    with open("links_to_transcribe.txt", "r") as f:
        links = f.readlines()
    return [link.strip() for link in links]

def write_result(link, transcribe_time, text):
    with open("results.txt", "a", encoding='utf-8') as f:
        f.write(f"Ссылка: {link}\nВремя расшифровки: {transcribe_time}\nТекст: {text}\n\n")


def download_and_convert_audio(url):
    r = requests.get(url)
    filename = url.split('/')[-1]
    filepath = os.path.join('downloads', filename)
    with open(filepath, 'wb') as f:
        f.write(r.content)

    # Конвертация аудио в формат WAV
    audio = AudioSegment.from_file(filepath)

    # Удаление шума (это простой пример, на практике может потребоваться более сложная обработка)
    audio = audio.low_pass_filter(3000)

    # Увеличение громкости
    audio = audio + 10

    # Нормализация аудио
    audio = normalize(audio)

    wav_filename = os.path.splitext(filepath)[0] + '.wav'
    audio.export(wav_filename, format="wav")

    return wav_filename
