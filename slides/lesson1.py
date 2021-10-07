from OPU import *

class Intro1(OPU_Slide):
    def construct(self):
        self.add_info()
        welcome = Text("Welcome to 20944").scale(0.8).shift(UP)
        title = Text("Robotics Algorithms", color=BLUE).next_to(welcome, DOWN)
        version = Text("Version 0001").scale(0.25).next_to(title,RIGHT).align_to(title, DOWN)
        self.play(Write(welcome), Write(title))
        self.play(Write(version))

class Intro2(OPU_Slide):
    def construct(self):
        self.add_info()
        today = date.today()
        welcome = Text("Welcome to 20944").scale(0.8).shift(UP)
        old_title = Text("Robotics Algorithms", color=BLUE).next_to(welcome, DOWN)
        self.add(old_title)
        lecture = Text("Robotics Algorithms "+str(today.year), color=BLUE).scale(0.25).shift(3.3*DOWN+5.3*RIGHT)
        self.play(ReplacementTransform(old_title, lecture))

class Admin(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Administrative").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN+LEFT).scale(0.4)
        img = ImageMobject('../images/pointing.jpg').scale(0.27).shift(RIGHT*4.5+1.9*UP)
        img_txt = Text("Framed base image data").scale(0.3).next_to(img, DOWN)
        # bul0 = Text("Dr. Elishai Ezra Tsur - Course manager.     email : elishai@nbel-lab.com")
        # bul1 = Text("Guy Tordjman - Course Host.     email : turgibot@gmail.com.     cell : 053-7203788").scale(0.3).next_to(bul0, DOWN).align_to(bul0, LEFT)
        # bul2 = Text("4 assignments - must submit 3/4.").scale(0.3).next_to(bul1, DOWN).align_to(bul1, LEFT)
        # bul3 = Text("...").scale(0.3).next_to(bul2, DOWN).align_to(bul2, LEFT)
        # bul4 = Text("...").scale(0.3).next_to(bul3, DOWN).align_to(bul3, LEFT)
        bul0 = "Dr. Elishai Ezra Tsur - Course manager.     email : elishai@nbel-lab.com"
        bul1 = "Guy Tordjman - Course Host.     email : turgibot@gmail.com.     cell : 053-7203788"
        bul2 = "4 assignments - must submit 3/4."
        bul3 = "4 assignments - must submit 3/4."
        bullets = [bul0,bul1,bul2]
        blist = BulletedList(*bullets).scale(0.5).shift(LEFT*1.2+UP)
        self.play(FadeIn(title, secondary_title, blist, img))

class Book(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Course Book").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN+LEFT).scale(0.4)
        img = ImageMobject('../images/book.jpg').scale(0.3).shift(RIGHT*4.5)
        img_txt = Text("Framed base image data").scale(0.3).next_to(img, DOWN)
        bul0 = "Modern Robotics - by Kevin M. Lynch and Frnack C. Park"
        bul2 = "Alongsided by short video lessons from Dr. Elishai"
        bul1 = "Our course deals with 6 chapters"
        bul3 = "Excerises mostly from the book"
        bul4 = "Plenty of online resources including Coursera and GitHub"

        bullets = [bul0,bul1,bul2,bul3,bul4]
        blist = BulletedList(*bullets).scale(0.5).shift(LEFT*1.2+UP)
        self.play(FadeIn(title, secondary_title, blist, img))

class HowTo(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("How to study and succeed in the course").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN+LEFT).scale(0.4)
        img = ImageMobject('../images/facing.jpg').scale(0.5).shift(RIGHT*2+DOWN*1.3)
        img_txt = Text("Framed base image data.").scale(0.3).next_to(img, DOWN)

        bul0 = "Read the elevant material in the book and course notebook."
        bul1 = "Watch Elishai's videos."
        bul2 = "Practise a few questions before class."
        bul3 = "Zoom and participate in lessons.(sessions are recorded and uploaded)"
        bul4 = "Complete all the assignments"
        bul5 = "Ask anything anytime!!!"

        bullets = [bul0,bul1,bul2,bul3,bul4, bul5]
        blist = BulletedList(*bullets).scale(0.5).shift(LEFT*1.2+UP*0.7)
        self.play(FadeIn(title, secondary_title, blist, img))