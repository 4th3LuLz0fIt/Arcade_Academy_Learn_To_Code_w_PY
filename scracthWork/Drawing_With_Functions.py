""" Drawing with functions """

# import Arcade
import arcade

# Constants for screen height and width
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Draw screen and give it a title, set bkground color and render()


# Draw the ground using function draw_lrtb_rectangle_filled and set color
# Convert the function
def draw_grass():
    """ Draw Grass """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    # Draw a snow person

    # Draw apoint at x , y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes

    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def main():
    # Convert to main() function

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(150, 140)
    draw_snow_person(450, 180)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Calls def main(): to start the program

main()
