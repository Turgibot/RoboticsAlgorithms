from OPU import *

class Intro1(OPU_Slide):
    def construct(self):
        self.add_info()
        welcome = Text("Welcome to 20944").scale(0.8).shift(UP)
        title = Text("Algorithmic Robotics", color=BLUE).next_to(welcome, DOWN)
        version = Text("Version 0001").scale(0.25).next_to(title,RIGHT).align_to(title, DOWN)
        self.play(Write(welcome), Write(title))
        self.play(Write(version))

class Intro2(OPU_Slide):
    def construct(self):
        self.add_info()
        today = date.today()
        welcome = Text("Welcome to 20944").scale(0.8).shift(UP)
        old_title = Text("Algorithmic Robotics", color=BLUE).next_to(welcome, DOWN)
        self.add(old_title)
        lecture = Text("Algorithmic Robotics "+str(today.year), color=BLUE).scale(0.25).shift(3.3*DOWN+5.3*RIGHT)
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
        bul2 = "4 assignments - must submit at least 3 @ 5 points each."
        bul3 = "Assignments contribute max 15 or 20 pts. exam contributes 85 or 80 pts."
        bullets = [bul0,bul1,bul2, bul3]
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
        bul4 = "Plenty of online resources including wiki, Coursera and GitHub"

        bullets = [bul0,bul1,bul2,bul3,bul4]
        blist = BulletedList(*bullets).scale(0.5).shift(LEFT*1.2+UP)
        self.play(FadeIn(title, secondary_title, blist, img))

class HowTo(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("How to study and succeed in the course").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN+LEFT).scale(0.4)
        img = ImageMobject('../images/facing.jpg').scale(0.4).shift(RIGHT*3.5+DOWN*1.6)
        img_txt = Text("Framed base image data.").scale(0.3).next_to(img, DOWN)

        bul0 = "Read the relevant material in the book and course material."
        bul1 = "Watch Elishai's videos."
        bul2 = "Practise a few questions from the book before class."
        bul3 = "Zoom and participate in lessons.(sessions are recorded and uploaded)"
        bul4 = "Complete all the assignments"
        bul5 = "Ask anything during lecture. email anytime or call me on Tuesday 13-14 at 053-7203788"

        bullets = [bul0,bul1,bul2,bul3,bul4, bul5]
        blist = BulletedList(*bullets).scale(0.5).shift(LEFT*1.5+UP*0.7)
        self.play(FadeIn(title, secondary_title, blist, img))

class Overview(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Course Overview").shift(UP*3).scale(0.65)
        secondary_title = Text("The course subjects 6 chapters in the book:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/boston.jpg').scale(0.9).shift(DOWN*1.3)
        img_txt = Text("Framed base image data.").scale(0.3).next_to(img, DOWN)

        bul0 = "Chapter 2: Configuration Space."
        bul1 = "Chapter 3: Rigid-Body Motions."
        bul2 = "Chapter 4: Forward Kinematics."
        bul3 = "Chapter 5: Velocity Kinematics and Statics."
        bul4 = "Chapter 6: Inverse Kinematics."
        bul5 = "Chapter 8: Dynamics of Open Chains."

        bullets = [bul0,bul1,bul2,bul3,bul4, bul5]
        for i in range(len(bullets)):
            bullets[i] = str(i+1)+". "+bullets[i]
        blist = BulletedList(*bullets, dot_scale_factor=0).scale(0.5)
        img.next_to(blist, RIGHT)
        main = Group(blist, img).center()
        self.play(FadeIn(title, secondary_title, main))