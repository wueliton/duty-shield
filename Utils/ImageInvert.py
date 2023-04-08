from PIL import ImageEnhance, Image as Img, ImageOps


class ImageInvert:
    @staticmethod
    def invert(image: Img.Image):
        img = image.convert("RGBA")
        r, g, b, a = img.split()
        r, g, b = map(ImageOps.invert, (r, g, b))
        img = Img.merge("RGBA", (r, g, b, a))
        return img
