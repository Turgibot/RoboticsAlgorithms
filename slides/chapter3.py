from math import e
from cv2 import FILLED, FastFeatureDetector
from numpy import WRAP, right_shift
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )

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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        fixedFrameCopy = self.add_frame(position=number_plane.get_origin(), name="s")
        fixedFrame.set_opacity(0.5)
        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)
        self.remove(bodyFrame)

        all = VGroup(number_plane, fixedFrame, bodyFrame, fixedFrameCopy)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.play(ReplacementTransform(fixedFrameCopy, bodyFrame))
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        fixedFrame.set_opacity(0.5)

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)

        all = VGroup(number_plane, bodyFrame, fixedFrame)
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
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*4 )
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
        fixedFrame.set_opacity(0.5)

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)

        all = VGroup(number_plane, bodyFrame, fixedFrame)
        all.scale(0.75).shift(DOWN)
        
        p_tex = Tex(r"$p=p_x\hat{x}_s+p_y\hat{y}_s$").scale(0.5).next_to(trans, DOWN)
        p_mat = Tex(r"$p=\begin{bmatrix}p_x\\p_y\end{bmatrix}$").scale(0.5).next_to(p_tex,DOWN)
        self.add(p_mat,p_tex)

        fig = ImageMobject("../images/R.png").scale(1.2).next_to(rot, DOWN)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.add(arc,theta)
        trans2 = Text("Translation & Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.play(ReplacementTransform(rot, trans2))
        self.play(FadeIn(fig))
        self.wait()

class Chap3_18(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"We Used 4 parameters to describe the rotation.")
        bullets+= Text(r"What's the actual DOF of the rotation?")
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist)

        rot = Text("Translation & Rotation", color=RED).scale(0.3).shift(RIGHT*4 )
        self.add(rot)

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
        fixedFrame.set_opacity(0.5)

        bodyFrame = self.add_frame('b', number_plane.get_origin(), 60)

        all = VGroup(number_plane, bodyFrame, fixedFrame)
        all.scale(0.75).shift(DOWN)
       

        fig = ImageMobject("../images/R.png").scale(1.2).next_to(rot, DOWN)
        arc =  Arc(radius=2,angle=60*DEGREES, color=GREEN, stroke_width=2).scale(0.15).move_to(number_plane.get_origin()+[0.2,0.12,0])
        theta = Tex(r"$\theta$", color=GREEN).scale(0.33).move_to(number_plane.get_origin()+[0.16,0.1,0])
        self.add(arc,theta,fig)
       
        const = Text("Rotation Constraints", color=RED).scale(0.3).shift(LEFT*4 )
        self.play(Write(const))

        p_tex = Tex(r"$||\hat{x}||= 1$\\$||\hat{y}||= 1$").scale(0.5).next_to(const, DOWN)
        self.play(Write(p_tex))
        p_mat = Tex(r"$\hat{x}\cdot\hat{y}=0$").scale(0.5).next_to(p_tex,DOWN)
        self.play(Write(p_mat))
        dof = Tex(r"$dof_{rotation} = |Cspace| - |constraints| = 4 - 3 = 1$", color=BLUE).scale(0.4).next_to(p_mat,DOWN).shift(0.5*DOWN)
        self.play(Write(dof))
        self.wait()


class Chap3_19(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.1: Rigid-Body Motions in the Plane", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"Section 3.1 shows ...")
        bullets+= Text(r"how to represent a 2D configuration of a rigid body in {s}")
        bullets+= Text(r"how to change the reference frame in which a 2D vector or frame is represented")
        bullets+= Text(r"how to displace a 2D vector or a frame")
        bullets+= Text(r"an example of 2D screw motion and twist")
        bullets+= Text(r"We will cover it in 3D in section 3.2")
        blist = MyBullets(latex_grp=bullets, size=6).scale(0.27)

        self.add(title, secondary_title, blist)

        img = ImageMobject('../images/3drot.png').scale(0.8).shift(DOWN*1.7+RIGHT*3)
        self.add(img)
        self.wait()


class Chap3_210(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1: Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"There are three major uses for a 3x3 rotation matrix R:")
        bullets+= Text(r"represent an orientation")
        bullets+= Text(r"to change the reference frame in which a vector or a frame is represented")
        bullets+= Text(r"to rotate a vector or a frame")

        blist = MyBullets(latex_grp=bullets, size=4).scale(0.27).shift(UP)
        img = ImageMobject('../images/fullR.png').scale(0.99).shift(DOWN*1.3)
        r = Text("R").scale(0.5).next_to(img, LEFT)

        self.add(title, secondary_title, blist, img, r)

       
        self.wait()

class Chap3_211(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1: Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"We Used 9 parameters to describe the rotation.", color=RED)
        bullets+= Text(r"What's the actual DOF of the rotation?", color=RED)
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        img = ImageMobject('../images/fullR.png').scale(0.99).shift(DOWN*1.3)
        r = Text("R").scale(0.5).next_to(img, LEFT)

        self.add(title, secondary_title, blist, img, r)

       
        self.wait()


class Chap3_212(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1: Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
 
        bullets = VGroup()
        bullets+= Text(r"We Used 9 parameters to describe the rotation.", color=RED)
        bullets+= Text(r"What's the actual DOF of the rotation?", color=RED)
        blist = MyBullets(latex_grp=bullets, size=2).scale(0.27).shift(UP)

        img = ImageMobject('../images/fullR.png').scale(0.99).shift(DOWN*1.3)
        r = Text("R").scale(0.5).next_to(img, LEFT)
        img = Group(r, img)

        imgcopy = img.copy().shift(UP*2.75).scale(0.8)

        self.add(title, secondary_title, blist, img)
        
        self.play(FadeOut(blist), ReplacementTransform(img, imgcopy))
       

        img = ImageMobject('../images/full_cons.png').scale(0.99).shift(DOWN*1.3)
        self.play(FadeIn(img))
        self.wait()


class Chap3_213(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1: Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img = ImageMobject('../images/so.png').scale(1.2).shift(DOWN*0.3)
        self.play(FadeIn(img))
        self.wait()

class Chap3_214(OPU_Slide, VectorScene):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.1: Properties of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img0 = ImageMobject('../images/grp0.png')
        img1 = ImageMobject('../images/prp0.png').next_to(img0, DOWN)
        img2 = ImageMobject('../images/prp1.png').next_to(img1, DOWN).shift(LEFT*0.06)
        img3 = ImageMobject('../images/prp3.png').next_to(img2, DOWN).shift(RIGHT*0.06)
        img4 = ImageMobject('../images/prp2.png').next_to(img3, DOWN)
        img=Group(img0, img1, img2, img3, img4).scale(1.1).shift(UP*0.6)
        self.play(FadeIn(img))
        self.wait()


class Chap3_215(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)
        self.play(FadeIn(img))

        trans = Text("Translation", color=RED).scale(0.3).shift(LEFT*3 +DOWN )
        rot = Text("Orientation", color=RED).scale(0.3).shift(RIGHT*3 +DOWN)
        self.add(trans,rot)
        rot0 = ImageMobject('../images/3rot.png').next_to(rot, DOWN)
        trans0 = ImageMobject('../images/3loc.png').next_to(trans, DOWN)

        self.play(FadeIn(rot0, trans0))
        self.wait()


class Chap3_216(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)

        rec = Rectangle(color=BLACK, width=2, fill_color=BLACK, fill_opacity=1).shift(UP*0.7)
        self.add(img)



        rot_title = Text("Representing an orientation", color=RED).scale(0.3).shift(DOWN)
        self.add(rot_title)
        rot0 = ImageMobject('../images/rep.png').next_to(rot_title, DOWN)

        self.play(FadeIn(rot0, rec))

        # axes = ThreeDAxes()
        # arrow = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, arrow)
        self.wait()

class Chap3_217(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)
        self.add(img)
        chang = Tex(r"Changing the reference frame", color=RED).scale(0.5).shift(DOWN+2*LEFT)
        r_ab = Tex(r"let $R_{ab}$ represent the orientation of {b} in {a}", color=GREEN).scale(0.5).next_to(chang, DOWN).align_to(chang, LEFT)
        r_bc = Tex(r"let $R_{bc}$ represent the orientation of {c} in {b}", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)
        quest = Tex(r"How would you extract the orientation of {c} in {a}?", color=BLUE).scale(0.5).next_to(r_bc, DOWN).align_to(r_ab, LEFT)
        r_ac = Tex(r"$R_{ac} = R_{ab}R_{bc}$", color=BLUE).scale(0.5)
        
        self.play(FadeIn(chang.shift(LEFT),r_ab, r_bc, quest))
        self.wait()

class Chap3_218(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)
        chang = Tex(r"Changing the reference frame", color=RED).scale(0.5).shift(DOWN+2*LEFT)
        r_ab = Tex(r"let $R_{ab}$ represent the orientation of {b} in {a}", color=GREEN).scale(0.5).next_to(chang, DOWN).align_to(chang, LEFT)
        r_bc = Tex(r"let $R_{bc}$ represent the orientation of {c} in {b}", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)
        quest = Tex(r"How would you extract the orientation of {c} in {a}?", color=BLUE).scale(0.5).next_to(r_bc, DOWN).align_to(r_ab, LEFT)
        r_ac = Tex(r"$R_{ac} = R_{ab}R_{bc}$", color=BLUE).scale(0.5).next_to(quest, RIGHT)
        
        self.add(chang.shift(LEFT),r_ab, r_bc, quest, img)

        self.play(Write(r_ac))
        self.wait()

class Chap3_219(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)
        self.add(img)
        chang = Tex(r"Changing the reference frame", color=RED).scale(0.5).shift(DOWN+2*LEFT)
        r_ab = Tex(r"let $R_{ab}$ represent the orientation of {b} in {a}", color=GREEN).scale(0.5).next_to(chang, DOWN).align_to(chang, LEFT)
        r_bc = Tex(r"let $p_b$ represent the location of p in {b}", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)
        quest = Tex(r"How would you extract the location of p in {a}?", color=BLUE).scale(0.5).next_to(r_bc, DOWN).align_to(r_ab, LEFT)
        r_ac = Tex(r"$p_a = R_{ab}p_b$", color=BLUE).scale(0.5).next_to(quest, RIGHT)
        
        self.play(FadeIn(chang.shift(LEFT),r_ab, r_bc, quest))
        self.wait()

class Chap3_2120(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)


        img = ImageMobject('../images/3frames.png').scale(1.2).shift(UP*0.7)
        chang = Tex(r"Changing the reference frame", color=RED).scale(0.5).shift(DOWN+2*LEFT)
        r_ab = Tex(r"let $R_{ab}$ represent the orientation of {b} in {a}", color=GREEN).scale(0.5).next_to(chang, DOWN).align_to(chang, LEFT)
        r_bc = Tex(r"let $p_b$ represent the location of p in {b}", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)
        quest = Tex(r"How would you extract the location of p in {a}?", color=BLUE).scale(0.5).next_to(r_bc, DOWN).align_to(r_ab, LEFT)
        r_ac = Tex(r"$p_a = R_{ab}p_b$", color=BLUE).scale(0.5).next_to(quest, RIGHT)
        
        self.add(chang.shift(LEFT),r_ab, r_bc, quest, img)

        self.play(Write(r_ac))

       
        self.wait()

class Chap3_2121(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        chang = Tex(r"Rotating a vector or a frame", color=RED).scale(0.5).shift(UP+3.5*LEFT)

        img = ImageMobject('../images/rotw.png').scale(1.2).shift(UP)
        img1 = ImageMobject('../images/rotxt.png').next_to(img, DOWN)
        img2 = ImageMobject('../images/rotwt.png').next_to(img, DOWN)
        

        self.play(FadeIn(chang, img))
        self.wait()

class Chap3_2122(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        chang = Tex(r"Rotating a vector or a frame", color=RED).scale(0.5).shift(UP+3.5*LEFT)

        img = ImageMobject('../images/rotw.png').scale(1.2).shift(UP)
        img1 = ImageMobject('../images/rotxt.png').scale(1.2).next_to(img, DOWN)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        
        rec = Rectangle(color=BLACK, width=5, height=0.3, fill_color=BLACK, fill_opacity=1).move_to(img2.get_top()).shift(LEFT*1.55+DOWN*0.2)

        self.add(chang, img, img2, rec)
        self.wait()

class Chap3_2123(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        chang = Tex(r"Rotating a vector or a frame", color=RED).scale(0.5).shift(UP+3.5*LEFT)

        img = ImageMobject('../images/rot90.png').scale(1.2).shift(UP)
        img1 = ImageMobject('../images/rotxt.png').scale(1.2).next_to(img, DOWN).shift(DOWN*0.3)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        self.add(chang, img, img1)
        self.wait()

class Chap3_2124(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"Use the Rotation operator to\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rotxt.png').scale(1.2).next_to(img, DOWN).shift(DOWN*0.3)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        self.add(quest, img, r)
        self.wait()

class Chap3_2125(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"Use the Rotation operator to\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rels.png').scale(1.2).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        self.add(quest, img, img1, r)
        self.wait()

class Chap3_2126(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"Use the Rotation operator to\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rels.png').scale(1.2).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/relb.png').scale(1.2).next_to(img, RIGHT).shift(DOWN)
        self.add(quest, img, img1, img2, r)
        self.wait()


class Chap3_220(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.2: Angular Velocities", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"In this section we'll see how to respresent rotation using angular velocity", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/der.png').scale(1.2).shift(LEFT*2+DOWN*0.5)
        img1 = ImageMobject('../images/cross.png').scale(1.2).next_to(img, RIGHT)
        img2 = ImageMobject('../images/relb.png').scale(1.2).next_to(img, RIGHT).shift(DOWN)
        self.add(quest, img)
        self.wait()

class Chap3_221(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.2: Angular Velocities", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"In this section we'll see how to respresent rotation using angular velocity", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/der.png').scale(1.2).shift(LEFT*2+DOWN*0.5)
        img1 = ImageMobject('../images/cross.png').scale(1.2).next_to(img, RIGHT)
        img2 = ImageMobject('../images/crossall.png').scale(1.2).next_to(img1, RIGHT).shift(DOWN)
        self.add(quest, img, img1, img2)
        self.wait()

class Chap3_222(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.2: Angular Velocities", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        r_ab = Tex(r"Let $R(t)$ be the rotation matrix describing the orientation of the body frame with respect to the fixed frame at time t.", color=GREEN).scale(0.5).shift(UP*1.5)
        r_bc = Tex(r"let $w_s \in \mathbb{R}^3$ be the angular velocity w expressed in fixed-frame coordinates", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)

        img = ImageMobject('../images/cross.png').scale(1.2).shift(DOWN*0.5)
        img1 = ImageMobject('../images/wcr.png').scale(1.2).next_to(r_bc, DOWN).align_to(r_bc, LEFT)
        img2 = ImageMobject('../images/rdot.png').scale(1.2).next_to(img1, DOWN).align_to(r_bc, LEFT)
        self.add(r_ab, r_bc, img1, img2)
        self.wait()

class Chap3_223(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.2: Angular Velocities", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        r_ab = Tex(r"Let $R(t)$ be the rotation matrix describing the orientation of the body frame with respect to the fixed frame at time t.", color=GREEN).scale(0.5).shift(UP*1.5)
        r_bc = Tex(r"let $w_s \in \mathbb{R}^3$ be the angular velocity w expressed in fixed-frame coordinates", color=GREEN).scale(0.5).next_to(r_ab, DOWN).align_to(r_ab, LEFT)

        img = ImageMobject('../images/cross.png').scale(1.2).shift(DOWN*0.5)
        img1 = ImageMobject('../images/wcr.png').scale(1.2).next_to(r_bc, DOWN).align_to(r_bc, LEFT)
        img2 = ImageMobject('../images/rdot.png').scale(1.2).next_to(img1, DOWN).align_to(r_bc, LEFT)
        self.add(r_ab, r_bc, img1, img2)


        skew1 = Tex(r"The cross product is eliminated by using skew symetric matrix multiplication.", color=RED).scale(0.5).next_to(img2, DOWN).align_to(r_bc, LEFT)
        skew2 = Tex(r"$\dot{R} = w_s \times R = [w_s]R$").scale(0.4).next_to(skew1, DOWN).align_to(r_bc, LEFT)
        img3 = ImageMobject('../images/skew.png').scale(1.2).next_to(skew2, RIGHT).shift(RIGHT+DOWN*0.5)

        self.add(skew1, skew2, img3)
        self.wait()


class Chap3_224(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.2: Angular Velocities", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        skew0 = Tex(r"Some usuful properties:(see book for proff):", color=RED).scale(0.5).shift(LEFT*2+UP*1.5)
        skew1 = Tex(r"$R[w]R^T = [Rw]$").scale(0.5).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"$\dot{R} = [w_s]R$").scale(0.5).next_to(skew1, DOWN).align_to(skew1, LEFT)
        skew3 = Tex(r"$\dot{R}R^{-1} = [w_s]$").scale(0.5).next_to(skew2, DOWN).align_to(skew1, LEFT)
        skew4 = Tex(r"$w_s = R_{sb}w_b \rightarrow w_b = R_{sb}^{-1}w_s = R^{-1}w_s = R^Tw_s$").scale(0.5).next_to(skew3, DOWN).align_to(skew1, LEFT)
        img3 = ImageMobject('../images/prp5.png').scale(1.2).next_to(skew4, DOWN).align_to(skew1, LEFT)

        self.add(skew1, skew2, skew3, skew4, skew0, img3)
        self.wait()

class Chap3_2320(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/prot.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"$p(0)$ is rotated by $\theta$ about $\hat{w}$ to $p(\theta)$ :", color=GREEN).scale(0.5).shift(LEFT*2+UP*1.5)
        skew1 = Tex(r"Assume that: $\dot{\theta}=1rad/sec$, then  $w = \hat{w}\dot{\theta} = \hat{w}$", color=GREEN).scale(0.5).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"$\dot{p} = \hat{w}\times p$", color=RED).scale(0.5).next_to(skew1, DOWN)
        skew3 = Tex(r"$\dot{p} = [\hat{w}]p$", color=RED).scale(0.5).next_to(skew2, DOWN)
        skew4 = Tex(r"This is a linear differential equation of the form $\dot{x} = Ax$", color=GREEN).scale(0.5).next_to(skew3, DOWN).align_to(skew1, LEFT)
        skew5 = Tex(r"Its solution id given by:", color=GREEN).scale(0.5).next_to(skew4, DOWN).align_to(skew1, LEFT)
        skew51 = Tex(r"$p(t) = e^{[\hat{w}]t}p(0)$", color=RED).scale(0.5).next_to(skew5, RIGHT)
        skew6 = Tex(r"Change parameter and get:", color=GREEN).scale(0.5).next_to(skew5, DOWN).align_to(skew1, LEFT)
        skew61 = Tex(r" $p(\theta) = e^{[\hat{w}]\theta}p(0) = Rot(\hat{w}, \theta)$", color=RED).scale(0.5).next_to(skew6, RIGHT)

        self.add(skew1, skew2, skew3, skew0, img3)
        self.wait()


class Chap3_2321(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/prot.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"$p(0)$ is rotated by $\theta$ about $\hat{w}$ to $p(\theta)$ :", color=GREEN).scale(0.5).shift(LEFT*2+UP*1.5)
        skew1 = Tex(r"Assume that: $\dot{\theta}=1rad/sec$, then  $w = \hat{w}\dot{\theta} = \hat{w}$", color=GREEN).scale(0.5).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"$\dot{p} = \hat{w}\times p$", color=RED).scale(0.5).next_to(skew1, DOWN)
        skew3 = Tex(r"$\dot{p} = [\hat{w}]p$", color=RED).scale(0.5).next_to(skew2, DOWN)
        skew4 = Tex(r"This is a linear differential equation of the form $\dot{x} = Ax$", color=GREEN).scale(0.5).next_to(skew3, DOWN).align_to(skew1, LEFT)
        skew5 = Tex(r"Its solution id given by:", color=GREEN).scale(0.5).next_to(skew4, DOWN).align_to(skew1, LEFT)
        skew51 = Tex(r"$p(t) = e^{[\hat{w}]t}p(0)$", color=RED).scale(0.5).next_to(skew5, RIGHT)
        skew6 = Tex(r"Change parameter and get:", color=GREEN).scale(0.5).next_to(skew5, DOWN).align_to(skew1, LEFT)
        skew61 = Tex(r" $p(\theta) = e^{[\hat{w}]\theta}p(0) = Rot(\hat{w}, \theta)$", color=RED).scale(0.5).next_to(skew6, RIGHT)

        self.add(skew1, skew2, skew3, skew4, skew0, img3, skew5,skew51, skew61, skew6)
        self.wait()


class Chap3_2322(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/prot.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"The Rodrigues’ formula for rotations:", color=GREEN).scale(0.5).shift(LEFT*2+UP*1.5)
        skew1 = Tex(r"$Rot(\hat{w}, \theta) = e^{[\hat{w}]\theta} = I + sin\theta[\hat{w}] + (1-cos\theta)[\hat{w}]^2$", color=BLUE).scale(0.5).next_to(skew0, DOWN)
        skew2 = Tex(r"$R' = Rot(\hat{w}, \theta)R$", color=RED).scale(0.5).shift(DOWN+LEFT*4)
        skew21 = Tex(r"is the orientation achieved by the rotation R by $\theta$ about the axis $\hat{w}$ in the fixed frame", color=GREEN).scale(0.5).next_to(skew2, RIGHT).shift(DOWN*0.12)
        skew3 = Tex(r"$R'' = R Rot(\hat{w}, \theta)$", color=RED).scale(0.5).shift(DOWN*1.8+LEFT*4)
        skew31 = Tex(r"is the orientation achieved by the rotation R by $\theta$ about the axis $\hat{w}$ in the body frame", color=GREEN).scale(0.5).next_to(skew3, RIGHT).shift(DOWN*0.12)
        

        self.add(skew1, skew2, skew3, skew0, img3, skew21, skew31)
        self.wait()


class Chap3_2323(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)

        self.add(skew1, skew2, skew3, skew0, img3)
        self.wait()

class Chap3_2324(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        img4 = ImageMobject('../images/sol32.png').scale(1.2).next_to(skew3, DOWN).shift(RIGHT*1.4)

        self.add(skew1, skew2, skew3, skew0, img3, img4)
        self.wait()

class Chap3_2325(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        skew4 = Tex(r"b) ${b}$ got rotated again by $\theta_2$ about a fixed frame axis $\hat{w}_1 \neq \hat{w}_1$", color=RED).scale(0.4).next_to(skew3, DOWN).align_to(skew0, LEFT)

        self.add(skew1, skew2, skew3, skew0, img3, skew4)
        self.wait()

class Chap3_2326(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        skew4 = Tex(r"b) ${b}$ got rotated again by $\theta_2$ about a fixed frame axis $\hat{w}_1 \neq \hat{w}_1$", color=RED).scale(0.4).next_to(skew3, DOWN).align_to(skew0, LEFT)
        skew5 = Tex(r"$R' = Rot(\hat{w}_2, \theta_2)R$", color=BLUE).scale(0.4).next_to(skew4, DOWN)
        self.add(skew1, skew2, skew3, skew0, img3, skew4, skew5)
        self.wait()

class Chap3_2327(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        skew4 = Tex(r"b) ${b}$ got rotated again by $\theta_2$ about a fixed frame axis $\hat{w}_1 \neq \hat{w}_1$", color=RED).scale(0.4).next_to(skew3, DOWN).align_to(skew0, LEFT)
        skew5 = Tex(r"c) same as b) but the rotation is about the body frame", color=RED).scale(0.4).next_to(skew4, DOWN).align_to(skew0, LEFT)
        self.add(skew1, skew2, skew3, skew0, img3, skew4, skew5)
        self.wait()


class Chap3_2328(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        skew4 = Tex(r"b) ${b}$ got rotated again by $\theta_2$ about a fixed frame axis $\hat{w}_1 \neq \hat{w}_1$", color=RED).scale(0.4).next_to(skew3, DOWN).align_to(skew0, LEFT)
        skew5 = Tex(r"c) same as b) but the rotation is about the body frame", color=RED).scale(0.4).next_to(skew4, DOWN).align_to(skew0, LEFT)
        skew6 = Tex(r"$R' = R Rot(\hat{w}_2, \theta_2)$", color=BLUE).scale(0.4).next_to(skew5, DOWN)
        self.add(skew1, skew2, skew3, skew0, img3, skew4, skew5, skew6)
        self.wait()


class Chap3_2330(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.3: Matrix Logarithm of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/explog.png').scale(1.5)
      
        self.add(img3)
        self.wait()


class Chap3_2331(OPU_Slide):
    def construct(self):
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.3: Matrix Logarithm of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img1 = ImageMobject('../images/alg0.png').shift(UP*0.4)
        img2 = ImageMobject('../images/alg1.png').next_to(img1, DOWN).shift(RIGHT*0.1)
      
        self.add(img2, img1)
        self.wait()

