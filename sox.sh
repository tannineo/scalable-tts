#!/bin/bash

file=$1
input=$2
output=$3

echo $file

for fn in `cat ${file}`;do
	sox $input/$fn -n spectrogram -r -o $output/${fn}.png -x 256 -y 128
done

