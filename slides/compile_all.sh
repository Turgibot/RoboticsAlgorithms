#!/bin/sh
echo Compiling all manim animation and uploading to website

manim lesson0.py Intro1
manim lesson0.py Intro2
manim lesson0.py Admin
manim lesson0.py Book
manim lesson0.py HowTo
manim lesson0.py Overview


manim lesson1.py Chap2_00
manim lesson1.py Chap2_01
manim lesson1.py Chap2_02
manim lesson1.py Chap2_03
#2.1
manim lesson1.py Chap2_10
manim lesson1.py Chap2_11
manim lesson1.py Chap2_12
manim lesson1.py Chap2_13
manim lesson1.py Chap2_14
manim lesson1.py Chap2_15
manim lesson1.py Chap2_16
manim lesson1.py Chap2_17

#2.2
manim lesson1.py Chap2_20
manim lesson1.py Chap2_21
manim lesson1.py Chap2_22
manim lesson1.py Chap2_23
manim lesson1.py Chap2_24
manim lesson1.py Chap2_25
manim lesson1.py Chap2_26
manim lesson1.py Chap2_27
manim lesson1.py Chap2_28
manim lesson1.py Chap2_29
manim lesson1.py Chap2_210
manim lesson1.py Chap2_211
manim lesson1.py Chap2_212
manim lesson1.py Chap2_213

#2.3
manim lesson1.py Chap2_30
manim lesson1.py Chap2_31
manim lesson1.py Chap2_32
manim lesson1.py Chap2_33
manim lesson1.py Chap2_34
manim lesson1.py Chap2_35
manim lesson1.py Chap2_36
manim lesson1.py Chap2_37
manim lesson1.py Chap2_38
manim lesson1.py Chap2_39

#2.4


manim lesson1.py Chap2_40
manim lesson1.py Chap2_41
manim lesson1.py Chap2_42
manim lesson1.py Chap2_43
manim lesson1.py Chap2_44
manim lesson1.py Chap2_45
manim lesson1.py Chap2_46
manim lesson1.py Chap2_47
manim lesson1.py Chap2_48
manim lesson1.py Chap2_49
manim lesson1.py Chap2_410
manim lesson1.py Chap2_411

#2.5


manim lesson1.py Chap2_50
manim lesson1.py Chap2_51
manim lesson1.py Chap2_52
manim lesson1.py Chap2_53
manim lesson1.py Chap2_54








echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push