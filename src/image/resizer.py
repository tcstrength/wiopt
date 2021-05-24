from PIL import Image
import logging
import os.path
from utils.file_utils import FileUtils

class ImageResizer:
  def __init__(self, image_path: str, size_limit_kb: int, prefix: str, postfix: str):
    logging.info("")
    logging.info("Read image {}".format(image_path))

    logging.debug("Encode and decode for windows path")
    image_path = image_path.encode().decode('utf-8')

    self.path = image_path
    self.prefix = prefix
    self.postfix = postfix
    self.img = Image.open(image_path)
    self.size_limit_kb = size_limit_kb
    self.quality_limit = 10
    width, height = self.img.size

    logging.info("Image read width, height {}x{}".format(width, height))

  def resize_with_width(self, new_width):
    width, height = self.img.size
    ratio = width / height
    new_height = new_width / ratio
    return self.resize(new_width, new_height)

  def resize(self, new_width, new_height):
    width, height = self.img.size
    ratio = width / height
    new_ratio = new_width / new_height
    logging.debug("Resize image from {}x{} to {}x{} with ratio {} vs {}".format(width, height, new_width, new_height, ratio, new_ratio))

    if self.img.mode in ("RGBA", "P"): 
      logging.info("File is in RGBA mode, converting to RGB")
      self.img = self.img.convert("RGB")

    self.img.resize((new_width, new_width), Image.ANTIALIAS)

    new_path = FileUtils.get_resized_image_name(self.path, self.prefix, self.postfix)

    quality = 95

    while True:
      file = open(os.path.normpath(new_path), 'w')
      self.img.save(file, format='jpeg', optimize=True, quality=quality)
      new_file_size_kb = (int)(FileUtils.get_file_size(new_path) / 1024)

      if (new_file_size_kb <= self.size_limit_kb):
        logging.debug("File size {}KB is acceptable".format(new_file_size_kb))
        break
      elif (quality <= self.quality_limit):
        logging.debug("Quality is too low, current quality <= {}%, save file".format(self.quality_limit))
        break
      else:
        quality = quality - 5
        logging.debug("File size {}KB > {}KB, reduce quality to {}%".format(new_file_size_kb, self.size_limit_kb, quality))

    return new_path
