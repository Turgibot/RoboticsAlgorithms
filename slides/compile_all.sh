#!/bin/sh
echo Compiling all manim animation and uploading to website

manim introduction.py Intro1
manim introduction.py Intro2
manim introduction.py Admin
manim introduction.py Book
manim introduction.py HowTo
manim introduction.py Overview


manim chapter2.py Chap2_00
manim chapter2.py Chap2_01
manim chapter2.py Chap2_02
manim chapter2.py Chap2_03
#2.1
manim chapter2.py Chap2_10
manim chapter2.py Chap2_11
manim chapter2.py Chap2_12
manim chapter2.py Chap2_13
manim chapter2.py Chap2_14
manim chapter2.py Chap2_15
manim chapter2.py Chap2_16
manim chapter2.py Chap2_17

#2.2
manim chapter2.py Chap2_20
manim chapter2.py Chap2_21
manim chapter2.py Chap2_22
manim chapter2.py Chap2_23
manim chapter2.py Chap2_24
manim chapter2.py Chap2_25
manim chapter2.py Chap2_26
manim chapter2.py Chap2_27
manim chapter2.py Chap2_28
manim chapter2.py Chap2_29
manim chapter2.py Chap2_210
manim chapter2.py Chap2_211
manim chapter2.py Chap2_212
manim chapter2.py Chap2_213

#2.3
manim chapter2.py Chap2_30
manim chapter2.py Chap2_31
manim chapter2.py Chap2_32
manim chapter2.py Chap2_33
manim chapter2.py Chap2_34
manim chapter2.py Chap2_35
manim chapter2.py Chap2_36
manim chapter2.py Chap2_37
manim chapter2.py Chap2_38
manim chapter2.py Chap2_39

#2.4


manim chapter2.py Chap2_40
manim chapter2.py Chap2_41
manim chapter2.py Chap2_42
manim chapter2.py Chap2_43
manim chapter2.py Chap2_44
manim chapter2.py Chap2_45
manim chapter2.py Chap2_46
manim chapter2.py Chap2_47
manim chapter2.py Chap2_48
manim chapter2.py Chap2_49
manim chapter2.py Chap2_410
manim chapter2.py Chap2_411

#2.5


manim chapter2.py Chap2_50
manim chapter2.py Chap2_51
manim chapter2.py Chap2_52
manim chapter2.py Chap2_53
manim chapter2.py Chap2_54

#Chapter 3

manim chapter3.py Chap3_00
manim chapter3.py Chap3_01

#3.1

manim chapter3.py Chap3_10
manim chapter3.py Chap3_11
manim chapter3.py Chap3_12
manim chapter3.py Chap3_13
manim chapter3.py Chap3_14
manim chapter3.py Chap3_15
manim chapter3.py Chap3_16
manim chapter3.py Chap3_17
manim chapter3.py Chap3_18
manim chapter3.py Chap3_19

#3.2.1

manim chapter3.py Chap3_210
manim chapter3.py Chap3_211
manim chapter3.py Chap3_212
manim chapter3.py Chap3_213
manim chapter3.py Chap3_214
manim chapter3.py Chap3_215
manim chapter3.py Chap3_216
manim chapter3.py Chap3_217
manim chapter3.py Chap3_218
manim chapter3.py Chap3_219

#3.2.1.2

manim chapter3.py Chap3_2120
manim chapter3.py Chap3_2121
manim chapter3.py Chap3_2122
manim chapter3.py Chap3_2123
manim chapter3.py Chap3_2124
manim chapter3.py Chap3_2125

#3.2.2

manim chapter3.py Chap3_220
manim chapter3.py Chap3_221
manim chapter3.py Chap3_222
manim chapter3.py Chap3_223
manim chapter3.py Chap3_224

#3.2.3.2

manim chapter3.py Chap3_2320
manim chapter3.py Chap3_2321
manim chapter3.py Chap3_2322
manim chapter3.py Chap3_2323
manim chapter3.py Chap3_2324
manim chapter3.py Chap3_2325
manim chapter3.py Chap3_2326
manim chapter3.py Chap3_2327
manim chapter3.py Chap3_2328

#3.2.3.3

manim chapter3.py Chap3_2330
manim chapter3.py Chap3_2331



#3.3.1

manim chapter3.py Chap3_310












echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push