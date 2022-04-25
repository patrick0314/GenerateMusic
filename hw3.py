import math
import wave
import numpy as np
import simpleaudio as sa

def getmusic(score, beat, name, key, fs, unit_beat):
    # Semitone p = 69 + 12*log(2, f/f0)
    p = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, \
            77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96]

    # Base Frequency of Each Tone
    # f = f0 * 2^((p-69)/12)
    freq = [440.00, 493.88, 523.25, 587.31, 659.26, 739.99, 830.61]

    # Generation Music
    music = []
    for i in range(len(score)):
        time = np.arange(0, beat[i] * unit_beat, fs * beat[i] * unit_beat)
        f = freq[key] * pow(2, ((p[score[i]]-69) / 12))
        x = np.sin(2 * np.pi * f * time)
        music.append(x)

    # Play Music
    play_obj = sa.play_buffer(music, 1, 2, fs)
    play_obj.wait_done()
    return

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
    getmusic(score, beat, name, 0, 100, 1)