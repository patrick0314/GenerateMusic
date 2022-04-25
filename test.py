import wave
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt

# 讀取音檔
wavefile = wave.open('test.wav', 'rb')

fs = wavefile.getframerate()
num_frame = wavefile.getnframes()

print('fs =', fs)
print('num of frame =', num_frame)

# 讀取波形與數據
str_data = wavefile.readframes(num_frame)
wave_data = np.frombuffer(str_data, dtype=np.int16)
wave_data = wave_data / max(abs(wave_data))
n_channel = 2
wave_data = np.reshape(wave_data, (num_frame, n_channel))

# 畫出音訊波形圖
time = np.arange(0, num_frame) * 1 / fs
plt.plot(time, wave_data)
plt.show()
plt.close()

# 播放聲音
n_bytes = 2
wave_data = (2**15-1) * wave_data
wave_data = wave_data.astype(np.int16)
play_obj = sa.play_buffer(wave_data, n_channel, n_bytes, fs)
play_obj.wait_done()

# 製作音檔
f = wave.open('test-copy.wav', 'wb')
f.setnchannels(2)
f.setsampwidth(2)
f.setframerate(fs)
f.writeframes(wave_data.tobytes)
f.close()