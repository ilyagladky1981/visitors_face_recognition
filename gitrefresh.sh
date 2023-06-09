#!/bin/bash
ver_id=`cat vid`

ver_id=$(expr $ver_id + 1)

echo $ver_id > vid

ver_id4=$[$ver_id % 10]
tmp_num=$(expr $ver_id - $ver_id4)
ver_id=$(expr $tmp_num / 10 )
ver_id3=$(expr $ver_id % 10 )
tmp_num=$(expr $ver_id - $ver_id3)
ver_id=$(expr $tmp_num / 10 )
ver_id2=$(expr $ver_id % 10)
tmp_num=$(expr $ver_id - $ver_id2)
ver_id=$(expr $tmp_num / 10 )
ver_id1=$(expr $ver_id % 10)

ver_id_str="$ver_id1"".""$ver_id2""$ver_id3""$ver_id4"

date && ( git add . ) && ( git commit -m "version num $ver_id_str" ) && ( git push -u origin main git@github.com:ilyagladky1981/visitors_face_recognition.git) 
