from vosk import Model, KaldiRecognizer
import wave
import json
from datetime import datetime

def transcribe_audio(filename):
    start_time = datetime.now()

    model = Model("vosk-model-small-ru")
    rec = KaldiRecognizer(model, 16000)

    wf = wave.open(filename, "rb")
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    end_time = datetime.now()
    transcribe_time = end_time - start_time

    result = json.loads(rec.FinalResult())
    return str(transcribe_time), result['text']
