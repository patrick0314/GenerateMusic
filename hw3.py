import time
import wave
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt

def getmusic(score, beat, name, key=1, unit_beat=1, volume=1):
    # Base Frequency of Each Tone
    fs = 96000
    basis = [261.63, 261.63*2**(1/6), 261.63*2**(1/3), 261.63*2**(5/12) \
                , 261.63*2**(7/12), 261.63*2**(3/4), 261.63*2**(11/12)]
    freq_dif = {-1:2**(-1), -2:2**(-5/6), -3:2**(-2/3), -4:2**(-7/12), -5:2**(-5/12), -6:2**(-1/4), -7:2**(-1/12), \
                1:2**(0), 2:2**(1/6), 3:2**(1/3), 4:2**(5/12), 5:2**(7/12), 6:2**(3/4), 7:2**(11/12), \
                8:2**(1), 9:2**(7/6), 10:2**(4/3), 11:2**(17/12), 12:2**(19/12), 13:2**(7/4), 14:2**(23/12) }

    # Generation Music
    music = []
    for i in range(len(score)):
        if beat[i] > 1:
            for b in range(beat[i]):
                t = np.linspace(0, unit_beat, unit_beat * fs, False)
                f = basis[key-1] * freq_dif[score[i]]
                note = np.sin(f * t * 2 * np.pi)
                audio = volume * 0.5 * note * (2**15 - 1) / np.max(np.abs(note))
                audio = audio.astype(np.int16)
                if b == 0: audio[:2050] = 0
                elif b == beat[i]-1: audio[-2050:] = 0
                music.append(audio)
        else:
            t = np.linspace(0, unit_beat, unit_beat * fs, False)
            f = basis[key-1] * freq_dif[score[i]]
            note = np.sin(f * t * 2 * np.pi)
            audio = volume * 0.5 * note * (2**15 - 1) / np.max(np.abs(note))
            audio = audio.astype(np.int16)
            audio[:2050] = 0
            audio[-2050:] = 0
            music.append(audio)

    music = np.array(music)

    '''
    # Sketch Plot
    tmp = np.reshape(music, (music.shape[0]*music.shape[1], ))
    time = np.arange(0, len(tmp)) # * 1 / fs
    plt.plot(time, tmp)
    plt.show()
    plt.close()
    '''

    '''
    # Play Music
    play_obj = sa.play_buffer(music, 1, 2, fs)
    play_obj.wait_done()
    '''

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

    print('\n =========================================================================')
    print(' Basic Function:')
    print('   score = [1, 1, 5, 5, 6, 6, 5] # 1:Do, 2:Re, 3:Mi ...')
    print('   beat = [1, 1, 1, 1, 1, 1, 2] # 拍子')
    print('   name = \'twinkle\'')
    print('   getmusic(score, beat, name) # Generate the music file \'twinkle.wav\'')
    print(' Advanced Function:')
    print('   score -1:低音Do, -2:低音Re, -3:低音Mi, ..., 8:高音Do, 9:高音Re, 10:高音Mi, ... 包含上下八度音')
    print('   key = [1, 2, 3, 4, 5, 6, 7] # 1:C major, 2:D major, 3:E major 更改 key 的話，score 對應的音調也會改變')
    print('   unit beat 為每拍的單位時間')
    print('   volume = 0 ~ 2, 可以調整音樂大小聲')
    print(' =========================================================================\n')
    
    score = list(map(int, list(input('Enter the notion: '))))
    beat = list(map(int, list(input('Enter the beats: '))))
    if len(score) != len(beat):
        print('ERROR !!!')
    name = input('Enter the file name: ')
    key = input('Enter wanted key: ')
    if key == '': key = 1
    else: key = int(key)
    unit_beat = input('Enter wanted unit_beat: ')
    if unit_beat == '': unit_beat = 1
    else: unit_beat = int(unit_beat)
    volume = input('Enter wanted volume: ')
    if volume == '': volume = 1
    else: volume = int(volume)
    getmusic(score, beat, name, key, unit_beat, volume)