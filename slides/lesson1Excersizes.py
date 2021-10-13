from math import e
from cv2 import FILLED
from numpy import WRAP
from OPU import *
from manim_slide import MyBullets
import random
class Chap2ex1(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
       
        question = ImageMobject('../images/ch2ex1.png')
        solution = ImageMobject('../images/ch2so1.png')
        self.play(FadeIn(title, question))
