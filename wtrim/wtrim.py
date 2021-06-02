import os

from PIL import Image, ImageChops


def trim(image_path: str, range: int, absolute_trim_width: int = 0) -> None:

    image = Image.open(image_path)
    width, _ = image.size
    bg = Image.new('RGB', image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff_bbox = diff.convert('RGB').getbbox()
    if absolute_trim_width == 0:
        l = diff_bbox[0] - range
        t = diff_bbox[1] - range
        r = diff_bbox[2] + range
        b = diff_bbox[3] + range
        crop_range = (l, t, r, b)
    elif absolute_trim_width > 0:
        l = absolute_trim_width
        t = diff_bbox[1] - range
        r = width - absolute_trim_width
        b = diff_bbox[3] + range
        crop_range = (l, t, r, b)
    else:
        raise ValueError
    crop_image = image.crop(crop_range)
    crop_image.save('trimed-' + os.path.basename(image_path))