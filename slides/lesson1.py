from math import e
from cv2 import FILLED
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
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_plane.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)").scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m = ", color=RED).scale(0.4).next_to(img, DOWN)

        self.play(FadeIn(title, secondary_title, definition_txt))

class Chap2_11(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_plane.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)").scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m =  ", color=RED).scale(0.4).next_to(img, DOWN).shift(LEFT*2)

        self.add(title, secondary_title, definition_txt)
        self.play(FadeIn( img, dof))

class Chap2_12(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_plane.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)").scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m =  ", color=RED).scale(0.4).next_to(img, DOWN).shift(LEFT*2)
        answer = Tex(r"$(x,y,\theta) + heads/tails$", color=RED).scale(0.6).next_to(img, RIGHT)
        self.add(title, secondary_title, definition_txt, img, dof)
        self.play(FadeIn( answer))

class Chap2_13(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_plane.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)").scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m = 3", color=RED).scale(0.4).next_to(img, DOWN).shift(LEFT*2)
        answer = Tex(r"$(x,y,\theta) + heads/tails$", color=RED).scale(0.6).next_to(img, RIGHT)
        self.add(title, secondary_title, definition_txt, img, dof, answer)
        x = Tex(r"$X$", color=BLUE).scale(2).next_to(img, RIGHT).shift(1.5*RIGHT)
        unreal = Text("NOT A REAL NUMBER", color=BLUE).scale(0.3).next_to(x, DOWN)
        self.play(FadeIn(x, unreal))

class Chap2_14(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_space.png').scale(0.7).shift(DOWN*0.6)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP).shift(UP*0.3)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)", color=RED).scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m =  ", color=RED).scale(0.4).next_to(img, DOWN).shift(LEFT*2)
        a = Text("A", color=BLUE).scale(0.4).shift(RIGHT*0.2)
        b = Text("B", color=BLUE).scale(0.4).shift(RIGHT*0.2+DOWN*0.7)
        c = Text("C", color=BLUE).scale(0.4).shift(RIGHT*1.3+DOWN*0.3)
        self.add(title, secondary_title, definition_txt)
        self.play(FadeIn( img, dof, equation, a, b, c))

class Chap2_15(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_space.png').scale(0.7).shift(DOWN*0.6)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP).shift(UP*0.3)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)", color=RED).scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m =  ", color=RED).scale(0.4).next_to(img, DOWN).shift(LEFT*2)
        a = Text("A", color=BLUE).scale(0.4).shift(RIGHT*0.2)
        b = Text("B", color=BLUE).scale(0.4).shift(RIGHT*0.2+DOWN*0.7)
        c = Text("C", color=BLUE).scale(0.4).shift(RIGHT*1.3+DOWN*0.3)
        self.add(title, secondary_title, definition_txt, img, dof, equation, a, b, c)

        point = Text("Point     #DOF        #Constraints     m", color=BLUE).scale(0.3).next_to(img, RIGHT).shift(UP)
        a_ = Text("A", color=BLUE).scale(0.4).next_to(point, DOWN). align_to(point, LEFT).shift(RIGHT*0.2)
        b_ = Text("B", color=BLUE).scale(0.4).next_to(a_, DOWN). align_to(a_, LEFT)
        c_ = Text("C", color=BLUE).scale(0.4).next_to(b_, DOWN). align_to(b_, LEFT)
        self.play(FadeIn(point, a_, b_, c_))

class Chap2_16(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/coin_space.png').scale(0.7).shift(DOWN*0.6)
        definition_txt = Text("DOF : The minimum number n of real-valued coordinates needed to represent a configuration.").scale(0.3).next_to(img, UP).shift(UP*0.3)
        equation = Text("DOF = (sum of freedoms of the bodies) - (number of independent constraints)", color=RED).scale(0.3).next_to(definition_txt, DOWN)
        dof = Text("#DOF = m = 3+2+1 = 6 ", color=RED).scale(0.4).next_to(img, DOWN)
        a = Text("A", color=BLUE).scale(0.4).shift(RIGHT*0.2)
        b = Text("B", color=BLUE).scale(0.4).shift(RIGHT*0.2+DOWN*0.7)
        c = Text("C", color=BLUE).scale(0.4).shift(RIGHT*1.3+DOWN*0.3)
        self.add(title, secondary_title, definition_txt, img, equation, a, b, c)

        point = Text("Point     #DOF        #Constraints     m", color=BLUE).scale(0.3).next_to(img, RIGHT).shift(UP)
        a_ = Text("A         3       -        0    =    3", color=BLUE).scale(0.4).next_to(point, DOWN). align_to(point, LEFT).shift(RIGHT*0.2)
        b_ = Text("B         3       -        1    =    2", color=BLUE).scale(0.4).next_to(a_, DOWN). align_to(a_, LEFT)
        c_ = Text("C         3       -        2    =    1", color=BLUE).scale(0.4).next_to(b_, DOWN). align_to(b_, LEFT)
        self.play(FadeIn(point, a_, b_, c_, dof))

class Chap2_17(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.1 Degrees of Freedom of a Rigid Body", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/configuration_coin.png').scale(0.7).shift(DOWN*0.6)
        
        self.add(title, secondary_title, img)


        conclusion0 = Text("CONCLUSION", color=BLUE).next_to(img, UP).shift(UP)
        conclusion1 = Text("A rigid body moving in a 3D space, (spatial rigid body), has 6 DOF.", color=RED).next_to(conclusion0, DOWN)
        conclusion2 = Text("A rigid body moving in a 2D plane (planar rigid body), has 3 DOF.", color=RED).next_to(conclusion1, DOWN).shift(DOWN*0.2)

        conclusion = VGroup( conclusion1, conclusion2).scale(0.3)
        self.play(Write(conclusion))


class Chap2_20(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2 Degrees of Freedom of a Robot", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/joint_types.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("Joint types and their DOF").scale(0.3).next_to(img, UP)
        self.play(FadeIn(title, secondary_title, definition_txt,img))
       

class Chap2_21(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2 Degrees of Freedom of a Robot", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/joint_types.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("Joint types and their DOF").scale(0.3).next_to(img, UP)
        self.add(title, secondary_title)
         #include video
        cap = cv2.VideoCapture("../media/videos/revolute.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(0.5*DOWN + RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Chap2_22(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2 Degrees of Freedom of a Robot", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/joint_types.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("Joint types and their DOF").scale(0.3).next_to(img, UP)
        self.add(title, secondary_title)
         #include video
        cap = cv2.VideoCapture("../media/videos/prismatic.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(0.5*DOWN + RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Chap2_23(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2 Degrees of Freedom of a Robot", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/joint_types.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("Joint types and their DOF").scale(0.3).next_to(img, UP)
        self.add(title, secondary_title)
         #include video
        cap = cv2.VideoCapture("../media/videos/spherical.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(0.5*DOWN + RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

class Chap2_24(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2 Degrees of Freedom of a Robot", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/joint_types.png').scale(0.7).shift(DOWN*0.5)
        definition_txt = Text("Joint types and their DOF").scale(0.3).next_to(img, UP)
        self.add(title, secondary_title)
         #include video
        cap = cv2.VideoCapture("../media/videos/universal.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(0.5*DOWN + RIGHT)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()


class Chap2_25(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/grubler.png').scale(0.8).shift(DOWN*0.5+RIGHT*3.5)
        definition_txt = Text("").scale(0.3).next_to(img, UP)
        self.add(title, secondary_title)

        bul0 = Tex(r"$\cdot$ Let $N$ be the number of links (Ground is also regarded as a link).")
        bul1 = Tex(r"$\cdot$ Let $J$ be the number of joints.").next_to(bul0, DOWN).align_to(bul0, LEFT)
        bul2 = Tex(r"$\cdot$ Let $m$ be the number of DOF of a rigid body. (3 planar 6 spatial mechanism)").next_to(bul1, DOWN).align_to(bul1, LEFT)
        bul3 = Tex(r"$\cdot$ Let $f_i$ be the number of freedoms provided by joint $i$.").next_to(bul2, DOWN).align_to(bul2, LEFT)
        bul4 = Tex(r"$\cdot$ Let $c_i$ be the number of constraints provided by joint $i$.").next_to(bul3, DOWN).align_to(bul3, LEFT)
        
        bullets = VGroup(bul0, bul1, bul2, bul3, bul4)
        bullets.scale(0.4).next_to(img, LEFT).shift(LEFT+UP)
        border = Rectangle(color=RED).surround(img, buff=1.5)
        self.play(FadeIn(img, bullets, border))

class Chap2_26(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 1", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/kr.png').scale(0.8).shift(DOWN*0.5+LEFT*3)
        img_title = Text("k-link planar serial chain", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        
        border = Rectangle(color=BLUE).surround(img, buff=1.5)
        self.play(FadeIn(img,img_title, border, formula, border_f))

class Chap2_27(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 1", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/kr.png').scale(0.8).shift(DOWN*0.5+LEFT*3)
        img_title = Text("k-link planar serial chain", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        
        border = Rectangle(color=BLUE).surround(img, buff=1.5)
        self.add(img,img_title, border, formula, border_f)
        solution = Tex(r"$dof = 3((k+1)-1-k)+k = k$", color = GREEN).scale(0.6).next_to(img, RIGHT).shift(RIGHT*1.3)
        self.play(FadeIn(solution))

class Chap2_28(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 2", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/watt.png').scale(0.95).shift(DOWN*0.5+LEFT*3)
        img_title = Text("Watt six-bar linkage", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        
        border = Rectangle(color=BLUE).surround(img, buff=1.5)
        self.play(FadeIn(img,img_title, border, formula, border_f))

class Chap2_29(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 2", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/watt.png').scale(0.95).shift(DOWN*0.5+LEFT*3)
        img_title = Text("Watt six-bar linkage", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        
        border = Rectangle(color=BLUE).surround(img, buff=1.5)
        self.add(img,img_title, border, formula, border_f)
        solution0 = Tex(r"$ m=3, N=6, J=7, f_i=1$", color = GREEN).scale(0.6).next_to(img, RIGHT).shift(RIGHT*1.3)
        solution1 = Tex(r"$dof = 3((6)-1-7)+ 7 = 1$", color = GREEN).scale(0.6).next_to(solution0, DOWN)

        self.play(FadeIn(solution0, solution1))

class Chap2_210(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 3", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/stewart.png').scale(0.85).shift(DOWN*0.5+LEFT*3)
        img_title = Text("Stewart–Gough platform", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        self.add(formula, border_f)
        self.play(FadeIn(img,img_title))

class Chap2_211(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 3", color=BLUE).next_to(title, DOWN).scale(0.4)
        # img = ImageMobject('../images/stewart.png').scale(0.85).shift(DOWN*0.5+LEFT*3)
        # img_title = Text("Stewart–Gough platform", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        self.add(formula, border_f)

        cap = cv2.VideoCapture("../media/videos/stewart.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.5).shift(DOWN)
                self.add(frame_img)
                self.wait(0.022) #faster
                self.remove(frame_img)
            
        cap.release()



class Chap2_212(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 3", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/stewart.png').scale(0.85).shift(DOWN*0.5+LEFT*3)
        img_title = Text("Stewart–Gough platform", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        self.add(formula, border_f, img,img_title)
        solution0 = Tex(r"$ m=6, N=14, J=18$", color = GREEN).scale(0.6).next_to(img, RIGHT).shift(RIGHT*1.3+UP*1.5)
        solution01 = Tex(r"$6 \cdot (univeral):f_i=2$", color = GREEN).scale(0.6).next_to(solution0, DOWN)
        solution02 = Tex(r"$6 \cdot (spherical):f_i=3$", color = GREEN).scale(0.6).next_to(solution01, DOWN)
        solution03 = Tex(r"$6 \cdot (prismatic):f_i=1$", color = GREEN).scale(0.6).next_to(solution02, DOWN)

        self.play(FadeIn(solution0, solution01, solution02, solution03))


class Chap2_213(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.2.2 Grübler’s Formula - Example 3", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/stewart.png').scale(0.85).shift(DOWN*0.5+LEFT*3)
        img_title = Text("Stewart–Gough platform", color=BLUE).next_to(img, DOWN).scale(0.25)
        self.add(title, secondary_title)
        formula = Tex(r"$dof = m(N-1-J)+\sum_{i=1}^J{f_i}$").scale(0.4).shift(RIGHT*4.6+UP*2)
        border_f = Rectangle(color=RED).surround(formula)
        self.add(formula, border_f, img,img_title)
        solution0 = Tex(r"$ m=6, N=14, J=18$", color = GREEN).scale(0.6).next_to(img, RIGHT).shift(RIGHT*1.3+UP*1.5)
        solution01 = Tex(r"$6 \cdot (univeral):f_i=2$", color = GREEN).scale(0.6).next_to(solution0, DOWN)
        solution02 = Tex(r"$6 \cdot (spherical):f_i=3$", color = GREEN).scale(0.6).next_to(solution01, DOWN)
        solution03 = Tex(r"$6 \cdot (prismatic):f_i=1$", color = GREEN).scale(0.6).next_to(solution02, DOWN)


        self.add(solution0, solution01, solution02, solution03)

        solution03 = Tex(r"$dof = 6(14-1-18)+6(1)+6(2)+6(3) = 6$", color = BLUE).scale(0.6).next_to(solution03, DOWN).shift(RIGHT)

        self.play(FadeIn(solution03))

class Chap2_30(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        solution0 =  Tex(r"dof is the dimension of the C-space, toplogy is its shape", color = GREEN).scale(0.6).center().shift(UP*1.5)
        solution01 = Tex(r"Two C-spaces may have the same dof but differ in other ways.", color = GREEN).scale(0.6).next_to(solution0, DOWN)
       
        rec = ImageMobject('../images/plane.png').scale(1.5).shift(DOWN+RIGHT*3)
        sphere = ImageMobject('../images/sphere.png').scale(1.2).shift(DOWN+LEFT*3)
        plane_txt = Text ("The 2D surface of a plane").scale(0.3).next_to(rec, DOWN)
        sphere_txt = Text ("The 2D surface of a sphere").scale(0.3).next_to(sphere, DOWN)

        self.play(FadeIn(solution0, solution01, rec, sphere, sphere_txt, plane_txt))
        


class Chap2_31(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        solution0 =  Tex(r"The topology of a space is independent of how we represent it.", color = GREEN).scale(0.6).center().shift(UP*1.5)
        solution01 = Tex(r"Two spaces are topologically equivalent if one can be smoothly deformed to the other without cutting or pasting.", color = GREEN).scale(0.6).next_to(solution0, DOWN)
        
        self.play(FadeIn(solution0, solution01))
        
        cap = cv2.VideoCapture("../media/videos/mug.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.4).shift(DOWN*2)
                self.add(frame_img)
                self.wait(0.032) 
                self.remove(frame_img)
            
        cap.release()


class Chap2_32(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        solution0 =  Tex(r"1D topologically distinct shapes:.", color = GREEN).scale(0.6).center().shift(UP*1.5+LEFT*3)
        solution01 = Tex(r"2D topologically distinct shapes:", color = GREEN).scale(0.6).next_to(solution0, RIGHT).shift(RIGHT*2)
        
        self.add(solution0, solution01)

        d1 = ImageMobject('../images/1d.png').scale(1).shift(DOWN+LEFT*3)
        s1_tex=Tex(r"$\mathbb{S}^1$", color=BLUE).scale(0.4).next_to(d1, LEFT).shift(UP)
        e1_tex=Tex(r"$\mathbb{E}^1$", color=BLUE).scale(0.4).next_to(s1_tex, DOWN).shift(DOWN*1.5)
        sphere = ImageMobject('../images/sphere.png').scale(0.8).shift(RIGHT*2.5)
        torus = ImageMobject('../images/torus.png').scale(1).next_to(sphere, RIGHT)
        plane = ImageMobject('../images/plane.png').scale(0.9).next_to(sphere, DOWN)
        cylinder = ImageMobject('../images/cylinder.png').scale(1).next_to(plane, RIGHT)
        e2_tex=Tex(r"$\mathbb{E}^2$", color=BLUE).scale(0.4).next_to(plane, LEFT)
        s2_tex=Tex(r"$\mathbb{S}^2$", color=BLUE).scale(0.4).next_to(sphere, LEFT)
        t2_tex=Tex(r"$\mathbb{T}^2$", color=BLUE).scale(0.4).next_to(torus, RIGHT)
        exs_tex=Tex(r"$\mathbb{E}^1 \times \mathbb{S}^1$", color=BLUE).scale(0.4).next_to(cylinder, RIGHT)

        self.play(FadeIn(d1, sphere, torus, plane, cylinder,s1_tex, e1_tex, e2_tex, s2_tex, t2_tex, exs_tex))

       
class Chap2_33(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        solution0 = Tex(r"Some spaces are Cartesian products of spaces of lower dimension, e.g.,", color = GREEN).scale(0.6).center().shift(UP*1.5)
        
        
        coin_plane = ImageMobject('../images/coin_plane.png').scale(0.7).shift(RIGHT*2+DOWN*0.5)
        e2xs_tex=Tex(r"$\mathbb{E}^2 \times \mathbb{S}^1$", color=BLUE).scale(0.4).next_to(coin_plane, RIGHT)
        cylinder = ImageMobject('../images/cylinder.png').scale(1).next_to(coin_plane, LEFT).shift(LEFT*2)
        exs_tex=Tex(r"$\mathbb{E}^1 \times \mathbb{S}^1$", color=BLUE).scale(0.4).next_to(cylinder, LEFT)


        self.play(FadeIn(solution0, coin_plane, e2xs_tex, cylinder, exs_tex))

class Chap2_34(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img = ImageMobject('../images/cspace_tbl.png').scale(0.8).shift(DOWN*0.5)
        
        self.play(FadeIn(img))

class Chap2_35(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        cap = cv2.VideoCapture("../media/videos/cspace_torus.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.9).shift(DOWN*0.5)
                self.add(frame_img)
                self.wait(0.042) 
                self.remove(frame_img)
            
        cap.release()

class Chap2_36(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        cap = cv2.VideoCapture("../media/videos/cspace_cylinder.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.9).shift(DOWN*0.5)
                self.add(frame_img)
                self.wait(0.042) 
                self.remove(frame_img)
            
        cap.release()

class Chap2_37(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        cap = cv2.VideoCapture("../media/videos/cspace_sphere.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.9).shift(DOWN*0.5)
                self.add(frame_img)
                self.wait(0.042) 
                self.remove(frame_img)
            
        cap.release()


class Chap2_38(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        sphere_opt = ImageMobject('../images/sphere_opt.png').shift(UP*0.8)
        
        self.play(FadeIn(sphere_opt))



class Chap2_39(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.3: Topology and Representation", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        sphere_opt = ImageMobject('../images/sphere_opt.png').shift(UP*0.8)
        explicit = ImageMobject('../images/explicit.png').shift(DOWN*1.5+LEFT*1.35)
        implicit = ImageMobject('../images/implicit.png').shift(DOWN*1.47+RIGHT*1.7)
        self.add(sphere_opt)
        self.play(FadeIn(implicit, explicit))




class Chap2_40(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        four_bar = ImageMobject('../images/4bar.png').scale(0.8).shift(LEFT*4)
        four_txt = Text("The four bar linkage.", color=BLUE).next_to(four_bar, DOWN).scale(0.3).shift(UP*0.3)

        
        self.add(four_bar, four_txt)

        dof = Tex(r"dof =            ", color=RED).scale(0.5).shift(RIGHT+UP)
        topology = Tex(r"Topology :  ", color=RED).scale(0.5).next_to(dof, DOWN).align_to(dof, LEFT)
        implicit = Tex(r"Implicit representaion :  ", color=RED).scale(0.5).next_to(topology, DOWN).align_to(topology, LEFT)
        explicit = Tex(r"Explicit representaion :  ", color=RED).scale(0.5).next_to(implicit, DOWN).align_to(implicit, LEFT)

        self.play(FadeIn(dof, topology, implicit, explicit))

class Chap2_41(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        four_bar = ImageMobject('../images/4bar.png').scale(0.8).shift(LEFT*4)
        four_txt = Text("The four bar linkage.", color=BLUE).next_to(four_bar, DOWN).scale(0.3).shift(UP*0.3)

        
        self.add(four_bar, four_txt)

        dof = Tex(r"dof = 3(4-1-4)+4 = 1", color=RED).scale(0.5).shift(RIGHT+UP)
        topology = Tex(r"Topology : $\mathbb{E}^1$", color=RED).scale(0.5).next_to(dof, DOWN).align_to(dof, LEFT)
        implicit = Tex(r"Implicit representaion : $\mathbb{R}^1$", color=RED).scale(0.5).next_to(topology, DOWN).align_to(topology, LEFT)
        explicit = Tex(r"Explicit representaion : $\mathbb{R}^4$", color=RED).scale(0.5).next_to(implicit, DOWN).align_to(implicit, LEFT)

        self.play(FadeIn(dof, topology, implicit, explicit))




class Chap2_42(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        four_bar = ImageMobject('../images/4bar.png').scale(0.8).shift(LEFT*4)
        four_txt = Text("The four bar linkage.", color=BLUE).next_to(four_bar, DOWN).scale(0.3).shift(UP*0.3)

        holonomic_eq = ImageMobject('../images/holonomic.png').scale(1.2).next_to(four_bar, RIGHT)

        
        self.add(four_bar, four_txt)

        holonomic = Text(r"k independent").scale(0.3).shift(LEFT*4.5+UP*1.6)
        bold = Text(r"holonomic constraints", color=RED, weight=BOLD).scale(0.3).next_to(holonomic, RIGHT).shift(LEFT*0.15+UP*0.02)
        on = Text(r"on n unknown variables reduce an n-dim C-space to n-k dof").scale(0.3).next_to(bold, RIGHT).shift(LEFT*0.15+DOWN*0.02)

        loop = Text("loop-closure equations", color=GREEN).scale(0.25).next_to(holonomic_eq, DOWN)
        self.play(FadeIn(holonomic_eq, holonomic, bold, on, loop))

class Chap2_43(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        

        holonomic = Text(r"k independent").scale(0.3).shift(LEFT*4.5+UP*1.6)
        bold = Text(r"holonomic constraints", color=RED, weight=BOLD).scale(0.3).next_to(holonomic, RIGHT).shift(LEFT*0.15+UP*0.02)
        on = Text(r"on n unknown variables reduce an n-dim C-space to n-k dof").scale(0.3).next_to(bold, RIGHT).shift(LEFT*0.15+DOWN*0.02)

        g_thetas = ImageMobject('../images/g_thetas.png').scale(1.3).shift(DOWN*1)
        
        general = Text("A general form, for", color=GREEN).scale(0.3).shift(LEFT+UP*0.5)
        thetas = Tex(r"$\theta = [\theta_1, ... , \theta_n]^T$", color=GREEN).scale(0.5).next_to(general, RIGHT)
        
        self.add(holonomic, bold, on)

        self.play(FadeIn(  g_thetas, general, thetas))


class Chap2_44(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        

        pfaffian0 = Text(r"Suppose that a closed-chain robot with such loop-closure equations is in motion.").scale(0.3).shift(UP*1.6)
        pfaffian1 = Text(r"Pfaffian constraints:", color=RED).scale(0.3).shift(LEFT*4.5+UP)
        pfaffian2 = Text(r"are constraints on velocity:").scale(0.3).next_to(pfaffian1, RIGHT).shift(LEFT*0.15)
        

        vel0 = ImageMobject('../images/vel0.png').scale(1).shift(LEFT*4+0.3*DOWN)
        vel2 = ImageMobject('../images/vel2.png').scale(1).shift(DOWN*1).next_to(vel0, RIGHT).shift(RIGHT*0.5)
        vel3 = ImageMobject('../images/vel3.png').scale(1).shift(DOWN*1).next_to(vel2, RIGHT).shift(RIGHT*0.5)
        vel4 = ImageMobject('../images/vel4.png').scale(1).shift(DOWN*1.8+RIGHT)
        
        pfaffian3 = Text(r"The pfaffian constraints can be written as", color=GREEN).scale(0.3).next_to(vel4, LEFT)
        pfaffian4 = Text(r"If pfaffian constraints can be integrated to equivalent configuration constraints, they are ", color=BLUE).scale(0.3).next_to(pfaffian3, DOWN).shift(RIGHT)
        pfaffian5 = Text(r"holonomic.", color=RED ).scale(0.3).next_to(pfaffian4, RIGHT).shift(LEFT*0.15+UP*0.02)
        self.add(pfaffian0, pfaffian1, pfaffian2)

        self.play(FadeIn(pfaffian3,pfaffian4,pfaffian5, vel0, vel2, vel3, vel4))

class Chap2_45(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/car.png').scale(0.8).shift(DOWN+LEFT*1.3).shift(LEFT*2.3)
        rolling_txt = Text("A car on a plane.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"$q = \begin{pmatrix}\phi\\x\\y \end{pmatrix}$").scale(0.5).next_to(rolling, LEFT).shift(UP*1.4)
        x_vec = Vector().move_to(rolling, aligned_edge=LEFT).shift(LEFT+DOWN)
        y_vec = Vector(UP).move_to(rolling, aligned_edge=LEFT).shift(LEFT*1.1+DOWN*0.5)
        x = Text("x").scale(0.25).next_to(x_vec, DOWN).shift(UP*0.2)
        y = Text("y").scale(0.25).next_to(y_vec, LEFT).shift(RIGHT*0.2)
        self.add(pfaffian0,pfaffian1,pfaffian2, x, y, x_vec, y_vec)
        self.play(FadeIn(rolling, rolling_txt, cspace))

class Chap2_46(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/car.png').scale(0.8).shift(DOWN+LEFT*1.3).shift(LEFT*2.3)
        rolling_txt = Text("A car on a plane.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"$q = \begin{pmatrix}\phi\\x\\y \end{pmatrix}$").scale(0.5).next_to(rolling, LEFT).shift(UP*1.4)
        x_vec = Vector().move_to(rolling, aligned_edge=LEFT).shift(LEFT+DOWN)
        y_vec = Vector(UP).move_to(rolling, aligned_edge=LEFT).shift(LEFT*1.1+DOWN*0.5)
        x = Text("x").scale(0.25).next_to(x_vec, DOWN).shift(UP*0.2)
        y = Text("y").scale(0.25).next_to(y_vec, LEFT).shift(RIGHT*0.2)
        self.add(pfaffian0,pfaffian1,pfaffian2, x, y, x_vec, y_vec, rolling, rolling_txt, cspace)

        y_dot = Tex(r"$\dot{y} = v sin(\phi)$").scale(0.5).shift(UP*0.3)
        x_dot = Tex(r"$\dot{x} = v cos(\phi)$").scale(0.5).next_to(y_dot, DOWN).align_to(y_dot, LEFT)
        self.play(FadeIn(x_dot, y_dot))

class Chap2_47(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/car.png').scale(0.8).shift(DOWN+LEFT*1.3).shift(LEFT*2.3)
        rolling_txt = Text("A car on a plane.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"$q = \begin{pmatrix}\phi\\x\\y \end{pmatrix}$").scale(0.5).next_to(rolling, LEFT).shift(UP*1.4)
        x_vec = Vector().move_to(rolling, aligned_edge=LEFT).shift(LEFT+DOWN)
        y_vec = Vector(UP).move_to(rolling, aligned_edge=LEFT).shift(LEFT*1.1+DOWN*0.5)
        x = Text("x").scale(0.25).next_to(x_vec, DOWN).shift(UP*0.2)
        y = Text("y").scale(0.25).next_to(y_vec, LEFT).shift(RIGHT*0.2)
        y_dot = Tex(r"$\dot{y} = v sin(\phi)$").scale(0.5).shift(UP*0.3)
        x_dot = Tex(r"$\dot{x} = v cos(\phi)$").scale(0.5).next_to(y_dot, DOWN).align_to(y_dot, LEFT)
        self.add(pfaffian0,pfaffian1,pfaffian2, x, y, x_vec, y_vec, rolling, rolling_txt, cspace, x_dot, y_dot)

        y_dot = Tex(r"$\rightarrow v = \frac{\dot{y}}{sin(\phi)}$").scale(0.5).shift(UP*0.3).next_to(y_dot, RIGHT)
        x_dot = Tex(r"$= \frac{\dot{y}}{sin(\phi)}cos(\phi)$").scale(0.5).next_to(y_dot, DOWN).next_to(x_dot, RIGHT)
        self.play(FadeIn(x_dot, y_dot))
class Chap2_48(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/car.png').scale(0.8).shift(DOWN+LEFT*3.6)
        rolling_txt = Text("A car on a plane.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"$q = \begin{pmatrix}\phi\\x\\y \end{pmatrix}$").scale(0.5).next_to(rolling, LEFT).shift(UP*1.4)
        x_vec = Vector().move_to(rolling, aligned_edge=LEFT).shift(LEFT+DOWN)
        y_vec = Vector(UP).move_to(rolling, aligned_edge=LEFT).shift(LEFT*1.1+DOWN*0.5)
        x = Text("x").scale(0.25).next_to(x_vec, DOWN).shift(UP*0.2)
        y = Text("y").scale(0.25).next_to(y_vec, LEFT).shift(RIGHT*0.2)
        y_dot = Tex(r"$\dot{y} = v sin(\phi) \rightarrow v = \frac{\dot{y}}{sin(\phi)}$").scale(0.5).shift(UP*0.3+RIGHT*0.7)
        x_dot = Tex(r"$\dot{x} = v cos(\phi) = \frac{\dot{y}}{sin(\phi)}cos(\phi)$").scale(0.5).next_to(y_dot, DOWN).align_to(y_dot, LEFT)
        self.add(pfaffian0,pfaffian1,pfaffian2, x, y, x_vec, y_vec, rolling, rolling_txt, cspace, x_dot, y_dot)

        x_dot = Tex(r"$\rightarrow \dot{x} sin (\phi) - \dot{y}cos(\phi) = 0$").scale(0.5).next_to(x_dot, RIGHT)
        
        self.play(FadeIn(x_dot))

class Chap2_49(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/car.png').scale(0.8).shift(DOWN+LEFT*3.6)
        rolling_txt = Text("A car on a plane.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"$q = \begin{pmatrix}\phi\\x\\y \end{pmatrix}$").scale(0.5).next_to(rolling, LEFT).shift(UP*1.4)
        x_vec = Vector().move_to(rolling, aligned_edge=LEFT).shift(LEFT+DOWN)
        y_vec = Vector(UP).move_to(rolling, aligned_edge=LEFT).shift(LEFT*1.1+DOWN*0.5)
        x = Text("x").scale(0.25).next_to(x_vec, DOWN).shift(UP*0.2)
        y = Text("y").scale(0.25).next_to(y_vec, LEFT).shift(RIGHT*0.2)
        y_dot = Tex(r"$\dot{y} = v sin(\phi) \rightarrow v = \frac{\dot{y}}{sin(\phi)}$").scale(0.5).shift(UP*0.3+RIGHT*0.7)
        x_dot = Tex(r"$\dot{x} = v cos(\phi) = \frac{\dot{y}}{sin(\phi)}cos(\phi) \rightarrow \dot{x} sin (\phi) - \dot{y}cos(\phi) = 0$").scale(0.5).next_to(y_dot, DOWN).align_to(y_dot, LEFT)
        self.add(pfaffian0,pfaffian1,pfaffian2, x, y, x_vec, y_vec, rolling, rolling_txt, cspace, x_dot, y_dot)

        pfa_dot = Tex(r"$A(q)\dot{q} = \begin{pmatrix}0 & sin(\phi) & cos(\phi)\end{pmatrix} \cdot \begin{pmatrix}\dot{\phi}\\\dot{x}\\\dot{y} \end{pmatrix} = 0$").scale(0.5).next_to(x_dot, DOWN).shift(RIGHT*0.5+DOWN*0.2)
        
        pfaffian = ImageMobject('../images/pfafian.png').scale(0.4).next_to(pfa_dot, LEFT)

        self.play(FadeIn(pfa_dot, pfaffian))

class Chap2_410(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/rolling.png').scale(1).shift(DOWN+LEFT*1.3).shift(LEFT*2.3)
        rolling_txt = Text("A coin rolling on a plane without slipping.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"C-space: $\mathbb{R}^2\times\mathbb{T}^2$", color=RED).scale(0.5).next_to(rolling, LEFT).shift(UP*1.4+RIGHT*1.5)
        self.add(pfaffian0,pfaffian1,pfaffian2)
        self.play(FadeIn(rolling, rolling_txt, cspace))

class Chap2_411(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.4: Configuration and Velocity Constraints", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        pfaffian0 = Text(r"If pfaffian constraints can NOT be integrated to equivalent configuration constraints, they are ").scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*0.7)
        pfaffian1 = Text(r"non-holonomic.", color=RED ).scale(0.3).next_to(pfaffian0, RIGHT).shift(LEFT*0.15+UP*0.02)
        pfaffian2 = Text(r"They reduce the dimension of the feasible velocities, but not the dimension of the C-space.", color=GREEN).scale(0.3).next_to(pfaffian0, DOWN).align_to(pfaffian0, LEFT)

        rolling = ImageMobject('../images/rolling.png').scale(1).shift(DOWN+LEFT*1.3).shift(LEFT*2.3)
        rolling_txt = Text("A coin rolling on a plane without slipping.", color=BLUE).scale(0.25).next_to(rolling, DOWN)
        cspace = Tex(r"C-space: $\mathbb{R}^2\times\mathbb{T}^2$", color=RED).scale(0.5).next_to(rolling, LEFT).shift(UP*1.4+RIGHT*1.5)
        self.add(pfaffian0,pfaffian1,pfaffian2, rolling, rolling_txt, cspace)


        direction = ImageMobject('../images/direction.png').scale(1).next_to(rolling, RIGHT).shift(UP*1.5+LEFT*0.4)
        speed = ImageMobject('../images/speed.png').scale(1).next_to(direction, DOWN).align_to(direction, LEFT).shift(UP*0.2)
        collect = ImageMobject('../images/collect.png').scale(1).next_to(speed, DOWN).align_to(speed, LEFT).shift(UP*0.2)
        integrable = ImageMobject('../images/integrable.png').scale(1).next_to(collect, DOWN).align_to(collect, LEFT).shift(UP*0.2)

        self.play(FadeIn(direction, speed, collect, integrable))

      
class Chap2_50(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.5: Task Space and Workspace", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        task_space0 = Text("The task space is a space in which the robot’s task can be naturally expressed.").scale(0.3).shift(UP*1.5+LEFT*2)
        task_space1 = Text("For example, if the task is to control the position of the tip of a marker on a board, then task space is the Euclidean plane.").scale(0.3).next_to(task_space0, DOWN).align_to(task_space0, LEFT)
        task_space2 = Text(" You only have to know about the task, not the robot, to define the task space.").scale(0.3).next_to(task_space1, DOWN).align_to(task_space1, LEFT)

        task = ImageMobject('../images/task.jpg').shift(DOWN)

        self.play(FadeIn(task_space0, task_space1, task_space2, task))

class Chap2_51(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.5: Task Space and Workspace", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        task_space0 = Text("The workspace is a specification of the configurations that the end-effector of the robot can reach.").scale(0.3).shift(UP*1.5+LEFT)
        task_space1 = Text("It has nothing to do with a particular task.").scale(0.3).next_to(task_space0, DOWN).align_to(task_space0, LEFT)
        task_space2 = Text("For example, a planar robot with 2 revolute joints, limited to ranges of motion of 180 and 150 degrees, has the workspace:").scale(0.3).next_to(task_space1, DOWN).align_to(task_space1, LEFT)

        task = ImageMobject('../images/workspace.png').shift(DOWN*1.7).scale(0.6)

        self.play(FadeIn(task_space0, task_space1, task_space2, task))

class Chap2_52(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.5: Task Space and Workspace", color=BLUE).next_to(title, DOWN).scale(0.4)
        img_title = Text("The SCARA robot", color=YELLOW).next_to(secondary_title, DOWN).scale(0.3)
        
        self.add(title, secondary_title, img_title)
        
        
         #include video
        cap = cv2.VideoCapture("../media/videos/scara_cut.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.5).next_to(img_title, DOWN)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()


      
class Chap2_53(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.5: Task Space and Workspace", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        task_space0 = Tex(r"The SCARA robot is an RRRP open chain that is widely used for tabletop pick-and-place tasks.").scale(0.5).shift(UP*1.5+LEFT*2)
        task_space1 = Tex(r"The end-effector configuration is described by the four parameters $(x, y, z, \phi)$.").scale(0.5).next_to(task_space0, DOWN).align_to(task_space0, LEFT)
        task_space2 = Tex(r"Task space: $\mathbb{R}^3 \times \mathbb{S}^1$").scale(0.5).next_to(task_space1, DOWN).align_to(task_space1, LEFT)
        task_space3 = Tex(r"The workspace is defined as the EE reachable points in (x, y, z) Cartesian space, since all orientations can be achieved").scale(0.5).next_to(task_space2, DOWN).align_to(task_space2, LEFT)
        frame_img = ImageMobject("../images/scara.png").scale(0.66).shift(RIGHT*4+DOWN)
        self.play(FadeIn(frame_img, task_space0, task_space1, task_space2, task_space3))
      

class Chap2_54(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 2: Configuration Space").shift(UP*3).scale(0.65)
        secondary_title = Text("2.5: Task Space and Workspace", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)
        
        task_space0 = Text(r"The task space and workspace relate to configuration of the EE and are distinct from the robot’s C-space.").scale(0.3).shift(UP*1.5)
        task_space1 = Text(r"Some points in the task space may not be reachable at all by the robot").scale(0.3).next_to(task_space0, DOWN).align_to(task_space0, LEFT)
        task_space20 = Text(r"All points in the workspace are reachable by at least one configuration of the robot.").scale(0.3).next_to(task_space1, DOWN).align_to(task_space1, LEFT)         
        task_space2 = Text(r"A point in the task space or the workspace may be achievable by more than one robot configuration.").scale(0.3).next_to(task_space20, DOWN).align_to(task_space1, LEFT)
        task_space3 = Text(r"Some freedoms of the EE (for ex. orientation), do not have to be represented for the task and workspace.").scale(0.3).next_to(task_space2, DOWN).align_to(task_space2, LEFT)
        task_space4 = Text(r"Two mechanisms with the same C-space may also have diferent workspaces.").scale(0.3).next_to(task_space3, DOWN).align_to(task_space2, LEFT)
        
        
        cspace_a = ImageMobject("../images/cspace_a.png").scale(0.66).next_to(task_space4, DOWN).shift(LEFT)
        cspace_c = ImageMobject("../images/cspace_c.png").scale(0.66).next_to(cspace_a, RIGHT).shift(RIGHT*2)
        
        
        
        self.play(FadeIn(task_space0,task_space20, task_space1, task_space2, task_space3, task_space4, cspace_a, cspace_c))
      
      
