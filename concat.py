#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import random
import sys

mp3list = []
charlist = []

def grandom():
    left = 8
    res = None
    cres = ""
    while left > 0:
        left -= 1
        pos = random.randint(0,len(mp3list)-1 )
        if res == None:
            res = mp3list[pos]
            #res = AudioSegment.from_mp3(mp3list[pos])
            cres += charlist[pos]
        else:
            res += mp3list[pos]
            #res += AudioSegment.from_mp3(mp3list[pos])
            cres += charlist[pos]
    return res, cres






def testsplit():
    song = grandom()

    # Split track where the silence is 2 seconds or more and get chunks using
    # the imported function.
    for sli_len in range(200,20,-10):
        for fenbei in range(-20,-50, -10):
            chunks = split_on_silence (
                # Use the loaded audio.
                song,
                # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
                min_silence_len = sli_len,
                # Consider a chunk silent if it's quieter than -16 dBFS.
                # (You may want to adjust this parameter.)
                silence_thresh = fenbei,
                keep_silence=100
            )
            if len(chunks) == 8:
                print(sli_len,fenbei)
                return

for idx,i in enumerate(os.listdir("convert")):
    if i % 500 == 0:
        print("load ",i)
    mp3list.append(AudioSegment.from_mp3("convert/"+i))
    #mp3list.append("convert/"+i)
    charlist.append(i[0])



for i in range(0,5000):
    if i % 500 == 0:
        print("generrate ",i)
    song,cres = grandom()
    song.export("{0}/{1}.mp3".format(sys.argv[1],cres),format="mp3")
