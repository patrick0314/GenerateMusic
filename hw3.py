import math
import wave
import numpy as np
import simpleaudio as sa

def getmusic(score, beat, name, key=0, unit_beat=1, fs=44100):
    # Semitone p = 69 + 12*log(2, f/f0)
    p = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, \
            77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96]

    # Base Frequency of Each Tone
    # f = f0 * 2^((p-69)/12)
    freq = [440.00, 493.88, 523.25, 587.31, 659.26, 739.99, 830.61]

    # Generation Music
    music = []
    for i in range(len(score)):
        if beat[i] > 1:
            for b in range(beat[i]):
                t = np.linspace(0, 1, 1 * fs, False)
                note = np.sin(freq[score[i]-1] * t * 2 * np.pi)
                audio = note * (2**15 - 1) / np.max(np.abs(note))
                audio = audio.astype(np.int16)
                if b == 0: audio[:2050] = 0
                elif b == beat[i]-1: audio[-4010:] = 0
                music.append(audio)
        else:
            t = np.linspace(0, 1, fs, False)
            note = np.sin(freq[score[i]-1] * t * 2 * np.pi)
            audio = note * (2**15 - 1) / np.max(np.abs(note))
            audio = audio.astype(np.int16)
            audio[:2050] = 0
            audio[-2050:] = 0
            music.append(audio)

    music = np.array(music)

    play_obj = sa.play_buffer(music, 1, 2, fs)
    play_obj.wait_done()

    f = wave.open(name+'.wav', 'wb')
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(fs)
    f.writeframes(music.tobytes())
    f.close()

if __name__ == '__main__':
    # =========================================================================
    # Basic Function:
    #   score = [1, 1, 5, 5, 6, 6, 5] # 1:Do, 2:Re, 3:Mi ...
    #   beat = [1, 1, 1, 1, 1, 1, 2] # 拍子
    #   name = 'twinkle'
    #   getmusic(score, beat, name) # Generate the music file 'twinkle.wav'
    # =========================================================================

    score = [1, 1, 5, 5, 6, 6, 5]
    beat = [1, 1, 1, 1, 1, 1, 2]
    name = 'twinkle'
    getmusic(score, beat, name)