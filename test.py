import wave
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt

def template():
    # 讀取音檔
    wavefile = wave.open('test.wav', 'rb')

    fs = wavefile.getframerate()
    num_frame = wavefile.getnframes()

    #print('fs =', fs) # 44100
    #print('num of frame =', num_frame) # 230400

    # 讀取波形與數據
    str_data = wavefile.readframes(num_frame)
    wave_data = np.frombuffer(str_data, dtype=np.int16)
    wave_data = wave_data / max(abs(wave_data))
    n_channel = 2
    wave_data = np.reshape(wave_data, (num_frame, n_channel))
    #print(wave_data.shape) # (230400, 2)
    #print(wave_data)

    # 畫出音訊波形圖
    time = np.arange(0, num_frame) * 1 / fs
    #plt.plot(time, wave_data)
    #plt.show()
    #plt.close()

    # 播放聲音
    n_bytes = 2
    wave_data = (2**15-1) * wave_data
    wave_data = wave_data.astype(np.int16)
    #play_obj = sa.play_buffer(wave_data, n_channel, n_bytes, fs)
    #play_obj.wait_done()
    #print(wave_data.shape) # (230400, 2)
    #print(wave_data)

    # 製作音檔
    '''
    f = wave.open('test-copy.wav', 'wb')
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(fs)
    f.writeframes(wave_data.tobytes())
    f.close()
    '''

def test():
    score = [1, 1, 5, 5, 6, 6, 5]
    beat = [1, 1, 1, 1, 1, 1, 1]
    freq = [440.00, 493.88, 523.25, 587.31, 659.26, 739.99, 830.61]
    fs = 44100

    music = []
    for i in range(len(score)):
        t = np.linspace(0, beat[i], beat[i] * fs, False)
        note = np.sin(freq[score[i]-1] * t * 2 * np.pi)
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        audio[:2050] = 0
        audio[-2050:] = 0
        music.append(audio)

    music = np.array(music)

    play_obj = sa.play_buffer(music, 1, 2, fs)
    play_obj.wait_done()

if __name__ == '__main__':
    template()
    test()
