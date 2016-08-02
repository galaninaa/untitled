import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

def format_time(x, pos=None):
    global duration, nframes, k
    progress = int(x / float(nframes) * duration * k)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out

def format_db(x, pos=None):
    if pos == 0:
        return ""
    global peak
    if x == 0:
        return "-inf"

    db = 20 * math.log10(abs(x) / float(peak))
    return int(db)

def count_channel(wav_file):
    wav = wave.open(wav_file, mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    print nchannels
    duration = nframes / framerate
    w, h = 800, 300
    k = nframes/w/32
    peak = 256 ** sampwidth / 2

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])


    for n in range(nchannels):
        channel = samples[n::nchannels]

        channel = channel[0::k]
    print "Not one channels:", max(channel),min(channel)

    for n in range(nchannels):
        channel = samples[n::nchannels]

        channel = channel[0::k]
        if nchannels == 1:
            channel = channel - peak
    print "For one channel:",max(channel),min(channel)