#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import random
import sys

mp3list = []

def grandom():
    left = 8
    res = None
    while left > 0:
        left -= 1
        if res == None:
            res = AudioSegment.from_mp3(mp3list[random.randint(0,len(mp3list))])
        else:
            res += AudioSegment.from_mp3(mp3list[random.randint(0,len(mp3list))])
    return res
            


for idx,i in enumerate(os.listdir("convert")):
    print(idx)
    #AudioSegment.from_mp3("convert/"+i)
    mp3list.append("convert/"+i)




def testsplit():
    song = grandom()
    
    # Split track where the silence is 2 seconds or more and get chunks using 
    # the imported function.
    for sli_len in range(20,80,10):
        for fenbei in range(-50,-20, 10):
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
    

for i in range(0,2000):
    testsplit()
    #print(len(chunks))
    #if len(chunks) != 8:
    #    song.export("file.mp3", format="mp3")
    #    for i, chunk in enumerate(chunks):
    #        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    #    
    #        # Add the padding chunk to beginning and end of the entire chunk.
    #        audio_chunk =  chunk 
    #    
    #        # Normalize the entire chunk.
    #        normalized_chunk = chunk
    #    
    #        # Export the audio chunk with new bitrate.
    #        print("Exporting chunk{0}.mp3.".format(i))
    #        normalized_chunk.export(
    #            "./chunk{0}.mp3".format(i),
    #            bitrate = "192k",
    #            format = "mp3"
    #        )
    #    sys.exit(1)
    
#sound = AudioSegment.from_mp3("/path/to/file.mp3")
#
## len() and slicing are in milliseconds
#halfway_point = len(sound) / 2
#second_half = sound[halfway_point:]
#
## Concatenation is just adding
#second_half_3_times = second_half + second_half + second_half
#
## writing mp3 files is a one liner
