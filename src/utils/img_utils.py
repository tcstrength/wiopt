from PIL import Image

class ImgUtils:
  def get_image_size(path: str):
    path = path.encode().decode('utf-8')
    img = Image.open(path)
    return img.size