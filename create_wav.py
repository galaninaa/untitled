import speech_recognition as sr
import wave


def BigEar(wd):
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        audio = r.listen(source)
        #wd.find_element_by_name("Calls").click()
        print("WAV Voicemail wiil created")
        f= open(str(wd) +".wav", "wb")
        f.write(audio.get_wav_data())
        print("WAV Voicemail is created")

def LittleEar(wd):
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        audio = r.record(source,duration = 10)
        f= open(str(wd) +".wav", "wb")
        f.write(audio.get_wav_data())
        print("WAV Voicemail is created")

'''
LittleEar('/Users/galaninaa/PycharmProjects/untitled/ipod/Empty phone')

wav = wave.open("/Users/galaninaa/PycharmProjects/untitled/ipod/Empty Voicemail2.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
print (nchannels, sampwidth, framerate, nframes, comptype, compname)


wav = wave.open("/Users/galaninaa/PycharmProjects/untitled/ipod/Empty Voicemail.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
print (nchannels, sampwidth, framerate, nframes, comptype, compname)

'''