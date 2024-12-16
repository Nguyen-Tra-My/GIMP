from gimpfu import *

def auto_enhance(image, drawable):
    # Tăng độ sáng và độ tương phản
    pdb.gimp_brightness_contrast(drawable, 10, 30)
    # Điều chỉnh đường cong màu
    pdb.gimp_curves_spline(drawable, HISTOGRAM_VALUE, 4, [0, 0, 64, 80, 192, 192, 255, 255])

register(
    "python_fu_auto_enhance",
    "Auto Enhance Image",
    "Automatically enhance the image quality",
    "Your Name",
    "Your License",
    "2024",
    "<Image>/Filters/Enhance/Auto Enhance...",
    "*",
    [],
    [],
    auto_enhance)

main()
