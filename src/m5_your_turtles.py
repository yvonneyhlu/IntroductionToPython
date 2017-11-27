"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Youhua Lu.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

body = rg.SimpleTurtle('turtle')
body.pen = rg.Pen('blue',5)
body.speed = 15
size = 30

for k in range(10):
    body.draw_circle(size)
    body.pen_up()
    body.left(90)
    body.forward(10)
    body.right(90)
    body.pen_down()
    size=size - 3

star = rg.SimpleTurtle('turtle')
star.pen = rg.Pen('yellow', 5)
star.speed = 5

for k in range(5):
    star.right(72)
    star.forward(100)
    star.right(36)

window.close_on_mouse_click()



