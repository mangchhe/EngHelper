import librosa
import os
import numpy as np
import matplotlib.pyplot as plt

#mp3 = r'C:\Users\mangc\Desktop\Test 4_Part2.mp3'

wav = r'C:\Users\mangc\Desktop\EngHelper\Audio\Test 4_Part2 (online-audio-converter.com).wav'

file_dir, file_id = os.path.split(wav)

print('file_dir : ', file_dir)
print('file_id : ', file_id)

m, s = map(int, input().split())
m2, s2 = map(int, input().split())

if m > 0:
    sSum = (m * 60) + s
else:
    sSum = s

if m2 > 0:
    sSum2 = (m2 * 60) + s2
else:
    sSum2 = s2

y, sr = librosa.load(wav)

start = (sSum/(len(y)/sr))*100
end = (sSum2/(len(y)/sr))*100

startLen = round(len(y) * (start / 100))
endLen = round(len(y) * (end / 100))

y = y[startLen:endLen]

time = np.linspace(0, len(y)/sr, len(y))

fig, ax1 = plt.subplots()
ax1.plot(time, y, color = 'b', label = 'speech waveform')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time [s]')
plt.title(file_id)
plt.savefig(file_id+'.png')
librosa.output.write_wav('half_file.wav',y,sr)
plt.show()