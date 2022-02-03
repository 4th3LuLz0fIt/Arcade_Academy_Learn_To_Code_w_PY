"""Code to show how to draw uing Python and Arcade"""
# How to Open a Window for Drawing?

# import the arcade library
import arcade

# Create a window for drawing
# from arcade libabry use function open_window
# open_window takes three parameters
# height and width integers and TITLE of the window as a string

arcade.open_window(600, 600, 'Drawing Example')

# Clearing the screen
arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

# To draw the colors we need two more fuction to start and end
# To Draw
arcade.start_render()

# (The drawing code goes in between start_render and finish_render .)
# Draw code goes here!

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom 0f
# Fill w/ color: arcade.csscolor.COLORNAME
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(300, 599, 300, 0, arcade.csscolor.GREEN)
# Draw a tree
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
# Draw circle for tree leaves
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.GREEN)
# Draw Eclipse
#arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
#arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)

# Ellipse Tree
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Arc Tree
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

arcade.draw_rectangle_filled(400, 320, 20, 40, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.GREEN)
# To end
arcade.finish_render()
# From the arcade library use run command
# The run command will keep the open_window() from closing

arcade.run()
