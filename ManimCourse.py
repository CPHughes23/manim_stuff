from manim import *

class Test(Scene):
    def construct(self):
        t = Tex("Hello World!")
        self.play(Create(t))
        self.wait(3)

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = always_redraw(lambda : Text('(2, 2)').next_to(arrow.get_end(), RIGHT))
        self.add(numberplane, dot, arrow, origin_text, tip_text)
        arrow2 = Arrow(ORIGIN, [2,0,0], buff=0)
        self.play(Transform(arrow, arrow2), run_time = 2)
        



# class Vectors(VectorScene):
#     def construct(self):
#         plane = self.add_plane(animate = True).add_coordinates()
#         vector = self.add_vector([-3,-2], color = YELLOW)

#         basis = self.get_basis_vectors()
#         self.add(basis)
#         self.vector_to_coords(vector = vector)

#         vector2 = self.add_vector([2,2])
#         self.write_vector_coordinates(vector = vector2)
#         A = np.array([[2,1],[1,2]])
#         plane.add(vector)
#         self.play(ApplyMatrix(A, plane))

# class Vector_demo(VectorScene):
#     def construct(self):
#         plane = self.add_plane(animate=True).add_coordinates()
#         i_hat = self.add_vector([1, 0], color=GREEN)
#         i_label = MathTex("i", color=GREEN)
#         j_label = MathTex("j", color=RED)
#         self.label_vector(i_hat, i_label, animate=True, direction="right")
#         j_hat = self.add_vector([0, 1], color=RED)
#         self.label_vector(j_hat, j_label, animate=True, direction="left")
#         self.wait(3)
#         vector = self.add_vector([3, 2])
#         self.wait()
#         self.write_vector_coordinates(vector)
#         self.wait(2)
#         self.remove(i_hat, j_hat, i_label, j_label)
#         self.vector_to_coords(vector=vector)
#         self.wait(3)

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates= True,
            leave_ghost_vectors= True,
            show_basis_vectors= False
        )
    def construct(self):
        matrix = [[2, 0],[0, 2]]
        matrix_tex = MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}").to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(lambda: Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))

        vector = self.get_vector([1, -2], color = PURPLE_B)

        self.add_transformable_mobject(vector, unit_square)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix, run_time = 5)
        self.wait()
