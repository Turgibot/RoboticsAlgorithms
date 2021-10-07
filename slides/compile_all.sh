#!/bin/sh
echo Compiling all manim animation and uploading to website

manim lesson0.py Intro1
manim lesson0.py Intro2
manim lesson0.py Admin
manim lesson0.py Book
manim lesson0.py HowTo
manim lesson0.py Overview












echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push