import speech_recognition as sr
sr.__version__
r = sr.Recognizer()
male = sr.AudioFile('/home/rho/Downloads/male.wav')
with male as source:
    audio = r.record(source)
type(audio)
#r.recognize_google(audio)
print(r.recognize_google(audio))