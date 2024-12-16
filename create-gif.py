from gimpfu import *

def create_gif(image, drawable, delay):
    num_layers = pdb.gimp_image_get_layers(image)[0]
    layers = pdb.gimp_image_get_layers(image)[1]
    for layer in layers:
        pdb.gimp_image_set_active_layer(image, layer)
        pdb.gimp_layer_set_visible(layer, TRUE)
        pdb.gimp_item_transform_flip_simple(layer, ORIENTATION_HORIZONTAL, TRUE, 0)
    
    pdb.file_gif_save(image, drawable, "/tmp/animated.gif", "/tmp/animated.gif", 1, 0, delay, 0)

register(
    "python_fu_create_gif",
    "Create GIF Animation",
    "Create an animated GIF from layers",
    "Your Name",
    "Your License",
    "2024",
    "<Image>/File/Create/Animation/Create GIF...",
    "*",
    [
        (PF_INT, "delay", "Delay between frames (ms)", 100),
    ],
    [],
    create_gif)

main()
