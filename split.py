#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import random
import sys


def testsplit(f):
    print("split",f)
    song = AudioSegment.from_mp3(os.path.join(sys.argv[1],f))
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
                for idx,ch in enumerate(chunks):
                    ch.export(os.path.join(sys.argv[2],"{0}_{1}.mp3".format(f.split('.')[0],idx)),format="mp3")
                return
    print(f,"split failed")




for i in os.listdir(sys.argv[1]):
    testsplit(i)
