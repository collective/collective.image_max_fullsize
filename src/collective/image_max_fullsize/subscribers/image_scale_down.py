# -*- coding: utf-8 -*-

from plone.app.contenttypes.interfaces import IImage
from plone.scale.scale import scaleImage

import transaction as zt


def handler(obj, event=None):
    """
    """
    max_width = 1900
    max_height = 1900
    max_size = 1048576  # 1048576 == 1MB
    if not IImage.providedBy(obj):
        return

    if obj.image.size <= max_size:
        print("image size lower than max_size: {}".format(max_size))
        return

    image_dimensions = obj.image.getImageSize()
    if image_dimensions[0] < max_width and image_dimensions[1] < max_height:
        print("image dimensions smaler than: {}x{}".format(max_width, max_height))
        return

    data = obj.image.data
    result = scaleImage(
        data, width=max_width, height=max_height, direction="down", quality=90
    )
    obj.image._setData(result[0])
    print("Image scaled down to {0}KB / {1}".format(obj.image.size / 1024, result[2]))
    zt.commit()
