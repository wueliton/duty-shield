from PIL import ImageEnhance, Image as Img


class ImageAlpha:
    @staticmethod
    def alpha(image: Img.Image, opacity: float = 1):
        transparent_image = image.copy()
        alpha = transparent_image.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        transparent_image.putalpha(alpha)
        return transparent_image
