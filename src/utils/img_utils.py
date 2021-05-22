from PIL import Image

class ImgUtils:
  def get_image_size(path):
    img = Image.open(path)
    return img.size