# from manim import *

# class Matrix_demo(Scene):
#     def construct(self):
#         background_grid = NumberPlane(
#             background_line_style={
#                 "stroke_color": GREY,
#                 "stroke_width": 1,
#             },
#             x_range=[-16,16],
#             y_range=[-16,16],
#             x_length=20,
#             y_length=20
#         )
#         background_grid.set_opacity(0.3)

#         foreground_grid = NumberPlane(
#             background_line_style={
#                 "stroke_color": BLUE,
#                 "stroke_width": 1,
#             },
#             x_range=[-16,16],
#             y_range=[-16,16],
#             x_length=20,
#             y_length=20
#         )
#         foreground_grid.set_opacity(0.7)

#         foreground_grid.set_z_index(1)
#         background_grid.set_z_index(-1)

#         background_grid_zoomed_in = NumberPlane(
#             background_line_style={
#                 "stroke_color": GREY,
#                 "stroke_width": 1,
#             },
#             x_range=[-4,4],
#             y_range=[-4,4],
#             x_length=20,
#             y_length=20
#         )
#         background_grid_zoomed_in.set_opacity(0.3)

#         foreground_grid_zoomed_in = NumberPlane(
#             background_line_style={
#                 "stroke_color": BLUE,
#                 "stroke_width": 1,
#             },
#             x_range=[-4,4],
#             y_range=[-4,4],
#             x_length=20,
#             y_length=20
#         )
#         foreground_grid_zoomed_in.set_opacity(0.7)

#         foreground_grid_zoomed_in.set_z_index(1)
#         background_grid_zoomed_in.set_z_index(-1)

#         i_hat_zoomed_in = Vector().put_start_and_end_on(
#             start=background_grid_zoomed_in.get_origin(),
#             end=background_grid_zoomed_in.c2p(1, 0)
#         ).set_color(GREEN)
#         j_hat_zoomed_in = Vector().put_start_and_end_on(
#             start=background_grid_zoomed_in.get_origin(),
#             end=background_grid_zoomed_in.c2p(0, 1)
#         ).set_color(RED)

#         i_label_zoomed_in = always_redraw(lambda :MathTex("\hat{i}", color=GREEN).next_to(i_hat_zoomed_in, DOWN))
#         j_label_zoomed_in = always_redraw(lambda :MathTex("\hat{j}", color=RED).next_to(j_hat_zoomed_in, LEFT))

#         planes_zoomed_in = Group(background_grid_zoomed_in, foreground_grid_zoomed_in)
#         planes = Group(background_grid, foreground_grid)

#         vector_group_zoomed_in = VGroup(i_hat_zoomed_in, j_hat_zoomed_in).set_z_index(2)


#         matrix = [[2, 1], [-3, 2]]
#         matrix_tex = MathTex("A = \\begin{bmatrix} 2 & 1 \\\ -3 & 2 \\end{bmatrix}").to_edge(UL).add_background_rectangle()

#         self.play(
#             *(DrawBorderThenFill(mob) for mob in planes_zoomed_in)
#         )

#         self.wait()

#         self.play(Create(vector_group_zoomed_in))
#         self.play(Write(i_label_zoomed_in), Write(j_label_zoomed_in))
#         self.wait(3)

#         i_hat = Vector().put_start_and_end_on(
#             start=background_grid.get_origin(),
#             end=background_grid.c2p(1, 0)
#         ).set_color(GREEN)
#         j_hat = Vector().put_start_and_end_on(
#             start=background_grid.get_origin(),
#             end=background_grid.c2p(0, 1)
#         ).set_color(RED)

#         vector_group = VGroup(i_hat, j_hat).set_z_index(2)

#         transformation_group = VGroup(vector_group, foreground_grid)

#         i_label = MathTex("\hat{i}", color=GREEN).next_to(i_hat, DOWN, buff=0.025).scale(0.6)
#         j_label = MathTex("\hat{j}", color=RED).next_to(j_hat, LEFT, buff=0.025).scale(0.6)

#         i_hat_text = always_redraw(lambda: MathTex('(1,0)').next_to(i_hat.get_end(), DR, buff=0.01))
#         j_hat_text = always_redraw(lambda: MathTex('(0,1)').next_to(j_hat.get_end(), UP, buff=0.01))

#         self.play(
#             *(FadeOut(mob) for mob in planes_zoomed_in),
#             *(DrawBorderThenFill(mob) for mob in planes),
#             ReplacementTransform(i_hat_zoomed_in, i_hat, run_time=2),
#             ReplacementTransform(j_hat_zoomed_in, j_hat, run_time=2),
#             ReplacementTransform(i_label_zoomed_in, i_label, run_time=2),
#             ReplacementTransform(j_label_zoomed_in, j_label, run_time=2)

#         )
#         self.remove(planes_zoomed_in)
#         self.add(vector_group)
#         self.remove(i_hat_zoomed_in, j_hat_zoomed_in)
#         self.add(i_label, j_label)
#         self.remove(i_label_zoomed_in, j_label_zoomed_in)

#         self.wait()

#         self.play(
#             FadeIn(i_hat_text.scale(0.5), run_time=4),
#             FadeIn(j_hat_text.scale(0.5), run_time=4)
#         )

#         self.add(i_hat_text.scale(0.5), j_hat_text.scale(0.5))

#         self.wait(2)

#         matrix_vector_i = MathTex("\\begin{pmatrix} 1 \\\ 0 \\end{pmatrix}", color=GREEN).to_corner(UL, buff=0.5)
#         matrix_vector_j = MathTex("\\begin{pmatrix} 0 \\\ 1 \\end{pmatrix}", color=RED).to_corner(UL, buff=0.5).shift(RIGHT)

#         matrix_i_label = MathTex("\hat{i}", color=GREEN).next_to(matrix_vector_i, DOWN)
#         matrix_j_label = MathTex("\hat{j}", color=RED).next_to(matrix_vector_j, DOWN)

#         self.play(
#             TransformMatchingTex(i_hat_text, matrix_vector_i, run_time=2),
#             TransformMatchingTex(j_hat_text, matrix_vector_j, run_time=2),
#             FadeIn(matrix_i_label, run_time=2),
#             FadeIn(matrix_j_label, run_time=2)
#         )
#         self.add(matrix_i_label)
#         self.add(matrix_j_label)
#         self.wait(2)

#         identity_matrix_vectors = Matrix([[1, 0], [0, 1]],
#                                  left_bracket="(",
#                                  right_bracket=")").to_edge(LEFT).shift(UP).set_opacity(0)
        
#         entries = identity_matrix_vectors.get_entries()
        
#         entries[0].set_color(GREEN)  
#         entries[2].set_color(GREEN)  
#         entries[1].set_color(RED)    
#         entries[3].set_color(RED)    

#         self.add(identity_matrix_vectors)

#         eye_vector_group = Group(matrix_vector_i, matrix_vector_j)

#         self.play(
#             Transform(eye_vector_group, identity_matrix_vectors, run_time=2),
#             ApplyMethod(identity_matrix_vectors.set_opacity, 1, run_time=2),
#             FadeOut(matrix_i_label),
#             FadeOut(matrix_j_label)
#         )
#         self.remove(matrix_j_label, matrix_i_label)
        
#         self.wait()

#         i_hat_vector = i_hat.get_end() - i_hat.get_start()
#         j_hat_vector = j_hat.get_end() - j_hat.get_start()

#         transformed_i = matrix @ i_hat_vector[:2]
#         transformed_j = matrix @ j_hat_vector[:2]

#         transformed_i_hat = Vector(transformed_i, color=GREEN)
#         transformed_j_hat = Vector(transformed_j, color=RED)

#         # self.play(
#         #    (
#         #         *(ApplyMatrix(mobject=mob, matrix=matrix, run_time=3) for mob in transformation_group),
#         #         Transform(i_hat, transformed_i_hat, run_time=3),
#         #         Transform(j_hat, transformed_j_hat, run_time=3)
#         #     )
#         # )
#         self.wait(2)

from manim import *

class MatrixDemo(Scene):
    def create_grid(self, x_range, y_range, color, opacity=0.3, z_index=0):
        grid = NumberPlane(
            background_line_style={
                "stroke_color": color,
                "stroke_width": 1,
            },
            x_range=x_range,
            y_range=y_range,
            x_length=20,
            y_length=20
        )
        grid.set_opacity(opacity)
        grid.set_z_index(z_index)
        return grid

    def create_vector(self, start, end, color, label_tex, label_position, label_color):
        vector = Vector().put_start_and_end_on(start=start, end=end).set_color(color)
        label = MathTex(label_tex, color=label_color).next_to(vector.get_end(), label_position)
        return vector, label

    def construct(self):
        # Create background and foreground grids
        background_grid = self.create_grid([-16, 16], [-16, 16], GREY, opacity=0.3, z_index=-1)
        foreground_grid = self.create_grid([-16, 16], [-16, 16], BLUE, opacity=0.7, z_index=1)
        self.add(background_grid, foreground_grid)

        # Create zoomed-in grids
        background_grid_zoomed_in = self.create_grid([-4, 4], [-4, 4], GREY, opacity=0.3, z_index=-1)
        foreground_grid_zoomed_in = self.create_grid([-4, 4], [-4, 4], BLUE, opacity=0.7, z_index=1)

        # Create i and j vectors for zoomed-in grid
        i_hat_zoomed_in, i_label_zoomed_in = self.create_vector(
            start=background_grid_zoomed_in.get_origin(), 
            end=background_grid_zoomed_in.c2p(1, 0), 
            color=GREEN, 
            label_tex=r"\hat{i}", 
            label_position=DOWN, 
            label_color=GREEN
        )
        j_hat_zoomed_in, j_label_zoomed_in = self.create_vector(
            start=background_grid_zoomed_in.get_origin(), 
            end=background_grid_zoomed_in.c2p(0, 1), 
            color=RED, 
            label_tex=r"\hat{j}", 
            label_position=LEFT, 
            label_color=RED
        )

        # Group for zoomed-in vectors
        vector_group_zoomed_in = VGroup(i_hat_zoomed_in, j_hat_zoomed_in)

        # Play grid animations
        self.play(DrawBorderThenFill(background_grid), DrawBorderThenFill(foreground_grid))
        self.wait()

        # Play zoomed-in grid and vector animations
        self.play(Create(vector_group_zoomed_in))
        self.play(Write(i_label_zoomed_in), Write(j_label_zoomed_in))
        self.wait(3)

        # Create vectors for regular grid
        i_hat, i_label = self.create_vector(
            start=background_grid.get_origin(), 
            end=background_grid.c2p(1, 0), 
            color=GREEN, 
            label_tex=r"\hat{i}", 
            label_position=DOWN, 
            label_color=GREEN
        )
        j_hat, j_label = self.create_vector(
            start=background_grid.get_origin(), 
            end=background_grid.c2p(0, 1), 
            color=RED, 
            label_tex=r"\hat{j}", 
            label_position=LEFT, 
            label_color=RED
        )

        # Group for regular vectors
        vector_group = VGroup(i_hat, j_hat)
        transformation_group = VGroup(vector_group, foreground_grid)

        # Play animations for transforming vectors
        self.play(
            ReplacementTransform(i_hat_zoomed_in, i_hat, run_time=2),
            ReplacementTransform(j_hat_zoomed_in, j_hat, run_time=2),
            ReplacementTransform(i_label_zoomed_in, i_label, run_time=2),
            ReplacementTransform(j_label_zoomed_in, j_label, run_time=2)
        )
        self.remove(background_grid, foreground_grid)
        self.add(vector_group)

        # Add labels for vectors
        i_hat_text = always_redraw(lambda: MathTex('(1,0)').next_to(i_hat.get_end(), DR, buff=0.01))
        j_hat_text = always_redraw(lambda: MathTex('(0,1)').next_to(j_hat.get_end(), UP, buff=0.01))

        self.play(
            FadeIn(i_hat_text.scale(0.5), run_time=4),
            FadeIn(j_hat_text.scale(0.5), run_time=4)
        )
        self.add(i_hat_text, j_hat_text)

        # Wait for a while
        self.wait(2)

        # Create matrix and vector labels for transformation
        matrix_vector_i = MathTex("\\begin{pmatrix} 1 \\\ 0 \\end{pmatrix}", color=GREEN).to_corner(UL, buff=0.5)
        matrix_vector_j = MathTex("\\begin{pmatrix} 0 \\\ 1 \\end{pmatrix}", color=RED).to_corner(UL, buff=0.5).shift(RIGHT)
        matrix_i_label = MathTex(r"\hat{i}", color=GREEN).next_to(matrix_vector_i, DOWN)
        matrix_j_label = MathTex(r"\hat{j}", color=RED).next_to(matrix_vector_j, DOWN)

        self.play(
            TransformMatchingTex(i_hat_text, matrix_vector_i, run_time=2),
            TransformMatchingTex(j_hat_text, matrix_vector_j, run_time=2),
            FadeIn(matrix_i_label, run_time=2),
            FadeIn(matrix_j_label, run_time=2)
        )
        self.add(matrix_i_label, matrix_j_label)
        self.wait(2)

        # Create identity matrix with colored vectors
        identity_matrix_vectors = Matrix([[1, 0], [0, 1]], left_bracket="(", right_bracket=")").to_edge(LEFT).shift(UP).set_opacity(0)
        entries = identity_matrix_vectors.get_entries()

        # Set colors for matrix entries
        entries[0].set_color(GREEN)
        entries[2].set_color(GREEN)
        entries[1].set_color(RED)
        entries[3].set_color(RED)

        self.add(identity_matrix_vectors)

        eye_vector_group = Group(matrix_vector_i, matrix_vector_j)

        self.play(
            Transform(eye_vector_group, identity_matrix_vectors, run_time=2),
            ApplyMethod(identity_matrix_vectors.set_opacity, 1, run_time=2),
            FadeOut(matrix_i_label),
            FadeOut(matrix_j_label)
        )

        self.remove(matrix_j_label, matrix_i_label)
        self.wait()
