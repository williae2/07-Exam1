"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem3  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(10, 20), 200, 25, window)
    window.close_on_mouse_click()

    # TWO tests on ONE window.
    title = 'Tests 2, 3 and 4 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(15, 30), 100, 20, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 10), 90, 45, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 125), 80, 45, window)
    window.close_on_mouse_click()


def problem3(point, length, delta, window):
    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- Two positive integers
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given rg.RoseWindow:

      -- A VERTICAL rg.Line for which:
           -- Its topmost point is the given point.
           -- Its length is the given length.
           -- Its color is 'black'.
           -- Its thickness is 3.

      -- Several HORIZONTAL rg.Lines such that:
           -- All the horizontal lines have their leftmost point
                on the vertical line.  SEE THE PICTURES.
           -- For the FIRST of these HORIZONTAL lines:
                -- Its leftmost point is the given point.
                -- Its length is the given length.
           -- Each SUBSEQUENT HORIZONTAL rg.Line is  delta  pixels
                directly below the previous rg.Line (where delta is a parameter)
                and 20 pixels longer than the previous rg.Line.
           -- All the HORIZONTAL lines have thickness 3.
           -- The 1st, 4th, 7th, etc rg.Lines have color 'magenta',
              The 2nd, 5th, 8th, etc rg.Lines have color 'cyan'
              The 3rd, 6th, 9th, etc rg.Lines have color 'spring green'

      NOTE: The NUMBER of lines to draw is determined by the facts that:
        -- The vertical line has the given length.
        -- All horizontal lines have their left endpoint on the vertical line.
        -- The distance between horizontal lines is the given delta.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:   rg.Point
      :type length:  int
      :type delta:   int
      :type window:  rg.RoseWindow
    """
    # --------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    # TODO (continued):  IMPORTANT: Use this ITERATIVE ENHANCEMENT PLAN:
    # TODO (continued):    1. Make the sole VERTICAL line appear,
    # TODO (continued):         with thickness 3.
    # TODO (continued):    2. Make the FIRST horizontal line appear.
    # TODO (continued):    3. Make MORE horizontal lines appear,
    # TODO (continued):         each delta below the previous one.
    # TODO (continued):    4. Make each successive horizontal line
    # TODO (continued):         20 pixels longer than the previous one.
    # TODO (continued):    5. Make the right NUMBER of horizontal lines.
    # TODO (continued):    6. Make the horizontal lines each have thickness 3
    # TODO (continued):         and colors per the specified pattern.
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------
    vert_line = rg.Line(point, rg.Point(point.x, point.y + length))
    vert_line.thickness = 3
    mag_line = rg.Line(point, rg.Point(point.x + length, point.y))
    mag_line.color = 'magenta'
    mag_line.thickness = 3
    point = rg.Point(point.x, point.y + delta)
    mag2_line = rg.Line(rg.Point(point.x, point.y + 3*delta), rg.Point(point.x + length + 60, point.y +3*delta))
    mag3_line = rg.Line(rg.Point(point.x, point.y + 6 * delta), rg.Point(point.x + length + 120, point.y + 6 * delta))
    mag2_line.color = 'magenta'
    mag2_line.thickness = 3
    mag3_line.color = 'magenta'
    mag3_line.thickness = 3

    cyan_line = rg.Line(rg.Point(point.x, point.y + delta), rg.Point(point.x + length + 20, point.y +delta))
    cyan2_line = rg.Line(rg.Point(point.x, point.y + 4*delta), rg.Point(point.x + length + 80, point.y + 4*delta))
    cyan3_line = rg.Line(rg.Point(point.x, point.y + 7*delta), rg.Point(point.x + length + 140, point.y + 7*delta))
    cyan_line.color = 'cyan'
    cyan_line.thickness = 3
    cyan2_line.color = 'cyan'
    cyan2_line.thickness = 3
    cyan3_line.color = 'cyan'
    cyan3_line.thickness = 3

    vert_line.attach_to(window)
    mag_line.attach_to(window)
    mag2_line.attach_to(window)
    mag3_line.attach_to(window)
    cyan_line.attach_to(window)
    cyan2_line.attach_to(window)
    cyan3_line.attach_to(window)
    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
