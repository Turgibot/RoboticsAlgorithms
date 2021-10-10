from math import e
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

        solution0 = Tex(r"dof is the dimension of the C-space, toplogy is its shape", color = GREEN).scale(0.6).center().shift(UP*1.5)
        solution01 = Tex(r"Two C-spaces may have the same dof but differ in other ways.", color = GREEN).scale(0.6).next_to(solution0, DOWN)
        solution02 = Tex(r"The topology (“shape”) of a space is independent of how we represent it", color = GREEN).scale(0.6).next_to(solution01, DOWN)
        solution03 = Tex(r"Two spaces are topologically equivalent if one can be continuously deformed to the other without cutting or pasting.", color = GREEN).scale(0.6).next_to(solution02, DOWN)
        

        self.play(FadeIn(solution0, solution01, solution02, solution03))