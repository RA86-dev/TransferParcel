#############################
# Name: Audio Class I -  Uses external libs
# Description: NOTE: AUTO DOWNLOADS DATA
# CREATED and SENT PUBLIC: SATURDAY FEB 24, 2024
# UPDATE 2 - SUNDAY FEB 25 AT 9 AM
#
#############################
import os
print('Connection was received.')

## import data:
try:
    import soundfile as sf
    import librosa
    import matplotlib.pyplot as plt
    import numpy as np
    import pyaudio
    import wave
    from moviepy.editor import VideoFileClip, AudioFileClip
    import speech_recognition as sr
except ImportError:
    try:
        print('You have suffered an issue. We are installing missing libraries.')
        os.system('pip install numpy')
        os.system('pip install matplotlib')
        os.system('pip install pyaudio')
        os.system('pip install wave')
        os.system('pip install moviepy')
        os.system('pip install SpeechRecognition')

        os.system('pip install soundfile')
    except OSError as c:
        print('You have suffered an issue. We are installing missing libraries. Using PIP3')
        os.system
        os.system('pip3 install numpy')
        os.system('pip3 install matplotlib')
        os.system('pip3 install pyaudio')
        os.system('pip3 install wave')
        os.system('pip3 install moviepy')
        os.system('pip3 install SpeechRecognition')
        os.system('pip3 install soundfile')




        
    
#class_Data I - Audio CONFIG
class Audio:
    def normalize_audio(self,file_path):
        try:
            # Read audio file
            audio_data, sample_rate = sf.read(file_path)

            # Calculate normalization factor
            normalization_factor = np.max(np.abs(audio_data))

            # Normalize audio data
            normalized_audio = (audio_data / normalization_factor)

            # Write normalized audio back to file
            sf.write(file_path, normalized_audio, sample_rate)

            print(f"Normalized audio saved to {file_path}")
        except Exception as e:
            print(f"Error: {e}")
    def recognize_speech(self,audio):
        recognizer_class = sr.Recognizer()
        with sr.AudioFile(audio) as source:
            audio_data = recognizer_class.record(source=source)
        try:
            text = recognizer_class.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print('Could not understand audio. Please try again.')

        except Exception as c:
            print(f"Error: {c}")
    def mp3_to_mp4(mp3_file, mp4_file):
        audio = AudioFileClip(mp3_file)
        # Create a video clip with a black screen matching the audio duration
        video = audio.to_videofile(mp4_file, codec="libx264", fps=24, audio=False)

    def mp4_to_mp3(mp4_file, mp3_file):
        video = VideoFileClip(mp4_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)

    def mp3_to_wav(mp3_file, wav_file):
        audio = AudioFileClip(mp3_file)
        audio.write_audiofile(wav_file)

    def mp4_to_wav(mp4_file, wav_file):
        video = VideoFileClip(mp4_file)
        audio = video.audio
        audio.write_audiofile(wav_file)

    def wav_to_mp3(wav_file, mp3_file):
        audio = AudioFileClip(wav_file)
        audio.write_audiofile(mp3_file)

    def wav_to_mp4(wav_file, mp4_file):
        # Create a video clip with a black screen and the audio from the WAV file
        audio = AudioFileClip(wav_file)
        video = audio.to_videofile(mp4_file, codec="libx264", fps=24, audio=True)

    def recordData(self, time_in_seconds, output):
        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 44100
        seconds = time_in_seconds
        filename = output
        p = pyaudio.PyAudio()
        print('Recording..')
        stream = p.open(format=sample_format,
                        channels=channels,
                        frames_per_buffer=chunk,
                        rate=fs,
                        input=True)
        frames = []
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()
        print('Finished Recording.')
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

 
    def analyze_audio_file(self, file_path,printData=True,includeMatplotlib=True,returnData=True):
        print(f"Analyzing file: {file_path}")
        try:
            # Load audio file
            signal, sr = librosa.load(file_path)
            

            # Get duration
            duration = librosa.get_duration(y=signal, sr=sr)

            # Get file size
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # in MB

            # Get sample rate
            sample_rate = sr

            # Get number of channels
            num_channels = 1 if len(signal.shape) == 1 else signal.shape[0]

            # Get peak amplitude
            peak_amplitude = max(abs(signal))

            # Calculate RMS energy
            rms_energy = librosa.feature.rms(y=signal)[0][0]

            # Calculate spectral centroid
            spectral_centroid = librosa.feature.spectral_centroid(y=signal, sr=sr)[0][0]

            # Calculate zero crossing rate
            zero_crossing_rate = librosa.feature.zero_crossing_rate(signal)[0][0]

            # Calculate spectral bandwidth
            spectral_bandwidth = librosa.feature.spectral_bandwidth(y=signal, sr=sr)[0][0]

            # Compute chroma variant CENS
            chroma_cens = librosa.feature.chroma_cens(y=signal, sr=sr)

            # Compute constant-Q chromagram
            chroma_cqt = librosa.feature.chroma_cqt(y=signal, sr=sr)

            # Compute MFCCs
            mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)

            # Compute spectral contrast
            spectral_contrast = librosa.feature.spectral_contrast(y=signal, sr=sr)

            # Compute tempogram
            onset_env = librosa.onset.onset_strength(y=signal, sr=sr)
            tempogram = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr)

            # Compute spectral rolloff
            spectral_rolloff = librosa.feature.spectral_rolloff(y=signal, sr=sr)
            if printData == True:
                print(f"Duration: {duration:.2f} seconds")
                print(f"Sample rate: {sample_rate} Hz")
                print(f"Number of channels: {num_channels}")
                print(f"Peak amplitude: {peak_amplitude:.2f}")
                print(f"RMS energy: {rms_energy:.2f}")
                print(f"Spectral centroid: {spectral_centroid:.2f}")
                print(f"Zero crossing rate: {zero_crossing_rate:.2f}")
                print(f"Spectral bandwidth: {spectral_bandwidth:.2f}")
                print(f"File size: {file_size:.2f} MB")

                # Print shapes of computed features
                print(f"Chroma CENS shape: {chroma_cens.shape}")
                print(f"Chroma CQT shape: {chroma_cqt.shape}")
                print(f"MFCCs shape: {mfccs.shape}")
                print(f"Spectral Contrast shape: {spectral_contrast.shape}")
                print(f"Tempogram shape: {tempogram.shape}")
                print(f"Spectral Rolloff shape: {spectral_rolloff.shape}")
            

            if includeMatplotlib == True:
                # Plot Chroma CENS
                plt.figure(figsize=(14, 5))
                plt.plot(np.linspace(0, len(signal) / sr, num=len(signal)), signal)
                plt.xlabel("Time (s)")
                plt.ylabel("Amplitude")
                plt.title("Waveform")
                plt.show()
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(chroma_cens, y_axis='chroma', x_axis='time')
                plt.colorbar()
                plt.title('Chroma CENS')
                plt.tight_layout()
                plt.show()

                 # Plot Chroma CQT
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(chroma_cqt, y_axis='chroma', x_axis='time')
                plt.colorbar()
                plt.title('Chroma CQT')
                plt.tight_layout()
                plt.show()

                    # Plot MFCCs
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(mfccs, x_axis='time')
                plt.colorbar()
                plt.title('MFCCs')
                plt.tight_layout()
                plt.show()

                # Plot Spectral Contrast
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(spectral_contrast, x_axis='time')
                plt.colorbar()
                plt.title('Spectral Contrast')
                plt.tight_layout()
                plt.show()

                # Plot Tempogram
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(tempogram, x_axis='time')
                plt.colorbar()
                plt.title('Tempogram')
                plt.tight_layout()
                plt.show()

                # Plot Spectral Rolloff
                plt.figure(figsize=(10, 4))
                plt.plot(np.linspace(0, len(spectral_rolloff) / sr, num=len(spectral_rolloff)), spectral_rolloff)

                plt.xlabel("Time (s)")
                plt.ylabel("Frequency (Hz)")
                plt.title("Spectral Rolloff")
                plt.tight_layout()
                plt.show()

            json_data = {
                "duration": duration,
                "sample_rate": sample_rate,
                'channel_num': num_channels,
                'peak_amplitude': peak_amplitude,
                'rms_energy': rms_energy,
                'spectral_centroid': spectral_centroid,
                'zero_crossing_rate': zero_crossing_rate,
                'spectral_bandwidth': spectral_bandwidth,
                'file_size': file_size,
                'chroma_cens': chroma_cens.tolist(),
                'chroma_cqt': chroma_cqt.tolist(),
                'mfccs': mfccs.tolist(),
                'spectral_contrast': spectral_contrast.tolist(),
                'tempogram': tempogram.tolist(),

            }
            if returnData == True:
                return json_data
            else:
                return
        except Exception as c:
            print(f'ERROR {c}') 
