from manim_slide import *
from datetime import date

class OPU_Slide(SlideScene):
    def add_info(self):
        today = date.today()
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        nbel_img = ImageMobject('../images/nbel.png').scale(0.18).shift(3*UP+5.8*RIGHT)
        name = Text("Guy Tordjman").scale(0.25).shift(3.3*DOWN+6.1*LEFT)
        lecture = Text("Algorithmics Robotics "+str(today.year), color=BLUE).scale(0.25).shift(3.3*DOWN+5.3*RIGHT)
        
        
        self.add(ou_img, name, lecture)
