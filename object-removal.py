from gimpfu import *

def remove_object(image, drawable, x, y, width, height):
    pdb.gimp_selection_rectangle(image, CHANNEL_OP_REPLACE, x, y, width, height)
    pdb.plug_in_resynthesizer(image, drawable, x, y, width, height, 3, 0.2, 0.5, 0.2, 0.2) # Sử dụng Resynthesizer để loại bỏ đối tượng

register(
    "python_fu_remove_object",
    "Remove Object",
    "Remove an unwanted object from the image",
    "Your Name",
    "Your License",
    "2024",
    "<Image>/Filters/Remove Object...",
    "*",
    [
        (PF_INT, "x", "X coordinate", 0),
        (PF_INT, "y", "Y coordinate", 0),
        (PF_INT, "width", "Width of object", 50),
        (PF_INT, "height", "Height of object", 50),
    ],
    [],
    remove_object)

main()
