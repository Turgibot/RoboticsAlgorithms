from numpy import WRAP
from OPU import *
from manim_slide import MyBullets
import random
class Chap2_00(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("Links, Joints, End-Effector", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/basicBot.jpg').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("Framed base image data.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"A robot is mechanically constructed by connecting a set of bodies, called links, to each other using various types of joints.")
        bullets+= Text(r"Actuators, such as electric motors, deliver forces or torques that cause the robot’s links to move.")
        bullets+= Text(r"Usually an end-effector, such as a gripper or hand for grasping and manipulating objects, is attached to a specific link.")
        bullets+= Text(r"All the robots considered in this course have links that can be modeled as rigid bodies")

        blist = MyBullets(latex_grp=bullets, size=4, isNumbered=True).scale(0.3).shift(UP)

        self.play(FadeIn(title, secondary_title, blist,img))

class Chap2_01(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/basicBot.jpg').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"The configuration of a robot is a complete specification of the position of every point of the robot.")
        bullets+= Text(r"The number of Degrees of freedom (DOF) of a robot is the minimum number n of real-valued coordinates needed to represent the configuration.")
        bullets+= Text(r"The Configuration space or C-space, is an n-dimensional space containing all possible configurations of the robot.")
        bullets+= Text(r"The configuration of a robot is represented by a point in its C-space.")
        
        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)

        self.play(FadeIn(title, secondary_title, blist,img))

class Chap2_02(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/basicBot.jpg').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"The configuration of a robot is a complete specification of the position of every point of the robot.")
        bullets+= Text(r"The number of Degrees of freedom (DOF) of a robot is the minimum number n of real-valued coordinates needed to represent the configuration.")
        bullets+= Text(r"The Configuration space or C-space, is an n-dimensional space containing all possible configurations of the robot.")
        bullets+= Text(r"The configuration of a robot is represented by a point in its C-space.")
        
        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)

        self.play(FadeIn(title, secondary_title, blist))
        # line = NumberLine(
        #     x_range=[-10, 10, 1],
        #     length=10,
        #     color=BLUE,
        #     include_numbers=True,
        #     label_direction=UP,
        # ).shift(DOWN)
        # dot = Dot(line.n2p(3),radius=0.1, color=RED)
        # self.play(FadeIn(line, dot))
        # for i in range(25):
        #     rand = random.random()*20 -10
        #     self.play(dot.animate.move_to(line.n2p(rand)), run_time=1)

class Chap2_03(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/basicBot.jpg').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"The configuration of a robot is a complete specification of the position of every point of the robot.")
        bullets+= Text(r"The number of Degrees of freedom (DOF) of a robot is the minimum number n of real-valued coordinates needed to represent the configuration.")
        bullets+= Text(r"The Configuration space or C-space, is an n-dimensional space containing all possible configurations of the robot.")
        bullets+= Text(r"The configuration of a robot is represented by a point in its C-space.")
        
        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)
        circ1, rect1, in_circ1, circ2, rect2, in_circ2, rect0 = get_robot_1dof()
        moving_arm = VGroup(circ1, rect1, in_circ1, circ2, rect2, in_circ2).scale(0.5).shift(DOWN*2)
        rect0.scale(0.5).next_to(circ1, DOWN).shift(UP*0.5)
        self.play(FadeIn(moving_arm,rect0))
        self.play(Rotate(moving_arm,50*DEGREES,about_point=circ1.get_center()), rate_func=linear)
        self.play(Rotate(rect2,50*DEGREES,about_point=circ2.get_center()), rate_func=linear)
        self.play(Rotate(rect2,-70*DEGREES,about_point=circ2.get_center()), rate_func=linear)
        self.play(Rotate(moving_arm,50*DEGREES,about_point=circ1.get_center()), rate_func=linear)
        self.play(Rotate(rect2,-70*DEGREES,about_point=circ2.get_center()), rate_func=linear)
        self.play(Rotate(moving_arm,50*DEGREES,about_point=circ1.get_center()), rate_func=linear)
        self.play(Rotate(rect2,160*DEGREES,about_point=circ2.get_center()), rate_func=linear)

        dof = Text("How many DOF?").scale(0.3).shift(RIGHT*1.5+DOWN*1.5)
        cspace = Text("What's its C-space?").scale(0.3).shift(RIGHT*1.5+DOWN*1.5).next_to(dof, DOWN)

        self.play(Write(dof))
        self.play(Write(cspace))



def get_robot_1dof(dof=1):
    rect1 = Rectangle(BLUE, 0.75,3)
    circ1 = Circle(0.5).next_to(rect1, LEFT).shift(RIGHT*0.5)
    in_circ1= Circle(0.05, color=BLUE).move_to(circ1.get_center())
    rect2 = Rectangle(BLUE, 0.75,3).move_to(rect1.get_right()+RIGHT*2)
    circ2 = Circle(0.5).next_to(rect2, LEFT).shift(RIGHT*0.5)
    in_circ2= Circle(0.05, color=BLUE).move_to(circ2.get_center())
    rect0 = Rectangle(BLUE, 0.75,0.75).next_to(circ1, DOWN).shift(UP*0.5)
    return circ1, rect1, in_circ1, circ2, rect2, in_circ2, rect0

class Chap2_10(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/configuration_coin.png').scale(0.8).shift(DOWN*1.3)
        img_txt = Text("Framed base image data.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"The number of Degrees of freedom (DOF) is the minimum number n of real-valued coordinates needed to represent a configuration.")
        
        blist = MyBullets(latex_grp=bullets, size=4, isNumbered=True).scale(0.3).shift(UP)

       

        self.play(FadeIn(title, secondary_title, blist, img))

