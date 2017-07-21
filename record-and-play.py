"""PyAudio example: Record 5 seconds and play it immediately."""

import pyaudio
import wave
import time

CHUNK = 1024
FORMAT = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)


stream.start_stream()

start_time = stream.get_time()
while stream.is_active():
    if (stream.get_time()-start_time < RECORD_SECONDS):
        time.sleep(0.1)
    else:
        break

stream.stop_stream()
stream.close()

p.terminate()
