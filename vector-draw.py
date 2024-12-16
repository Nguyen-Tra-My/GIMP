from gimpfu import *

def draw_vector_line(image, drawable, x1, y1, x2, y2):
    pdb.gimp_paintbrush_default(drawable, 4, [x1, y1, x2, y2]) # Vẽ đường thẳng vector

register(
    "python_fu_draw_vector_line",
    "Draw Vector Line",
    "Draw a vector line on the image",
    "Your Name",
    "Your License",
    "2024",
    "<Image>/Tools/Draw Vector Line...",
    "*",
    [
        (PF_INT, "x1", "X1 coordinate", 0),
        (PF_INT, "y1", "Y1 coordinate", 0),
        (PF_INT, "x2", "X2 coordinate", 100),
        (PF_INT, "y2", "Y2 coordinate", 100),
    ],
    [],
    draw_vector_line)

main()
