import librosa
from pydub import AudioSegment
from pydub.playback import play

# Şarkıyı yükle
song = AudioSegment.from_file("C:/Users/ASUS/Desktop/yeni/gülpembe.mp3", format="mp3")


# Şarkıyı numpy dizisine dönüştür
audio_data = song.get_array_of_samples()
sample_rate = song.frame_rate

# Ses özelliklerini analiz et
chroma = librosa.feature.chroma_stft(y=audio_data, sr=sample_rate)
mfcc = librosa.feature.mfcc(y=audio_data, sr=sample_rate)

# Ses sentezleme
# (Bu örnekte sadece aynı şarkıyı çalacak şekilde düzenlendi)
reconstructed_audio = librosa.feature.inverse.mfcc_to_audio(mfcc)

# Sesi çal
play(AudioSegment(
    reconstructed_audio.astype(audio_data.dtype).tobytes(),
    frame_rate=sample_rate,
    channels=1,
    sample_width=audio_data.dtype.itemsize
))
