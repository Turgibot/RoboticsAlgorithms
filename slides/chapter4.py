from OPU import *
from manim_slide import MyBullets



class Chap4_00(OPU_Slide):
   def construct(self):
        note = "בוא נעשה סקירה קצרה של החומר שלמדנו בקורס עד כה:\
                התחלנו בלדבר על קונפיגורציות ודרגות חופש של גופים קשיחים.\
                        המשכנו לדבר על תנועה של גוף קשיחי והתייחסנו לייצוג של רוטציה באמצעות מטריצות רוטציה ואז באמצעות קואורדינטות אקפוננציאליות.\
                                 ואת המפגש האחרון סיימנו בעצם כשדיברנו על מטריצות טרנפורמציה שמשלבות ייצוג של רוטציה וטרנסלציה ואז הגענו לדבר על ייצוג בורג והשתמשנו בו בייצוג הקואורדינטות האקספוננציאליות של קונפיגורציה. \
                                         היום נלמד נושא חשוב ומעניין שנקרא פורוורד קינמטיקס. קינמטיקס מתייחס לתנועה של גופים ומערכות ואילו המילה פורוורד מתארת את הגישה החישובית.\
                                                 מה שאנחנו בעצם מחשבים הוא את המיקום והאוריאנטציה של האנד אפקטור באמצעות הנתונים מהג'וינטס של הרובוט."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Roadmap : ", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/bluebot.jpg').scale(0.99).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"Configuration space, joint, links, DOF, grublers formula, task and workspaces ...")
        bullets+= Text(r"Rigid body motion, rotation matrices, twist, transformation matrices, screw motion, exponential coordinates")
        bullets+= Text(r"Today: Forward kinematics - the calculation of the position and orientation of the EE from its joint coordinates")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=True).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist, img)
        self.wait()


class Chap4_01(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        img1 = ImageMobject('../images/fk0.png').scale(1.1).next_to(img, RIGHT)

        self.add(title, secondary_title, prob, img, img1)
        self.wait()


class Chap4_02(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 1: Trigonometrically", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/tig.png').scale(1.5).next_to(sol1, DOWN).align_to(sol1, LEFT)

        

        self.add(title, secondary_title, prob, img, sol1, img1)
        self.wait()

class Chap4_03(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/fk1.png').scale(0.8).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 1: Trigonometrically", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = Text("?", color=RED).scale(3).next_to(sol1, DOWN)

        

        self.add(title, secondary_title, prob, img, sol1, img1)
        self.wait()

class Chap4_04(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)

        self.add(title, secondary_title, prob, img)
        self.wait()


class Chap4_05(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 2: Transformation matrix multiplication", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/t04.png').scale(1.4).next_to(sol1, DOWN)
        img2 = ImageMobject('../images/t04mat.png').scale(1.3).next_to(img1, DOWN).align_to(sol1, LEFT)

        self.add(title, secondary_title, prob, img, sol1, img1, img2)
        self.wait()

class Chap4_06(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 3: Product of Exponentials", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/poe0.png').scale(1.4).next_to(sol1, DOWN)
        img2 = ImageMobject('../images/poe1.png').scale(1.3).next_to(img1, DOWN)
        self.add(title, secondary_title, prob, img, sol1, img1, img2)
        self.wait()

class Chap4_07(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("In this course ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"We only deal with open chain robots where the joints to consider are:", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/joints.png').scale(0.7).shift(DOWN*1.1)
        jnt = Text("Joint Types", color=GREEN).scale(0.3).next_to(img, LEFT).shift(DOWN*0.5)
        

        self.add(title, secondary_title, prob, img, jnt)
        self.wait()




#Denavit Hartenberg Parameters

class DH_00(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("F.K. using D.H. method:", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        bullets = VGroup()
        bullets+= Text(r"Assign frames according to the D.H. convention rules")
        bullets+= Text(r"Create the D.H. parameters table.")
        bullets+= Text(r"Plug the table values into the corresponding H.T.M.")
        bullets+= Text(r"Multiply the H.T.M together in order")
        
        blist = MyBullets(latex_grp=bullets, size=4, isNumbered=True).scale(0.3).shift(UP)
        self.add(title, secondary_title, blist)
        self.wait()

class DH_01(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"We only deal with open chain robots where the joints to consider are:", color=RED).next_to(secondary_title, DOWN).scale(0.5)

        self.add(title, secondary_title, img, ll, lr)
        self.wait()


class DH_02(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.123)

        self.add(title, secondary_title, img, ll, lr, rule1, rule11)
        self.wait()


class DH_03(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.123)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)
        self.wait()

class DH_04(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/prismatic1.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
       
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4.5,-0.5,0], end=[-2.9,0.45,0], color=RED)
        zr = Arrow(start=[-4.5,-0.53,0], end=[-2.9,0.45,0], color=RED).shift(RIGHT*1.13)
        zl_ = Tex(r"$\hat{z}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, rule1, rule11, zl, zr, zl_, zr_)
        self.wait()

class DH_05(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.123)
        self.add(rule2, rule21)

        self.wait()

class DH_06(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.123)
        self.add(rule2, rule21)

        orthogonal = Line(start=[-4.5,-1.5,0], end=[-1.8,-1.3,0], stroke_width=2.1, color=BLUE)
        self.add(orthogonal)
        self.wait()

