import pyaudio
import wave


class RecordAudio:

    def __init__(self, length=5, fileName="recording.wav"):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = length
        self.audio = pyaudio.PyAudio()
        self.FILENAME = fileName

    def record(self,):
        self.stream = audio.open(format=FORMAT, channels=CHANNELS,
                                 rate=RATE, input=True,
                                 frames_per_buffer=CHUNK)
        print("recording audio for next ", self.RECORD_SECONDS, " ...")
        frames = list()

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.saveWav(frames)

    def saveWav(self, frames):
        waveFile = wave.open(self.FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
