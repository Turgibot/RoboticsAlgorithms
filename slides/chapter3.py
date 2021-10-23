from math import e
from cv2 import FILLED, FastFeatureDetector
from numpy import WRAP
from OPU import *
from manim_slide import MyBullets
import random
class Empty(OPU_Slide):
    def construct(self):
        self.add_info()
        self.wait()
        
class Chap3_00(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("In this chapter we will ...", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/bluebot.jpg').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r" Learn the mathematical description of rigidbody configuration, rotation, velocity and forces.")
        bullets+= Text(r"Adopt the usage of an implicit representation.")
        bullets+= Text(r"Attach a reference frame to a rigid body as the origin of its 3 axis space (or 2 in 2d).")
        bullets+= Text(r"Use the right hand rule.")
        
        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)

        self.play(FadeIn(title, secondary_title, blist, img))

class Chap3_01(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("The right hand rule", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/right.png').scale(1.2)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r" Learn the mathematical description of rigidbody configuration, rotation, velocity and forces.")
        bullets+= Text(r"Adopt the usage of an implicit representation.")
        bullets+= Text(r"Attach a reference frame to a rigid body as the origin of its 3 axis space (or 2 in 2d).")
        bullets+= Text(r"Use the right hand rule.")
        
        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)

        self.play(FadeIn(title, secondary_title, img))


class Chap3_10(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/planar_rot.png').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
      
        
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.play(FadeIn(title, secondary_title, blist, img))


class Chap3_11(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/planar_rot.png').scale(0.99).shift(DOWN*1.3)
        img_txt = Text("What is the configuration of an object = Where is it?.").scale(0.3).next_to(img, DOWN)
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist, img)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )

        self.play(Write(trans), Write(rot))


class Chap3_12(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        p = self.add_vector(target, animate=False, stroke_width=2).move_to(number_plane.c2p(0,0)+UP*(target[1]/target[0])+RIGHT*0.5*(target[0]/target[1]))
        p_label = Text("p", color=YELLOW).scale(0.33).next_to(p, DOWN).shift(UP*0.55)
        self.add(p_label)
        
        self.add(number_plane, p, p_label)
        fixedFrame = self.add_frame(position=number_plane.get_origin())
        bodyFrame = self.add_frame('b', number_plane.get_origin()+[2,1,0], 60)

        all = VGroup(number_plane, p, fixedFrame, bodyFrame, p_label)
        all.scale(0.75).shift(DOWN)
        self.wait()

class Chap3_13(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        # b_co = self.vector_to_coords(b)
        
        self.add(number_plane)
        fixedFrame = Dot(point=number_plane.get_origin(), color=RED)
        s = Text("{s}", color=RED).scale(0.33).next_to(fixedFrame, DOWN).shift(UP*0.15+LEFT*0.2)

        bodyFrame = Dot(point=number_plane.get_origin()+[2,1,0], color=BLUE)
        b = Text("{b}", color=BLUE).scale(0.33).next_to(bodyFrame, DOWN).shift(UP*0.15+RIGHT*0.2)

        self.add(fixedFrame, bodyFrame,s,b)
        p = self.add_vector(target, animate=False, stroke_width=2).move_to(number_plane.c2p(0,0)+UP*(target[1]/target[0])+RIGHT*0.5*(target[0]/target[1]))
        p_label = Text("p", color=YELLOW).scale(0.33).next_to(p, DOWN).shift(UP*0.55)
        self.add(p_label)
        all = VGroup(number_plane, fixedFrame, bodyFrame,p, p_label, s, b)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        self.play(Write(p_tex))
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.play(Write(p_mat))
        self.wait()

class Chap3_14(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        # b_co = self.vector_to_coords(b)
        
        self.add(number_plane)
     
        fixedFrame = self.add_frame(position=number_plane.get_origin(), name="s")

        all = VGroup(number_plane, fixedFrame)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)

        self.wait()

class Chap3_15(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        # b_co = self.vector_to_coords(b)
        
        self.add(number_plane)
     
        fixedFrame = self.add_frame(position=number_plane.get_origin(), name="s")

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)
        self.remove(bodyFrame)

        all = VGroup(number_plane, fixedFrame, bodyFrame)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.play(ReplacementTransform(fixedFrame, bodyFrame))
        self.play(Create(arc), Write(theta))

        self.wait()

class Chap3_16(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        # b_co = self.vector_to_coords(b)
        
        self.add(number_plane)
     

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)

        all = VGroup(number_plane, bodyFrame)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)

        fig = ImageMobject("../images/P.png").scale(1.2).next_to(rot, DOWN)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.add(arc,theta)
        self.wait()
        self.play(FadeIn(fig))


class Chap3_17(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Given a fixed frame {s} and a body frame {b} as shown in the figure.")
        bullets+= Text(r"How would you describe the configuration of planar body in respect to {s} ?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*4 )
        rot = Text("Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(trans,rot)

        number_plane = NumberPlane( 
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        
        # b = self.add_vector_to_frame(start=number_plane.c2p(0,0,0), end=number_plane.c2p(2,1,0), color=YELLOW)
        target = [2,1]
        # b_co = self.vector_to_coords(b)
        
        self.add(number_plane)
     

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)

        all = VGroup(number_plane, bodyFrame)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)

        fig = ImageMobject("../images/R.png").scale(1.2).next_to(rot, DOWN)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.add(arc,theta)
        trans2 = Text("Rotation & Translation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.play(ReplacementTransform(rot, trans2))
        self.play(FadeIn(fig))
        self.wait()

