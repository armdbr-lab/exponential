from manim import *

class EquationSolverRefined(Scene):
    def construct(self):
        # ==================== VIBRANT BACKGROUND ====================
        self.camera.background_color = "#0a0e27"  # Deep navy blue
        Text.set_default(color=WHITE)
        
        # ==================== TOPIC SECTION ====================
        title = Text("Solve the following equations:", font_size=40)
        title.move_to([0, 3.0, 0])
        title.set_color("#00ff88")  # Neon green
        
        eq1_topic = Text("x + y = 10", font_size=36)
        eq1_topic.move_to([0, 2.0, 0])
        eq1_topic.set_color("#ff006e")  # Hot pink
        
        eq2_topic = Text("2x + 5y = 32", font_size=36)
        eq2_topic.move_to([0, 1.0, 0])
        eq2_topic.set_color("#00d4ff")  # Cyan blue
        
        # Display topic all at once
        self.play(
            Write(title),
            Write(eq1_topic),
            Write(eq2_topic),
            run_time=2.0
        )
        self.wait(3)
        
        # Fade out topic
        self.play(
            FadeOut(title),
            FadeOut(eq1_topic),
            FadeOut(eq2_topic),
            run_time=1.5
        )
        self.wait(1.0)
        
        # ==================== THREE DIVIDER LINES - COLORFUL ====================
        divider_line_left = Line(
            start=[-2.67, 3.5, 0],
            end=[-2.67, -3.5, 0],
            color="#ff006e",  # Hot pink
            stroke_width=4
        )
        
        divider_line_right = Line(
            start=[2.67, 3.5, 0],
            end=[2.67, -3.5, 0],
            color="#00d4ff",  # Cyan blue
            stroke_width=4
        )
        
        self.play(Create(divider_line_left), Create(divider_line_right), run_time=1.5)
        self.wait(1.0)
        
        # ==================== COLUMN 1 (LEFT) - PINK THEME ====================
        col1_x = -5.4
        current_col1_y = 3.0
        spacing = 0.7
        
        col1_elements = []
        
        # STEP 1: Equation (1) label
        step1_label = Text("Equation (1):", font_size=28, color="#ff006e")  # Hot pink
        step1_label.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step1_label), run_time=1.5)
        col1_elements.append(step1_label)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # STEP 2: Equation (1)
        step1_eq = Text("x + y = 10", font_size=28, color="#ff1493")  # Deep pink
        step1_eq.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step1_eq), run_time=1.5)
        col1_elements.append(step1_eq)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # STEP 3: Equation (2) label
        step2_label = Text("Equation (2):", font_size=28, color="#00d4ff")  # Cyan
        step2_label.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step2_label), run_time=1.5)
        col1_elements.append(step2_label)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # STEP 4: Equation (2)
        step2_eq = Text("2x + 5y = 32", font_size=28, color="#00ffff")  # Bright cyan
        step2_eq.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step2_eq), run_time=1.5)
        col1_elements.append(step2_eq)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # STEP 5: Multiply Eq(1) by 2 label
        step3_label = Text("Multiply Eq(1) by 2:", font_size=26, color="#ff006e")  # Hot pink
        step3_label.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step3_label), run_time=1.5)
        col1_elements.append(step3_label)
        current_col1_y -= spacing
        self.wait(0.8)
        
        # STEP 6: Multiply step
        step3_step = Text("2(x + y) = 2(10)", font_size=24, color="#ffaa00")  # Orange
        step3_step.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step3_step), run_time=1.5)
        col1_elements.append(step3_step)
        current_col1_y -= spacing
        self.wait(0.8)
        
        # STEP 7: Result of multiplication
        step3_result = Text("2x + 2y = 20", font_size=26, color="#ff1493")  # Deep pink
        step3_result.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step3_result), run_time=1.5)
        col1_elements.append(step3_result)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # STEP 8: Already have Eq(2)
        step4_label = Text("We have Eq(2):", font_size=26, color="#00d4ff")  # Cyan
        step4_label.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step4_label), run_time=1.5)
        col1_elements.append(step4_label)
        current_col1_y -= spacing
        self.wait(0.8)
        
        # STEP 9: Multiply step
        step4_step = Text("2x + 5y = 32", font_size=24, color="#00ffff")  # Bright cyan
        step4_step.move_to([col1_x, current_col1_y, 0])
        self.play(Write(step4_step), run_time=1.5)
        col1_elements.append(step4_step)
        current_col1_y -= spacing
        self.wait(1.0)
        
        # ==================== COLUMN 2 (MIDDLE) - PURPLE/MAGENTA THEME ====================
        col2_x = 0.0
        current_col2_y = 3.0
        spacing = 0.8
        
        col2_elements = []
        
        # STEP 10: Subtract label
        step5_label = Text("Subtract Eq(1)' - Eq(2):", font_size=26, color="#a855f7")  # Purple
        step5_label.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step5_label), run_time=1.5)
        col2_elements.append(step5_label)
        current_col2_y -= spacing
        self.wait(0.8)
        
        # STEP 11: Subtraction step 1
        step5_step1 = Text("(2x + 2y) -", font_size=22, color="#d946ef")  # Magenta
        step5_step1.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step5_step1), run_time=1.5)
        col2_elements.append(step5_step1)
        current_col2_y -= spacing
        self.wait(0.6)
        
        # STEP 12: Subtraction step 2
        step5_step2 = Text("(2x + 5y) = 20 - 32", font_size=22, color="#d946ef")  # Magenta
        step5_step2.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step5_step2), run_time=1.5)
        col2_elements.append(step5_step2)
        current_col2_y -= spacing
        self.wait(0.8)
        
        # STEP 13: Subtraction result
        step5_result = Text("-3y = -12", font_size=28, color="#ec4899")  # Pink
        step5_result.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step5_result), run_time=1.5)
        col2_elements.append(step5_result)
        current_col2_y -= spacing
        self.wait(1.0)
        
        # STEP 14: Divide label
        step6_label = Text("Divide both sides by (-3):", font_size=26, color="#a855f7")  # Purple
        step6_label.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step6_label), run_time=1.5)
        col2_elements.append(step6_label)
        current_col2_y -= spacing
        self.wait(0.8)
        
        # STEP 15: Division step
        step6_step = Text("y = (-12) / (-3)", font_size=24, color="#d946ef")  # Magenta
        step6_step.move_to([col2_x, current_col2_y, 0])
        self.play(Write(step6_step), run_time=1.5)
        col2_elements.append(step6_step)
        current_col2_y -= spacing
        self.wait(1.0)
        
        # STEP 16: Y value with LIME color and CYAN box
        step6_result = Text("y = 4", font_size=32, color="#00ff88")  # Neon green
        step6_box = SurroundingRectangle(step6_result, color="#00d4ff", stroke_width=4, buff=0.3)  # Cyan box
        step6_result.move_to([col2_x, current_col2_y, 0])
        step6_box.move_to(step6_result)
        self.play(Write(step6_box), Write(step6_result), run_time=2.0)
        col2_elements.append(step6_box)
        col2_elements.append(step6_result)
        current_col2_y -= spacing
        self.wait(2.0)
        
        # ==================== COLUMN 3 (RIGHT) - GOLDEN/ORANGE THEME ====================
        col3_x = 4.5
        current_col3_y = 3.0
        spacing = 0.7
        
        col3_elements = []
        
        # STEP 17: Substitute label
        step7_label = Text("Substitute y = 4", font_size=26, color="#fbbf24")  # Amber
        step7_label.move_to([col3_x, current_col3_y, 0])
        self.play(Write(step7_label), run_time=1.5)
        col3_elements.append(step7_label)
        current_col3_y -= spacing
        self.wait(0.8)
        
        # STEP 18: Substitute label 2
        step7_label2 = Text("in Equation (1):", font_size=26, color="#fbbf24")  # Amber
        step7_label2.move_to([col3_x, current_col3_y, 0])
        self.play(Write(step7_label2), run_time=1.5)
        col3_elements.append(step7_label2)
        current_col3_y -= spacing
        self.wait(0.8)
        
        # STEP 19: Substitute step 1
        step7_step1 = Text("x + 4 = 10", font_size=24, color="#fcd34d")  # Golden
        step7_step1.move_to([col3_x, current_col3_y, 0])
        self.play(Write(step7_step1), run_time=1.5)
        col3_elements.append(step7_step1)
        current_col3_y -= spacing
        self.wait(0.8)
        
        # STEP 20: Subtract to isolate x
        step7_step2 = Text("x = 10 - 4", font_size=24, color="#fcd34d")  # Golden
        step7_step2.move_to([col3_x, current_col3_y, 0])
        self.play(Write(step7_step2), run_time=1.5)
        col3_elements.append(step7_step2)
        current_col3_y -= spacing
        self.wait(1.0)
        
        # STEP 21: X value with ORANGE color and MAGENTA box
        step7_result = Text("x = 6", font_size=32, color="#ffaa00")  # Orange
        step7_box = SurroundingRectangle(step7_result, color="#ff006e", stroke_width=4, buff=0.3)  # Hot pink box
        step7_result.move_to([col3_x, current_col3_y, 0])
        step7_box.move_to(step7_result)
        self.play(Write(step7_box), Write(step7_result), run_time=2.0)
        col3_elements.append(step7_box)
        col3_elements.append(step7_result)
        current_col3_y -= spacing
        self.wait(2.0)
        
        # ==================== TRANSITION: FADE OUT THREE COLUMNS ====================
        self.play(
            FadeOut(divider_line_left),
            FadeOut(divider_line_right),
            *[FadeOut(element) for element in col1_elements],
            *[FadeOut(element) for element in col2_elements],
            *[FadeOut(element) for element in col3_elements],
            run_time=2.0
        )
        self.wait(1.0)
        
        # ==================== VERIFICATION SCREEN ====================
        verify_title = Text("VERIFICATION", font_size=48, color="#00ff88")  # Neon green
        verify_title.move_to([0, 2.5, 0])
        
        self.play(Write(verify_title), run_time=1.5)
        self.wait(1.0)
        
        # Verification Equation 1
        verify_label1 = Text("Equation (1): x + y = 10", font_size=36, color="#ff006e")  # Hot pink
        verify_label1.move_to([0, 1.3, 0])
        
        verify_sub1 = Text("6 + 4 = 10", font_size=32, color="#ffaa00")  # Orange
        verify_sub1.move_to([0, 0.5, 0])
        
        verify_check1 = Text("✓ CORRECT", font_size=32, color="#00ff88")  # Neon green
        verify_check1.move_to([0, -0.3, 0])
        
        self.play(Write(verify_label1), run_time=1.5)
        self.wait(0.8)
        self.play(Write(verify_sub1), run_time=1.5)
        self.wait(0.8)
        self.play(Write(verify_check1), run_time=1.5)
        self.wait(1.5)
        
        # Verification Equation 2
        verify_label2 = Text("Equation (2): 2x + 5y = 32", font_size=36, color="#00d4ff")  # Cyan
        verify_label2.move_to([0, -1.2, 0])
        
        verify_sub2 = Text("2(6) + 5(4) = 12 + 20 = 32", font_size=32, color="#fbbf24")  # Amber
        verify_sub2.move_to([0, -2.0, 0])
        
        verify_check2 = Text("✓ CORRECT", font_size=32, color="#00ff88")  # Neon green
        verify_check2.move_to([0, -2.8, 0])
        
        self.play(Write(verify_label2), run_time=1.5)
        self.wait(0.8)
        self.play(Write(verify_sub2), run_time=1.5)
        self.wait(0.8)
        self.play(Write(verify_check2), run_time=1.5)
        self.wait(2.0)
        
        # ==================== FINAL SOLUTION ====================
        self.play(
            FadeOut(verify_title),
            FadeOut(verify_label1),
            FadeOut(verify_sub1),
            FadeOut(verify_check1),
            FadeOut(verify_label2),
            FadeOut(verify_sub2),
            FadeOut(verify_check2),
            run_time=1.5
        )
        self.wait(0.5)
        
        final_title = Text("FINAL SOLUTION", font_size=48, color="#00ff88")  # Neon green
        final_title.move_to([0, 2.0, 0])
        
        final_x = Text("x = 6", font_size=44, color="#ffaa00")  # Orange
        final_x_box = SurroundingRectangle(final_x, color="#ff006e", stroke_width=4, buff=0.4)  # Hot pink
        final_x_box.move_to([0, 0.5, 0])
        final_x.move_to([0, 0.5, 0])
        
        final_y = Text("y = 4", font_size=44, color="#00ff88")  # Neon green
        final_y_box = SurroundingRectangle(final_y, color="#00d4ff", stroke_width=4, buff=0.4)  # Cyan
        final_y_box.move_to([0, -1.0, 0])
        final_y.move_to([0, -1.0, 0])
        
        self.play(Write(final_title), run_time=1.5)
        self.wait(1.0)
        self.play(Write(final_x_box), Write(final_x), run_time=1.5)
        self.wait(1.0)
        self.play(Write(final_y_box), Write(final_y), run_time=1.5)
        self.wait(3.0)


# YouTube Short - Vertical Format (9:16)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9

class EquationSolverYouTubeShort(Scene):
    """
    YouTube Short format (9:16) - Three clear screens with VIBRANT COLORS:
    1. Problem statement (15 seconds)
    2. All solution steps visible (35 seconds)
    3. Verification (30 seconds)
    Total: 80 seconds (1 min 20 sec)
    
    Solving: x + y = 10
             2x + 5y = 32
    
    Solution: x = 6, y = 4
    """
    def construct(self):
        self.camera.background_color = "#0a0e27"  # Deep navy blue
        Text.set_default(color=WHITE)
        
        # ==================== SCREEN 1: PROBLEM ====================
        self.screen_problem()
        
        # ==================== SCREEN 2: FULL SOLUTION ====================
        self.screen_full_solution()
        
        # ==================== SCREEN 3: VERIFICATION ====================
        self.screen_verification()
    
    def screen_problem(self):
        """Screen 1: Show the problem (15 seconds total)"""
        # Title with neon green
        title = Text("Solve the Equations", font_size=60, color="#00ff88", weight=BOLD)
        title.move_to([0, 6.5, 0])
        
        # Equation 1 - HOT PINK
        eq1_text = "x + y = 10"
        eq1_display = Text(eq1_text, font_size=70, color="#ff006e", weight=BOLD)
        eq1_display.move_to([0, 4.0, 0])
        
        # Equation 2 - CYAN
        eq2_text = "2x + 5y = 32"
        eq2_display = Text(eq2_text, font_size=70, color="#00d4ff", weight=BOLD)
        eq2_display.move_to([0, 2.0, 0])
        
        # Decorative lines - Multiple colors
        line_left = Line([-4.0, 1.0, 0], [-3.5, 1.0, 0], color="#ff006e", stroke_width=6)
        line_center = Line([-0.25, 1.0, 0], [0.25, 1.0, 0], color="#00ff88", stroke_width=6)
        line_right = Line([3.5, 1.0, 0], [4.0, 1.0, 0], color="#00d4ff", stroke_width=6)
        
        # Instruction text - GOLDEN
        instruction = Text("Using Substitution Method", font_size=40, color="#fbbf24", weight=BOLD)
        instruction.move_to([0, -1.5, 0])
        
        # Animate entrance
        self.play(
            Write(title),
            run_time=1.0
        )
        self.wait(0.5)
        
        self.play(
            Write(eq1_display),
            run_time=0.8
        )
        self.wait(0.3)
        
        self.play(
            Write(eq2_display),
            run_time=0.8
        )
        self.wait(0.3)
        
        self.play(
            Create(line_left),
            Create(line_center),
            Create(line_right),
            run_time=0.6
        )
        self.wait(0.3)
        
        self.play(
            Write(instruction),
            run_time=0.8
        )
        self.wait(7.0)  # Hold on screen for 7 seconds
        
        # Fade out to next screen
        self.play(
            FadeOut(title),
            FadeOut(eq1_display),
            FadeOut(eq2_display),
            FadeOut(line_left),
            FadeOut(line_center),
            FadeOut(line_right),
            FadeOut(instruction),
            run_time=1.0
        )
        self.wait(0.2)
    
    def screen_full_solution(self):
        """Screen 2: Show all solution steps at once (35 seconds total)"""
        
        # Title - LIME GREEN
        title = Text("SOLUTION STEPS", font_size=60, color="#00ff88", weight=BOLD)
        title.move_to([0, 7.5, 0])
        
        # ---- STEP 1 - HOT PINK ----
        step1_label = Text("Step 1: Express x from Eq(1)", font_size=38, color="#ff006e", weight=BOLD)
        step1_label.move_to([0, 6.3, 0])
        
        step1_eq = Text("x = 10 - y", font_size=35, color="#ffaa00")
        step1_eq.move_to([0, 5.5, 0])
        
        # ---- STEP 2 - CYAN ----
        step2_label = Text("Step 2: Substitute into Eq(2)", font_size=38, color="#00d4ff", weight=BOLD)
        step2_label.move_to([0, 4.5, 0])
        
        step2_eq = Text("2(10 - y) + 5y = 32", font_size=35, color="#00ffff")
        step2_eq.move_to([0, 3.8, 0])
        
        # ---- STEP 3 - PURPLE ----
        step3_label = Text("Step 3: Simplify & Solve", font_size=38, color="#a855f7", weight=BOLD)
        step3_label.move_to([0, 2.8, 0])
        
        step3_eq1 = Text("20 - 2y + 5y = 32", font_size=35, color="#d946ef")
        step3_eq1.move_to([0, 2.1, 0])
        
        step3_eq2 = Text("3y = 12", font_size=35, color="#d946ef")
        step3_eq2.move_to([0, 1.4, 0])
        
        # ---- STEP 4: Y VALUE - GOLDEN ----
        step4_label = Text("Step 4: Solve for y", font_size=38, color="#fbbf24", weight=BOLD)
        step4_label.move_to([0, 0.5, 0])
        
        step4_y = Text("y = 4", font_size=45, color="#00ff88", weight=BOLD)
        step4_y.move_to([0, -0.4, 0])
        step4_y_box = SurroundingRectangle(step4_y, color="#00ff88", stroke_width=4, buff=0.3)
        
        # ---- STEP 5: X VALUE - PINK ----
        step5_label1 = Text("Step 5: Solve for x", font_size=38, color="#ec4899", weight=BOLD)
        step5_label1.move_to([0, -1.3, 0])
        
        step5_label2 = Text("x = 10 - 4", font_size=35, color="#f472b6")
        step5_label2.move_to([0, -2.0, 0])

        step5_x = Text("x = 6", font_size=45, color="#ffaa00", weight=BOLD)
        step5_x.move_to([0, -2.9, 0])
        step5_x_box = SurroundingRectangle(step5_x, color="#ffaa00", stroke_width=4, buff=0.3)
        
        # Animate all steps
        self.play(Write(title), run_time=0.8)
        self.wait(0.2)
        
        # Step 1
        self.play(
            Write(step1_label),
            Write(step1_eq),
            run_time=1.2
        )
        self.wait(1.5)
        
        # Step 2
        self.play(
            Write(step2_label),
            Write(step2_eq),
            run_time=1.2
        )
        self.wait(1.5)
        
        # Step 3
        self.play(
            Write(step3_label),
            Write(step3_eq1),
            run_time=1.0
        )
        self.wait(0.5)
        self.play(
            Write(step3_eq2),
            run_time=0.8
        )
        self.wait(1.5)
        
        # Step 4
        self.play(
            Write(step4_label),
            run_time=0.8
        )
        self.wait(0.3)
        self.play(
            Write(step4_y_box),
            Write(step4_y),
            run_time=1.0
        )
        self.wait(1.5)
        
        # Step 5
        self.play(
            Write(step5_label1),
            run_time=0.8
        )
        self.wait(0.3)
        self.play(
            Write(step5_label2),
            run_time=0.8
        )
        self.wait(0.3)
        self.play(
            Write(step5_x_box),
            Write(step5_x),
            run_time=1.0
        )
        self.wait(1.5)
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(step1_label), FadeOut(step1_eq),
            FadeOut(step2_label), FadeOut(step2_eq),
            FadeOut(step3_label), FadeOut(step3_eq1), FadeOut(step3_eq2),
            FadeOut(step4_label), FadeOut(step4_y_box), FadeOut(step4_y),
            FadeOut(step5_label1), FadeOut(step5_label2),
            FadeOut(step5_x_box), FadeOut(step5_x),
            run_time=0.8
        )
        self.wait(0.2)
    
    def screen_verification(self):
        """Screen 3: Verification - prove the solution is correct (30 seconds total)"""
        
        # Title - NEON GREEN
        title = Text("VERIFICATION ✓", font_size=70, color="#00ff88", weight=BOLD)
        title.move_to([0, 7.2, 0])
        
        # Solution display with colored boxes
        x_value = Text("x = 6", font_size=50, color="#ffaa00", weight=BOLD)
        x_value.move_to([0, 6.0, 0])
        x_box = SurroundingRectangle(x_value, color="#ffaa00", stroke_width=3, buff=0.3)
        
        y_value = Text("y = 4", font_size=50, color="#00ff88", weight=BOLD)
        y_value.move_to([0, 4.5, 0])
        y_box = SurroundingRectangle(y_value, color="#00ff88", stroke_width=3, buff=0.3)
        
        # Divider line - RAINBOW EFFECT
        line_part1 = Line([-3.5, 3.5, 0], [-1.75, 3.5, 0], color="#ff006e", stroke_width=4)
        line_part2 = Line([-1.75, 3.5, 0], [0, 3.5, 0], color="#00d4ff", stroke_width=4)
        line_part3 = Line([0, 3.5, 0], [1.75, 3.5, 0], color="#00ff88", stroke_width=4)
        line_part4 = Line([1.75, 3.5, 0], [3.5, 3.5, 0], color="#fbbf24", stroke_width=4)
        
        # Verification Label
        verify_label = Text("Checking both equations:", font_size=40, color="#a855f7", weight=BOLD)
        verify_label.move_to([0, 3.0, 0])
        
        # Equation 1 Verification - HOT PINK THEME
        eq1_check_label = Text("Eq(1): x + y = 10", font_size=38, color="#ff006e", weight=BOLD)
        eq1_check_label.move_to([0, 1.9, 0])
        
        eq1_check_calc = Text("6 + 4", font_size=35, color="#ffaa00")
        eq1_check_calc.move_to([0, 1.1, 0])
        
        eq1_check_result = Text("= 10 ✓", font_size=35, color="#00ff88")
        eq1_check_result.move_to([0, 0.3, 0])
        
        # Equation 2 Verification - CYAN THEME
        eq2_check_label = Text("Eq(2): 2x + 5y = 32", font_size=38, color="#00d4ff", weight=BOLD)
        eq2_check_label.move_to([0, -0.8, 0])
        
        eq2_check_calc = Text("2(6) + 5(4)", font_size=35, color="#fbbf24")
        eq2_check_calc.move_to([0, -1.6, 0])
        
        eq2_check_result = Text("= 12 + 20 = 32 ✓", font_size=35, color="#00ff88")
        eq2_check_result.move_to([0, -2.4, 0])
        
        # Final verification stamp - GLOWING EFFECT
        final_stamp = Text("VERIFIED!", font_size=60, color="#00ff88", weight=BOLD)
        final_stamp.move_to([0, -3.8, 0])
        stamp_box = SurroundingRectangle(final_stamp, color="#00ff88", stroke_width=5, buff=0.3)
        
        # Animate verification
        self.play(Write(title), run_time=1.0)
        self.wait(0.3)
        
        self.play(
            Write(x_box),
            Write(x_value),
            run_time=0.7
        )
        self.wait(0.2)
        
        self.play(
            Write(y_box),
            Write(y_value),
            run_time=0.7
        )
        self.wait(0.2)
        
        self.play(
            Create(line_part1),
            Create(line_part2),
            Create(line_part3),
            Create(line_part4),
            run_time=0.8
        )
        self.wait(0.2)
        
        self.play(Write(verify_label), run_time=0.8)
        self.wait(0.5)
        
        # Check Equation 1
        self.play(Write(eq1_check_label), run_time=0.8)
        self.wait(0.3)
        self.play(Write(eq1_check_calc), run_time=0.8)
        self.wait(0.3)
        self.play(Write(eq1_check_result), run_time=1.0)
        self.wait(1.0)
        
        # Check Equation 2
        self.play(Write(eq2_check_label), run_time=0.8)
        self.wait(0.3)
        self.play(Write(eq2_check_calc), run_time=0.8)
        self.wait(0.3)
        self.play(Write(eq2_check_result), run_time=1.0)
        self.wait(1.0)
        
        # Final verification stamp
        self.play(
            Write(stamp_box),
            Write(final_stamp),
            run_time=1.2
        )
        self.wait(3.0)
        
        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(x_box),
            FadeOut(x_value),
            FadeOut(y_box),
            FadeOut(y_value),
            FadeOut(line_part1),
            FadeOut(line_part2),
            FadeOut(line_part3),
            FadeOut(line_part4),
            FadeOut(verify_label),
            FadeOut(eq1_check_label), FadeOut(eq1_check_calc), FadeOut(eq1_check_result),
            FadeOut(eq2_check_label), FadeOut(eq2_check_calc), FadeOut(eq2_check_result),
            FadeOut(stamp_box), FadeOut(final_stamp),
            run_time=1.0
        )
