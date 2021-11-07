from math import e
from colour import Color
from cv2 import FILLED, FastFeatureDetector
from numpy import WRAP, right_shift
from OPU import *
from manim_slide import MyBullets
import random
class Empty(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()
        self.wait()

class Chap3_00(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1: Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img = ImageMobject('../images/so.png').scale(1.2).shift(DOWN*0.3)
        self.play(FadeIn(img))
        self.wait()

class Chap3_214(OPU_Slide, VectorScene):
   def construct(self):
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
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
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"$R_{sb}$ represents frame {b} relative to {s}.\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rotxt.png').scale(1.2).next_to(img, DOWN).shift(DOWN*0.3)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        self.add(quest, img, r)
        self.wait()

class Chap3_2125(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"$R_{sb}$ represents frame {b} relative to {s}.\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rels.png').scale(1.2).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/rotwt.png').scale(1.2).next_to(img, DOWN)
        self.add(quest, img, img1, r)
        self.wait()

class Chap3_2126(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.1.2: Uses of Rotation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        quest = Tex(r"$R_{sb}$ represents frame {b} relative to {s}.\\ Rotate {b} by $\theta$ about a unit axis $\hat{w} = \hat{z}$", color=GREEN).scale(0.5).shift(UP*1.5)

        img = ImageMobject('../images/rotrelative.png').scale(1.2).shift(LEFT*2+DOWN*1.2)
        r = ImageMobject('../images/rrot.png').next_to(img, UP)
        img1 = ImageMobject('../images/rels.png').scale(1.2).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/relb.png').scale(1.2).next_to(img, RIGHT).shift(DOWN)
        self.add(quest, img, img1, img2, r)
        self.wait()


class Chap3_220(OPU_Slide):
   def construct(self):
        note = "  אז עד כה ראינו איך משתמשים במטריצת רוטציה. אם נסתכל מזוית שונה נוכל לתאר רוטציה אר כפונקציה של זמן. כלומר המסגרת מסתובבת סביב ציר דבליו ואחרי דלתא טי הסתובבה דלתא טטא מעלות. אם משאיפים את דלתא טי לאפס הרי מהגדרה מדובר בנגזרת של הזוית טטא  "
        self.create_note(note)
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
        note = "הוא בעצם השינוי של זוית הרוטציה כתלות בזמן. המהירות הזויותית אומגה - מוגדרת כווקטור המכפלה בין אומגה האט לטטא דוט. מכפלה קרטזית של המהירות הזויתית בצירי המסגרת תתן את וקטור המהירות הקווית האורטוגונלי לשני הווקטורים   "
        self.create_note(note)
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
        note = "אוקיי אז בהנתן מטריצת רוטציה כלשהי אר, ומהירות זויות דבליו . המהירות הלינארית של כל אחד מהצירים הוא אר אי (תוצאה של המכפלה הוקטורית של המהירות הזויות עם וקטור הציר) ושל המטריצה כולה הוא אר גדולה דוט. "
        self.create_note(note)
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
        note = "לחשב מכפלה וקטורית שכזאת בין וקטור למטריצה זאת עבודה קשה. למזלינו ניתן לבצע זאת באמצעות מכפלה בין שתי מטריצות כאשר את ניצור מוקטור המהירות הזויותית מטריצה סקיו סימטרית לפי התבנית שמופיעה פה"
        self.create_note(note)
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
        note = "הספר ממשיך ועוסק בפיתוח והוכחה של משוואות המתארות תכונות של מטריצה סקיו סימטרית ואת היחס המעניין בינה לבין המטריצה הופכית. חשבתי שיהיה נכון לשים לכם הכל במקום אחד למקרה שתתקלו בסוג של תרגילים בנושא הזה.  חשוב לציין שני דברים :\
            1. שניתן להפל על וקטור המהירות מטריצת רוטציה ובכך לשנות את מערכת היחוס שלו.\
                2. פרופוזישיון 3.9 מציינת שאם מכפילים את אר דוא באר מינוס אחד מימין מכפלים את הסק'יו סימטריק מטריקס של אומגה ביחיס למסגרת אס  ואילו אם מכפילים את אר מינוס אחד משמאל מקבלים את הסקיו סימטריק מטריקס שבה ציר הסיבוב הוא ביחס למסגרת הבודי -בי. "
        self.create_note(note)
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
        note = "אז אתם שואלים את עצמכם למה אנחנו צריכים את זה? ובכן מבלי לעשות ספויילר - אם אנחנו חושבים על זה - אם יש לי את המהירות כנגזרת של הזוית אני מסוגל לעשות אינטגרציה ולקבל ממנה רוטציה. וזה בדיוק מה שנראה בסעיף המאד חשוב הזה.\
            נסתכל על הנקודה פי שמסתובבת מסביב לאומגה טטא מעלות. \
                אם נניח שקצה השינוי של טטא הוא ראדיאן לשנייה - אז אומגה שווה לאומגה גג והמהירות שזה נע הוקטור פי הוא פי דוט ששווה לסקיו סימטריק של אומגה מוכפל בוקטור פי."
        self.create_note(note)
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
        skew61 = Tex(r" $p(\theta) = e^{[\hat{w}]\theta}p(0) = Rot(\hat{w}, \theta)p(0)$", color=RED).scale(0.5).next_to(skew6, RIGHT)

        self.add(skew1, skew2, skew3, skew0, img3)
        self.wait()


class Chap3_2321(OPU_Slide):
   def construct(self):
        note = "זוהי משוואה דיפרנציאלי לינארית מהצורה איקס דוט שווה לאיי איקס שהפתרון שלה הוא פי של טי = אי בחזקת סקיו של אומגה מוכפל בטי - האקפוננט מוכפל בוקטור ההתחלה פי של אפס.\
            נבצע החלפת פרמטרים ונקבל שאי בחזקת סקיו מוכפל בטטא שקול למטריצת הרוטציה סביב אומגה בטטא מעלות. זאת לא הוכחה - את ההוכחה והנכונות תוכלו למצוא בספר - . "
        self.create_note(note)
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
        skew61 = Tex(r" $p(\theta) = e^{[\hat{w}]\theta}p(0) = Rot(\hat{w}, \theta)p(0)$", color=RED).scale(0.5).next_to(skew6, RIGHT)

        self.add(skew1, skew2, skew3, skew4, skew0, img3, skew5,skew51, skew61, skew6)
        self.wait()


class Chap3_2322(OPU_Slide):
   def construct(self):
        note = "אם כך אומגה וטטא משמשות כקואורדינטות האקספוננציאליות המבטאות אופרטור רוטציה מתאים, שימו לב לחיסכון מכיון שמדובר ב3 ולא 9 פרמטרים - ספויילר אלרט בפרק הבאנראה כיצד החיסכון הזה בא לידי ביטוי שנבצע מכפלה של אקפוננטים. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/prot.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"The Rodrigues’ formula for rotations:", color=GREEN).scale(0.5).shift(LEFT*2+UP*0.4)
        skew1 = Tex(r"$Rot(\hat{w}, \theta) = e^{[\hat{w}]\theta} = I + sin\theta[\hat{w}] + (1-cos\theta)[\hat{w}]^2$", color=BLUE).scale(0.5).next_to(skew0, DOWN)
        skew2 = Tex(r"$R' = Rot(\hat{w}, \theta)R$", color=RED).scale(0.5).shift(DOWN+LEFT*4)
        skew21 = Tex(r"is the orientation achieved by the rotation R by $\theta$ about the axis $\hat{w}$ in the fixed frame", color=GREEN).scale(0.5).next_to(skew2, RIGHT).shift(DOWN*0.12)
        skew3 = Tex(r"$R'' = R Rot(\hat{w}, \theta)$", color=RED).scale(0.5).shift(DOWN*1.8+LEFT*4)
        skew31 = Tex(r"is the orientation achieved by the rotation R by $\theta$ about the axis $\hat{w}$ in the body frame", color=GREEN).scale(0.5).next_to(skew3, RIGHT).shift(DOWN*0.12)
        skew32 = Tex(r"The vector $\hat{w}\theta \in \mathbb{R}^3$ is the three-parameter exponential coordinate representation of the rotation", color=WHITE).scale(0.5).next_to(skew2, UP).align_to(skew2, LEFT).shift (UP*1.8)
        

        self.add(skew1, skew2, skew3, skew0, img3, skew21, skew31, skew32)
        self.wait()


class Chap3_2323(OPU_Slide):
   def construct(self):
        note = "בוא נסתכל על דוגמה 3.2 מהספר : פריים בי היא בעצם רוטציה של פריים אס סביב אומגה 1 בטטא שווה 30 מעלות. חשבו את מטריצת הרוטציה של בי.\
            הפתרון הוא פשוט להציב בנוסחת רודריגז"
        self.create_note(note)
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
        note = "מציבים את טטא ומייצרים את הסקיו סימטריק של אומגה ומחברים בין 3 המטריצות לקבלת מטריצת רוטציה סופית אר- אס בי"
        self.create_note(note)
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
        note = " בסעיף בי  - אנחנו נדרשים לסובב את בי שוב בטטא שתיים מעלות סביב ציר אומגה 2 ביחס לפיקסד פריים - אז כמובן שיש להכפיל אופרטור רוטציה סביב אומגה 2 מימין לאר "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.2: Exponential Coordinates of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/rod.png').scale(1.2).shift(UP*0.75+RIGHT*4)
        skew0 = Tex(r"Example 3.2:").scale(0.4).shift(LEFT*4.5+UP*1.5)
        skew1 = Tex(r"The frame ${b}$ is obtained by rotation from an initial orientation aligned with the", color=GREEN).scale(0.4).next_to(skew0, DOWN).align_to(skew0, LEFT)
        skew2 = Tex(r"fixed frame ${s}$ about a unit axis $\hat{w}_1 = (0, 0.866, 0.5)$ by an angle of $\theta_1=30=0.524rad$", color=GREEN).scale(0.4).next_to(skew1, DOWN).align_to(skew0, LEFT)
        skew3 = Tex(r"a) Calculate the rotation matrix representation of ${b}$", color=RED).scale(0.4).next_to(skew2, DOWN).align_to(skew0, LEFT)
        skew4 = Tex(r"b) ${b}$ got rotated again by $\theta_2$ about a fixed frame axis $\hat{w}_2 \neq \hat{w}_1$", color=RED).scale(0.4).next_to(skew3, DOWN).align_to(skew0, LEFT)

        self.add(skew1, skew2, skew3, skew0, img3, skew4)
        self.wait()

class Chap3_2326(OPU_Slide):
   def construct(self):
        note = " בסעיף בי  - אנחנו נדרשים לסובב את בי שוב בטטא שתיים מעלות סביב ציר אומגה 2 ביחס לפיקסד פריים - אז כמובן שיש להכפיל אופרטור רוטציה סביב אומגה 2 מימין לאר "
        self.create_note(note)
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
        note = "ואם הסיבוב הוא ביחס לבודי פריים - אז סדר ההכפלה משתנה"
        self.create_note(note)
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
        note = "וההכפלה היא כאשר האופרטור מימין לאר"
        self.create_note(note)
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
        note = "שאלות ? \
            אז ראינו שבעזרת נוסחת רודריג אפשר הגיע מקואורדינטות אקפוננציאליות למטריצת רוטציה. עכשיו נכיר פעולה הפוכה - היא הלוגריתם שבאמצעותה אפשר לקבל קואורדינטות אקפוננציאליות מתוך מטריצת רוטציה"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.3: Matrix Logarithm of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        self.add(title, secondary_title)

        img3 = ImageMobject('../images/explog.png').scale(1.5)
      
        self.add(img3)
        self.wait()



class Chap3_2331(OPU_Slide):
   def construct(self):
        note = "את הפיתוח המתמטי כדאי להכיר אבל הוא לא נכלל בחומר לבחינה. והאלגוריתם שלפנינו יחסית פשוט ומציג שלושה מקרים שונים אפשריים .\
            ניתן לקרוא ישירות מהאלגוריתם ולעקוב אחר ההוראות בו לקבלת אומגה וטטא."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.2.3.3: Matrix Logarithm of Rotations", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img1 = ImageMobject('../images/alg0.png').shift(UP*0.4)
        img2 = ImageMobject('../images/alg1.png').next_to(img1, DOWN).shift(RIGHT*0.1)
      
        self.add(img2, img1)
        self.wait()



#3.3.1

class Chap3_310(OPU_Slide):
   def construct(self):
        note = "עד כה דנו במטריצות רוטציה והגיע הזמן להשתדרג למטריצות טרנפורמציה שהן באמת כלי העבודה שלנו מהסיבה שמריצת רוטציה 4 על 4 היא שילוב של מטריצת רוטציה עם וקטור טרנסלציה - או הזזה. כדי לייצר מטריצה ריבועית יש לשים שלושה אפסים תחת הרוטציה ואחד תחת וקטור המיקום"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1: Homogeneous Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img1 = ImageMobject('../images/transf0.png').shift(UP*0.8)
        img2 = ImageMobject('../images/transf1.png').next_to(img1, DOWN)
      
        self.add(img2, img1)
        self.wait()


class Chap3_3110(OPU_Slide):
   def construct(self):
        note = "גם כאן מדובר בקבוצה המקיימת את תכונות הקבוצה - וגם לה יש אינברס שניתן לחשב אותו כך:\
            --- באותו אופן מכפלה בוקטור איקס תתן וקטור מסובב ומוזז. שימו לב שיש להוסיף אחד כדי להתאים מידות ולאפשר את פעולת המכפלה "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.1: Properties of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img1 = ImageMobject('../images/transfprop0.png').shift(UP*0.8)
        img2 = ImageMobject('../images/transfprop1.png').next_to(img1, DOWN).align_to(img1, LEFT).shift(DOWN)
      
        self.add(img2, img1)
        self.wait()


class Chap3_3120(OPU_Slide):
   def construct(self):
        note = "אנחנו עכשיו נראה כיצד משתמשים במטריצות טרנספורמציה בשביל : 1. לייצג קונפיגורציה של גוף קשיח (מיקום ואוריינטציה) 2. לשנות מסגרת ייחוס 3. להזיז וקטור או פריים "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        
        self.add(title, secondary_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        self.add(img1, img2)
        self.wait()

class Chap3_3121(OPU_Slide):
   def construct(self):
        note = " אז בואו נייצג קונפיגורציה באמצעות מטריצות טרנספורמציה - בהינתן המסגרות איי בי וסי והנקודה וי ביחס לבי - ניתן בשלב ראשון מניתוח ויזואלי לייצר מטריצות רוטציה כאשר נניח שמסגרת איי חופפת ומלוכדת עם הפיקסד פריים אס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        self.add(img2)

        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6+LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2)

        self.play(FadeOut(img2), imgs.animate().shift(UP*2.5))

        
        self.wait()

class Chap3_3122(OPU_Slide):
   def construct(self):
        note = "שלושת מטריצות הרוטציה מתארות את האוריינטציה של כל אחד מהמסגרות ביחס לאס. ושלושת הוקטורים את המיקום של כל אחד מהמסגרות בקואורדינטות של אס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6+LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').next_to(imgs, DOWN)
        self.play(FadeIn(img5))
        self.wait()

class Chap3_3123(OPU_Slide):
   def construct(self):
        note = "נעשה קצת מקום ונשאל את השאלה הבאה:"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6+LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').next_to(imgs, DOWN)
        self.add(img5)
        
        self.play(imgs.animate().shift(RIGHT*5), img5.animate().shift(UP*2))
        self.wait()



class Chap3_3124(OPU_Slide):
   def construct(self):
        note = "איך נייצג את מטריצת הטרנספורמציה טי אס סי?"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{sc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.play(FadeIn(quest))
        self.wait()


class Chap3_3125(OPU_Slide):
   def construct(self):
        note = "כפי שראינו יש למקם את מטריצת הרוטציה 3 על 3 משמאל כשמתחתיה שלולשה אפסים ואת וקטור המיקום מימין ומתחתיו המספר 1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{sc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$T_{sc} = $", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ \begin{bmatrix}R_{sc} & p_{sc} \\ 0 & 1 \end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)
        self.wait()


class Chap3_3126(OPU_Slide):
   def construct(self):
        note = "וכך נראית המטריצה עם הנתונים עצמם"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(a) Representation of configuration", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{sc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$T_{sc} = $", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ \begin{bmatrix}R_{sc} & p_{sc} \\ 0 & 1 \end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)

        tbc = Tex(r"$ = \begin{bmatrix}-1 & 0 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(tbs, RIGHT)
        self.add(tbc)
        self.wait()



class Chap3_3127(OPU_Slide):
   def construct(self):
        note = "ואם נרצה לשנות מסגרת ייחוס כלומר לייצג את הקונפיגורציה של סי מנקודת המבט של בי?"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{bc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.play(FadeIn(quest))
        self.wait()

class Chap3_3128(OPU_Slide):
   def construct(self):
        note = "אז העקרון שלמדנו ממכפלת מטריצות רוטציה מתקיים כמובן גם במטריצות טרנפורמציה וניתן להכפיל בין מטריצות לקבלת הטרנפורמציה הרצויה"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{bc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$T_{bc} = T_{bs}T_{sc} = (T_{sb})^{-1} T_{sc}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)
        self.wait()

class Chap3_3129(OPU_Slide):
   def construct(self):
        note = "שימו לב שהמטריצה האינברס מתארת את נקודת המבט ההפוכה אבל לא שקולה לטרנספוז  "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{bc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$T_{bc} = T_{bs}T_{sc} = (T_{sb})^{-1} T_{sc}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ = \begin{bmatrix}0 & 0 & 1 & 0 \\ 0 & -1 & 0 & -2 \\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}^{-1}$\
            $\begin{bmatrix}-1 & 0 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)
        self.wait()


class Chap3_31210(OPU_Slide):
   def construct(self):
        note = "אפשר להסתכל ולוודא שאכן קיבלנו טרנספורמציה תקינה "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $T_{bc}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$T_{bc} = T_{bs}T_{sc} = (T_{sb})^{-1} T_{sc}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ = \begin{bmatrix}0 & 0 & 1 & 0 \\ 0 & -1 & 0 & -2 \\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}^{-1}$\
            $\begin{bmatrix}-1 & 0 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)

        tbc = Tex(r"$ = \begin{bmatrix}0 & 1 & 0 & 0 \\ 0 & 0 & -1 & -3 \\ -1 & 0 & 0 & -1\\ 0 & 0 & 0 & 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(tbs, RIGHT)
        self.add(tbc)
        self.wait()



class Chap3_31211(OPU_Slide):
   def construct(self):
        note = "ואם אנחנו רוצים לתאר את הנקודה וי מנקודת המבט של אי?"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $v_{a}?$", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.play(FadeIn(quest))
        self.wait()

class Chap3_31212(OPU_Slide):
   def construct(self):
        note = "נכפיל במטריצת הטרנפסורמציה מאיי לבי"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $v_{a}$?", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$v_{a} = T_{ab}v_{b}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)
        self.wait()

class Chap3_31213(OPU_Slide):
   def construct(self):
        note = "מבחינת מידות המכפלה אפשרית"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $v_{a}$?", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$v_{a} = T_{ab}v_{b}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ = \begin{bmatrix}0 & 0 & 1 & 0 \\ 0 & -1 & 0 & -2 \\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$\
            $\begin{bmatrix}0 \\ 0 \\ 1.5\\ 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)
        self.wait()


class Chap3_31214(OPU_Slide):
   def construct(self):
        note = "ונקבל את הוקטור הזה - ניתן לבדוק ויזואליות ולראות שאכן ביחס לאיי וי נמצאת ב ...."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img1 = ImageMobject('../images/transfuses.png').shift(UP*0.8)
        img2 = ImageMobject('../images/threeref.png').next_to(img1, DOWN)
      
        img3 = ImageMobject('../images/threerefcut.png').shift(UP)
        img4 = ImageMobject('../images/vb.png').shift(UP*0.6 + LEFT*1.2)
        imgs = Group(img3, img4).move_to(img2).shift(UP*2.5 + RIGHT*5)

        self.add(imgs)
        
        img5 = ImageMobject('../images/transfall.png').shift(UP*0.4)
        self.add(img5)
        
        quest = Tex(r"How would you represent $v_{a}$?", color=RED).scale(0.4).next_to(img5, DOWN).shift(LEFT*4+DOWN*0.7)
        self.add(quest)
        ans0 = Tex(r"$v_{a} = T_{ab}v_{b}$", color=GREEN).scale(0.4).next_to(quest, RIGHT)
        self.add(ans0)

        tbs = Tex(r"$ = \begin{bmatrix}0 & 0 & 1 & 0 \\ 0 & -1 & 0 & -2 \\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\end{bmatrix}$\
            $\begin{bmatrix}0 \\ 0 \\ 1.5\\ 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(ans0, RIGHT)
        self.add(tbs)

        tbc = Tex(r"$ = \begin{bmatrix}1.5 \\ -2 \\ 0\\ 1\end{bmatrix}$", color=GREEN).scale(0.4).next_to(tbs, RIGHT)
        self.add(tbc)
        self.wait()



class Chap3_31215(OPU_Slide):
   def construct(self):
        note = "הספר משתמש בסאבסקריפט קאנסליישן רול שעוזר לזכור כיצד לבצע מכפלות בסדר הנכון."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(b) Change of refrence frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        img3 = ImageMobject('../images/transftac.png').scale(1.5)
      
        self.add(img3)
        self.wait()


class Chap3_31216(OPU_Slide):
   def construct(self):
        note = "אפשרות נוספת להזזה של מסגרת או וקטור היא הפרדה של פעולת הרוטציה מהטרנסלציה"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        t = Tex(r"$T = (R,p) = (Rot(\hat{w},\theta), p)$").scale(0.4).shift(UP*1.4)
      
        self.add(t)
        self.wait()


class Chap3_31217(OPU_Slide):
   def construct(self):
        note = "כלומר אם (משמאל) נאכלס את מטריצת הטרנספורמציה באפסים במקום בוקטור מיקום - נאפס את פעולת הטרנסלציה ויתקבל אופרטור רוטציה.\
            ואילו אם (מימין) במקום החלק של הרוטציה נשים את מטריצת היחידה יתקבל אופרטור טרנלציה בלבד."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        t = Tex(r"$T = (R,p) = (Rot(\hat{w},\theta), p)$").scale(0.4).shift(UP*1.4)
        img1 = ImageMobject('../images/rotwth.png').shift(LEFT*2+UP*0.5).scale(1.2)
        img2 = ImageMobject('../images/transfp.png').next_to(img1, RIGHT).shift(RIGHT*2).scale(1.2)
        self.add(t, img1, img2)
        self.wait()

class Chap3_31218(OPU_Slide):
   def construct(self):
        note = "שימו לב שמכפלה בין אופרטור טרנסלציה מימין לאופרטור רוטציה תתן חזרה את מטריצת הטרנספורמציה טי. יש כמובן לשמור על הסדר בין האופרטורים וניתן להשתמש בו כדי לקבוע האם הטרנספורמציה ביחס לפיקסד או לבודי פריים בדיוק כפי שראינו במקרים קודמים. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        self.add(title, secondary_title, mini_title)

        t = Tex(r"$T = (R,p) = (Rot(\hat{w},\theta), p)$").scale(0.4).shift(UP*1.4)
        img1 = ImageMobject('../images/rotwth.png').shift(LEFT*2+UP*0.5).scale(1.2)
        img2 = ImageMobject('../images/transfp.png').next_to(img1, RIGHT).shift(RIGHT*2).scale(1.2)
        img3 = ImageMobject('../images/whether.png').shift(DOWN*1.4)
        self.add(t, img1, img2, img3)
        self.wait()


class Chap3_31219(OPU_Slide):
   def construct(self):
        note = "בואו ניתן דגש על סדר ההכפלה. בהנתן טרנספורמציה טי סביב אומגה ב90 מעלות והזזה פי."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)
        self.wait()




class Chap3_31220(OPU_Slide):
   def construct(self):
        note = "וטרנספורמציה נוספת המתארת את הקונפיגורציה של בי ביחס לאס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)

        tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/transftsb.png').next_to(tsb, DOWN)

        self.add(tsb, img2)

        
        self.wait()

class Chap3_31221(OPU_Slide):
   def construct(self):
        note = "כשנתאר את הטרנספורמציה ביחס לפיקסד פריים - אפשר לתאר את הפעולות כרוטציה סביב אומגה ביחס לאס וולאחר מכן הזזה לפי וקטור פי גם לפי אס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)

        tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/transftsb.png').next_to(tsb, DOWN)

        self.add(tsb, img2)

        fixed = Tex(r"Fixed frame transformation $T_{sb}'$").scale(0.4).next_to(mini_title, RIGHT).shift(RIGHT*3)
        img3 = ImageMobject('../images/fixed.png').next_to(fixed, DOWN)
        img4 = ImageMobject('../images/fixedt.png').next_to(img3, DOWN)

        self.add(fixed, img3)
        self.wait()

class Chap3_31222(OPU_Slide):
   def construct(self):
        note = "וכאמור טרנפורמציה ביחס לפיקסד פריים היא הכפלה בין המטריצות כשטי היא משמאל (קרוב ל אס)"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)

        tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/transftsb.png').next_to(tsb, DOWN)

        self.add(tsb, img2)

        fixed = Tex(r"Fixed frame transformation $T_{sb}'$").scale(0.4).next_to(mini_title, RIGHT).shift(RIGHT*3)
        img3 = ImageMobject('../images/fixed.png').next_to(fixed, DOWN)
        img4 = ImageMobject('../images/fixedt.png').next_to(img3, DOWN)

        self.add(fixed, img3, img4)
        self.wait()

class Chap3_31223(OPU_Slide):
   def construct(self):
        note = "ובמקרה האחר כשמדברים על טרנפורמציה ביחס לבודי פריים ההזזה מתבצעת תחילה ביחס לבודי פריים ורק לאחר מכן הרוטציה  - גם היא ביחס לבודי פריים"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)

        tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/transftsb.png').next_to(tsb, DOWN)

        self.add(tsb, img2)

        fixed = Tex(r"Body frame transformation $T_{sb}''$").scale(0.4).next_to(mini_title, RIGHT).shift(RIGHT*3)
        img3 = ImageMobject('../images/body.png').next_to(fixed, DOWN)

        self.add(fixed, img3)
        self.wait()

class Chap3_31224(OPU_Slide):
   def construct(self):
        note = " סדר המכפלות הפוף - כלומר יש למקם את הטרנספורמציה טי מימין (קרוב לבי)"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("(c) Displacing a vector or a frame", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*4.2)
        question = Tex(r"Transformation T with $\hat{w} = (0,0,1)$, $\theta = 90 $ and $p = (0,2,0)$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img1 = ImageMobject('../images/tranfwz.png').next_to(question, DOWN)
        
        self.add(img1)

        tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/transftsb.png').next_to(tsb, DOWN)

        self.add(tsb, img2)

        fixed = Tex(r"Body frame transformation $T_{sb}''$").scale(0.4).next_to(mini_title, RIGHT).shift(RIGHT*3)
        img3 = ImageMobject('../images/body.png').next_to(fixed, DOWN)
        img4 = ImageMobject('../images/bodyt.png').next_to(img3, DOWN)

        self.add(fixed, img3, img4)
        self.wait()


class Chap3_31225(OPU_Slide):
   def construct(self):
        note = "בואו נעשה תרגיל לדוגמה מהספר - בהנתן הטרנפורמציות הבאות - איך תתארו את הקונפיגורציה של הקובייה אי ביחס לאנד אפקטור של הרובוט? "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("Example 3.19", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*5.5)
        question = Tex(r"Given these Transformation matrices:", color=BLUE).scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img0 = ImageMobject('../images/exe1.png').next_to(question, DOWN).scale(0.95)
        img1 = ImageMobject('../images/exe2.png').next_to(img0, DOWN).shift(RIGHT*0.2+UP*0.3).scale(0.95)
        
        self.add(img1, img0)

        # tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/exe0.png').next_to(img1, RIGHT).shift(UP*0.7+LEFT*0.5).scale(0.75)

        self.add(img2)

        fixed = Tex(r"Whats the configuration of object \{e\} in respect to the robot EE ?", color=RED).scale(0.4).next_to(question, RIGHT).shift(RIGHT)
        img3 = ImageMobject('../images/body.png').next_to(fixed, DOWN)
        img4 = ImageMobject('../images/bodyt.png').next_to(img3, DOWN)

        self.add(fixed)
        self.wait()

class Chap3_31226(OPU_Slide):
   def construct(self):
        note = "זהו הפתרון שמופיע בספר"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.1.2: Uses of Transformation Matrices", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Text("Example 3.19", color=GREEN).scale(0.3).next_to(secondary_title, DOWN).shift(LEFT*5.5)
        question = Tex(r"Given these Transformation matrices:", color=BLUE).scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)

        img0 = ImageMobject('../images/exe1.png').next_to(question, DOWN).scale(0.95)
        img1 = ImageMobject('../images/exe2.png').next_to(img0, DOWN).shift(RIGHT*0.2+UP*0.3).scale(0.95)
        
        self.add(img1, img0)

        # tsb = Tex(r"The frame $\{b\}$ represnted in frame $\{s\}$ by:").scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        img2 = ImageMobject('../images/exe0.png').next_to(img1, RIGHT).shift(UP*0.7+LEFT*0.5).scale(0.75)

        self.add(img2)

        fixed = Tex(r"Whats the configuration of object \{e\} in respect to the robot EE ?", color=RED).scale(0.4).next_to(question, RIGHT).shift(RIGHT)
        img3 = ImageMobject('../images/exe3.png').next_to(img2, RIGHT).scale(0.85).shift(UP*0.5+LEFT*0.56)
        img4 = ImageMobject('../images/exe5.png').next_to(img3, DOWN).scale(0.85)

        self.add(fixed, img3, img4)
        self.wait()


class Chap3_320(OPU_Slide):
   def construct(self):
        note = "אוקיי אז לפני נמשיך אני רוצה רגע לעשות לכם סדר. \
            בתחילת הפרק דיברנו על רוטציות ואז השתמשנו בפתרון של משוואה דיפרנציאלית המתארת מהירות זויתית כדי להגיע לייצוג אקספוננציאלי של רוטציה. החלק האחרון של הפרק גם הוא מדבר על ייצוג אקספוננציאלי אך של טרנספורמציה. \
                הוא מתחיל בהגדרה של טוויסט כוקטור בעל שישה מימדים שהשלושה העליונים הם המהירות הזויתית והשלושה התחתונים הם המהירות הלינארית של גוף קשיח."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2: Twists", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Tex(r"Twist is an $\mathbb{R}^6$ vector that describes the velocity of a rigid body").scale(0.4).next_to(secondary_title, DOWN)
        question = Tex(r"$V =\begin{bmatrix}w\\v\end{bmatrix}$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)
        w = Text("Angular velocity", color=GREEN).scale(0.25).next_to(question, RIGHT).shift(UP*0.15)
        v = Text("Linear velocity", color=GREEN).scale(0.25).next_to(question, RIGHT).shift(DOWN*0.15)
        self.add(w, v)
        self.wait()

class Chap3_321(OPU_Slide):
   def construct(self):
        note = "בדומה למה שראינו בהקשר לרוטציה - קיים קשר בין הטרנספורמציה לנגזרת שלה בכך שהמכפלה בינהם יוצרת ייצוג מטריציוני של טוויסט. גם פה סדר המכפלה מתאים לייצוג ביחס לפיקס או לבודי פריים. בשקף הבא יש סיכום של היחסים הללו:"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2: Twists", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        mini_title = Tex(r"Twist is an $\mathbb{R}^6$ vector that describes the velocity of a rigid body").scale(0.4).next_to(secondary_title, DOWN)
        question = Tex(r"$V =\begin{bmatrix}w\\v\end{bmatrix}$").scale(0.4).next_to(mini_title, DOWN).align_to(mini_title, LEFT)
        self.add(title, secondary_title, mini_title ,question)
        w = Text("Angular velocity", color=GREEN).scale(0.25).next_to(question, RIGHT).shift(UP*0.15)
        v = Text("Linear velocity", color=GREEN).scale(0.25).next_to(question, RIGHT).shift(DOWN*0.15)
        self.add(w, v)

        img0 = ImageMobject('../images/lett.png').next_to(question, DOWN).scale(1.15).align_to(question, LEFT)
        img1 = ImageMobject('../images/tt.png').next_to(img0, DOWN).scale(1.15).align_to(question, LEFT)

        this_is = Tex(r"This is the matrix representation of a BODY twist", color=RED).scale(0.4).next_to(img1, DOWN).align_to(mini_title, LEFT)
        self.add(img1, img0, this_is)

        self.wait()


class Chap3_322(OPU_Slide):
   def construct(self):
        note = "בהנתן טרנספורמציה טי אס בי - אז מטריצת הבודי טוויסט נוצרת כאשר הנגזרת מימין להופכית ומטריצת הספיישיאל טוויסט נוצרת כשהסדר הפוך. \
            שימו לב לחלק התחתון שמתאר כיצד משתמשים במטריצה צמודה 6 על 6 כדי לקבל טוויסט ביחס למסגרת אחת מטוויסט ביחס למסגרת אחרת."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2: Twists", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)

        img0 = ImageMobject('../images/twistsum.png').scale(1.15).shift(DOWN*0.6)

        self.add(img0)
        self.wait()

class Chap3_3220(OPU_Slide):
   def construct(self):
        note = "מה שנראה עכשיו זה אפשר לפרש את הטוויסט לתנועת בורג - לפי התאוריה של מוצי כל תנועה של גוף קשיח יכולה להיות מתוארת כתנועה התואמת סיבוב לפי ציר בורג אס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2.2: The Screw Interpretation of a Twist", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)

         #include video
        cap = cv2.VideoCapture("../media/videos/screwMotion.mp4")
        rec = Rectangle(color=WHITE, width=2, height=1, fill_color=WHITE, fill_opacity=1).shift(LEFT*2.1+UP*0.5)

        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.66).shift(0.5*DOWN)
                self.add(frame_img, rec)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
        self.remove(rec)

       
        self.wait()

class Chap3_3221(OPU_Slide):
   def construct(self):
        note = "אס הוא שלשה כאשר קיו היא נקודה על ציר הבורג , אס זהו וקטור יחידה המתאר את כיוונו ואייצ זהו הפיטש - היחס בין המהירות הלינארית לזויתית של הגוף המסתובב"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2.2: The Screw Interpretation of a Twist", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/screw.png').scale(1.15).shift(DOWN*0.2)
        s = Tex(r"S is the collection $\{q, \hat{s}, h\}$", color=GREEN).scale(0.4).next_to(img0, UP).align_to(secondary_title, LEFT)

        self.add(img0, s,)
        self.wait()

class Chap3_3222(OPU_Slide):
   def construct(self):
        note = "אז אנחנו רואים את הקשר בין טוויסט לציר הבורג אס בכך שהמהירות הזויותית של הטוויסט - אומגה הוא ציר הסיבוב מוכפל בשינוי בזוית והמהירות הלינארית היא הקרוס פרודקט של ציר הסיבוב בנקודה קיו מחובר למכפלה המתארת את התנועה לאורך ציר הבורג "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2.2: The Screw Interpretation of a Twist", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/screw.png').scale(1.15).shift(DOWN*0.2)
        s = Tex(r"S is the collection $\{q, \hat{s}, h\}$", color=GREEN).scale(0.4).next_to(img0, UP).align_to(secondary_title, LEFT)

        so = Tex(r"so a twist V corresponding to an angular velocity $\dot{\theta}$ about a screw S is:", color=GREEN).scale(0.4).next_to(img0, DOWN).shift(LEFT)
        img1 = ImageMobject('../images/twistscrew.png').scale(1.15).next_to(so, RIGHT)

        self.add(img0, s, so, img1)
        self.wait()

class Chap3_3223(OPU_Slide):
   def construct(self):
        note = "ואחרי שהכרנו את הקשר בין הטוויסט לציר הבורג אס - במקום להשתמש בשלשה קיו , אס גג והפיטש  - ניתן לייצג את ציר הבורג באמצעות הגרסא המנורמלת של הטוויסט. כאשר אם יש מהירות זויותית אז ננרמל בגודל של הוקטור אומגה . ואם אין מהירות זויותית אז התנועה היא לינארית בלבד משמע ננרמל לפי גודל הוקטור וי. כפי שניתן לראות הנרמול מתבצע פשוט על ידי חלוקה בטטא דוט  "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2.2: The Screw Interpretation of a Twist", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/ab.png')

        s = Tex(r"Instead of using $\{q, \hat{s}, h\}$, the screw axis S is described using a normalized version of a twist:", color=GREEN).scale(0.4).next_to(img0, UP).shift(LEFT)
        img0.scale(1.15).shift(DOWN*0.2).align_to(s, LEFT)
        so = Tex(r"This leads to the following definition of a “unit” (normalized) screw axis:", color=GREEN).scale(0.4).next_to(img0, DOWN).align_to(s, LEFT)

        # img1 = ImageMobject('../images/twistscrew.png').scale(1.15).next_to(so, RIGHT)

        self.add(img0, s, so)
        self.wait()

class Chap3_3224(OPU_Slide):
   def construct(self):
        note = "כלומר ציר הסיבוב אס הוא גרסה מנורמלת של הטוויסט וכל הייצוגים המטריציונים שלו זהים"
        self.create_note(note)
        self.add_info()
        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.2.2: The Screw Interpretation of a Twist", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/ab.png')

        s = Tex(r"Instead of using $\{q, \hat{s}, h\}$, the screw axis S is described using a normalized version of a twist:", color=GREEN).scale(0.4).next_to(img0, UP).shift(LEFT)
        img0.scale(1.15).shift(DOWN*0.2).align_to(s, LEFT)
        so = Tex(r"This leads to the following definition of a “unit” (normalized) screw axis:", color=RED).scale(0.4).next_to(img0, DOWN).align_to(s, LEFT)

        self.play(so.animate().shift(UP*3).set(color=RED))

        img0 = ImageMobject('../images/unit1.png').scale(1).shift(UP*0.3)
        img1 = ImageMobject('../images/unit2.png').scale(1).next_to(img0, DOWN)
        self.add(img0, img1)
        self.wait()

class Chap3_330(OPU_Slide):
   def construct(self):
        note = "ובכך בעצם הגענו לייצוג חסכוני של טרנספורמציה באמצעות קואורדינטות אקספוננציאליות במימד 6 בצורה של ציר בורג אס מוכפל בזוית טטא. אז מטריצת הטרנספורמציה ההומוגנית טי שקולה לאקספוננט אי בחזקת הייצוג המטריציוני של ציר הבורג מוכפל בזוית טטא. \
            כפי שניתן לראות את המטריצה עצמה ניתן לשחזר על ידי נוסחת רודריגז ( עבור האקספוננט) ומכפלה של המטריצה שבסוגריים בוקטור המהירות וי. אם אין מהירות זויותית אז התנוע היא לינארית - משמע טרנסלציה בלבד."
        self.create_note(note)
        self.add_info()
        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.3.1: Exponential Coordinates of Rigid-Body Motions", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/expo1.png').scale(1.2).shift(UP)
        img1 = ImageMobject('../images/expo2.png').scale(1.2).next_to(img0, DOWN)
        img2 = ImageMobject('../images/expo3.png').scale(1.2).next_to(img1, DOWN).align_to(img1, LEFT)
        self.add(img0, img1, img2)
        self.wait()

class Chap3_331(OPU_Slide):
   def construct(self):
        note = "הנושא האחרון של הפרק הוא האלגוריתם לקבלת הייצוג האקספוננציאלי מתוך מטריצת טרנספורמציה. בהינתן מטריצת טרנספורמציה הומוגנית טי - ניתן לחשב באמצעות האלגוריתם את ציר הבורג אס ואת הזוית טטא."
        self.create_note(note)
        self.add_info()
        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.3.2: Matrix Logarithm of Rigid-Body Motions", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/explog1.png').scale(1.15).shift(UP*1.5)
        s = Tex(r"The Problem: Given a transformation matrix (R, p) $\in SE(3)$, one can find a screw axis $S=(w,v)$ and a scalar $\theta$ such that: ", color=RED).scale(0.4).next_to(img0, DOWN)

        img1 = ImageMobject('../images/log1.png').scale(1).next_to(s, DOWN)
        self.add(img0, img1, s)
        self.wait()

class Chap3_332(OPU_Slide):
   def construct(self):
        note = "האלגוריתם מאד פשוט והוא בעצם עוף את האלגוריתם הלוגריטמי שראינו עבור מטריצת הרוטציה. אני לא אעבור עליו עכשיו אלא כשנפתור תרגילים בנושא."
        self.create_note(note)
        self.add_info()
        title = Text("Chapter 3: Rigid-Body Motions").shift(UP*3).scale(0.65)
        secondary_title = Text("3.3.3.2: Matrix Logarithm of Rigid-Body Motions", color=BLUE).next_to(title, DOWN).scale(0.4).shift(UP*0.2)
        self.add(title, secondary_title)
        img0 = ImageMobject('../images/log2.png').scale(1.15).shift(DOWN*0.1)
        
        self.add(img0)
        self.wait()