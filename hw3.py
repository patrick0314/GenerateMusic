import time
import wave
import argparse
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt

def fading(X, order):
    n = int(0.05 * len(X))
    factor = np.linspace(0, 1, n) if order == 1 else np.linspace(1, 0, n)
    if order == 1: X[:n] *= factor
    else: X[-n:] *= factor
    return X

def getmusic(score, beat, name, key, unit_beat, volume, play):
    # Base Frequency of Each Tone
    fs = 44100
    basis = np.array([261.63, 261.63*2**(1/6), 261.63*2**(1/3), 261.63*2**(5/12) \
                , 261.63*2**(7/12), 261.63*2**(3/4), 261.63*2**(11/12), 261.63*2])
    keys = [1, 2**(1/6), 2**(1/3), 2**(5/12), 2**(7/12), 2**(3/4), 2**(11/12), 2]

    # Generation Music
    music = []
    basis = basis * keys[key-1]
    for i in range(len(score)):
        if beat[i] > 1:
            for b in range(beat[i]):
                t = np.linspace(0, unit_beat, unit_beat * fs, False)
                f = basis[score[i]-1]
                note = np.sin(f * t * 2 * np.pi)
                audio = volume * 0.5 * note * (2**15 - 1) / np.max(np.abs(note))
                if b == 0: fading(audio, 1)
                elif b == beat[i]-1: fading(audio, 0)
                music.append(audio.astype(np.int16))
        else:
            t = np.linspace(0, unit_beat, unit_beat * fs, False)
            f = basis[score[i]-1]
            note = np.sin(f * t * 2 * np.pi)
            audio = volume * 0.5 * note * (2**15 - 1) / np.max(np.abs(note))
            fading(audio, 1)
            fading(audio, 0)
            music.append(audio.astype(np.int16))

    music = np.array(music)
    music = np.reshape(music, (music.shape[0]*music.shape[1], ))

    '''
    '''
    # Sketch Plot
    time = np.arange(0, len(music)) * 1 / fs
    plt.plot(time, music)
    plt.show()
    plt.close()

    # Play Music
    if play:
        print('=== Play Music ===')
        play_obj = sa.play_buffer(music, 1, 2, fs)
        play_obj.wait_done()
        print('=== Play Done ===')

    # Save
    if name:
        f = wave.open(name+'.wav', 'wb')
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(fs)
        f.writeframes(music.tobytes())
        f.close()
        print('=== Save {}.wav file ==='.format(name))

if __name__ == '__main__':
    # =========================================================================
    # Basic Function:
    #   score = [1, 1, 5, 5, 6, 6, 5] # 1:Do, 2:Re, 3:Mi ...
    #   beat = [1, 1, 1, 1, 1, 1, 2] # 拍子
    #   name = 'twinkle'
    #   getmusic(score, beat, name) # Generate the music file 'twinkle.wav'
    # =========================================================================

    # Data Argumentation
    parser = argparse.ArgumentParser()
    parser.add_argument('--score', help='Enter the notion of the music.\n In C major, 1:Do 2:Re 3:Mi ...')
    parser.add_argument('--beat', help='Enter the beat in the music')
    parser.add_argument('--name', help='Enter the name of the file of the music')
    parser.add_argument('--key', help='Enter the major of the music and will affect the score represenetation.\n \
        (1, 2, 3, 4, 5, 6, 7, 8) = (C, D, E, F, G, A, B, C)')
    parser.add_argument('--unit_beat', help='Enter the sec per beat.')
    parser.add_argument('--volume', help='Enter the factor of the basic volume. Range is from 0 to 2')
    parser.add_argument('--play', help='Determine whether play the music while executing the program. 1 for playing')
    args = parser.parse_args()

    # Fool Proof
    if (not args.score or not args.beat) or len(args.score) != len(args.beat):
        print('ERROR !!! Something wrong with score or beat !!!')
    elif args.volume and (float(args.volume) > 2 or float(args.volume) < 0):
        print('ERROR !!! Something wrong with volume')
    else:
        # Data initialization
        score = list(map(int, list(args.score)))
        beat = list(map(int, list(args.beat)))
        name = args.name
        key = int(args.key) if args.key else 1
        unit_beat = int(args.unit_beat) if args.unit_beat else 1
        volume = float(args.volume) if args.volume else 1
        play = 1 if args.play == '1' else 0
        
        getmusic(score, beat, name, key=key, unit_beat=unit_beat, volume=volume, play=play)