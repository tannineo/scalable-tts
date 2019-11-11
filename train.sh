#!/bin/bash

virtualenv venv


. venv/bin/activate
pip install -r requirement.txt

tar -zxf audio.tar.gz

echo "train_audio"

mkdir train_audio

for i in seq `seq 1 15`;do
    python concat.py train_audio &
done

wait

echo "valid_audio"

mkdir valid_audio

for i in seq `seq 1 3`;do
    python concat.py valid_audio &
done

wait

echo "sox for train image"

ls train_audio > trainlist

mkdir train_image

split -l 2000 trainlist tsp

for spfile in `ls tsp*`;do
    sh sox.sh $spfile train_audio train_image &
done

wait

rm -f tsp*

echo "sox for valid image"

ls valid_audio > validlist

mkdir valid_image

split -l 2000 validlist validsp

for spfile in `ls validsp*`;do
    sh sox.sh $spfile valid_audio valid_image &
done

wait

rm -f validsp*

python pic_train.py --width 128 --height 64 --length 8 --symbols symbols.txt --batch-size 4 --epochs 6 --output-model audiomultts --train-dataset train_image --validate-dataset valid_image


tar -czvf modeltts.tar.gz audiomultts*

echo "model file is:modeltts.tar.tz"
