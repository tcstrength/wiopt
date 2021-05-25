from PIL import Image
import logging
import os.path
import piexif
from utils.file_utils import FileUtils

class ImageResizer:
  def __init__(self, image_path: str, size_limit_kb: int, prefix: str, postfix: str, metadata: dict):
    logging.info("")
    logging.info("Read image {}".format(image_path))

    logging.debug("Encode and decode for windows path")
    image_path = image_path.encode().decode('utf-8')

    self.path = image_path
    self.prefix = prefix
    self.postfix = postfix
    self.metadata = metadata
    self.img = Image.open(image_path)
    self.size_limit_kb = size_limit_kb
    self.quality_limit = 10
    width, height = self.img.size

    logging.info("Image read width, height {}x{}".format(width, height))

  @staticmethod
  def string_to_tuple(str):
    t = list(str.encode("utf-16"))
    t.pop(0)
    t.pop(0)
    return tuple(t)

  def mk_exif_from_metadata(self):
    title = self.metadata['image_title']
    comments = self.metadata['image_comments']
    authors = self.metadata['image_authors_copyright']
    subject = self.metadata['image_subject']

    zeroth = {
      piexif.ImageIFD.XPTitle: ImageResizer.string_to_tuple(title),
      piexif.ImageIFD.XPComment: ImageResizer.string_to_tuple(comments),
      piexif.ImageIFD.XPSubject: ImageResizer.string_to_tuple(subject),
      piexif.ImageIFD.XPKeywords: ImageResizer.string_to_tuple(title),
      piexif.ImageIFD.ImageDescription: title.encode('utf-8'),
      piexif.ImageIFD.Artist: authors.encode('utf-8'),
      piexif.ImageIFD.Copyright: authors.encode('utf-8'),
      piexif.ImageIFD.XPAuthor: ImageResizer.string_to_tuple(authors),
      piexif.ImageIFD.Rating: 5,
      piexif.ImageIFD.RatingPercent: 99
    }

    exif_dict = {
        "0th": zeroth, 
        "Exif": dict(), 
        "GPS": dict(), 
        "1st": dict(), 
        "thumbnail":None
    }

    exif_bytes = piexif.dump(exif_dict)

    return exif_bytes

  def resize_with_width(self, new_width):
    width, height = self.img.size
    ratio = width / height
    new_height = new_width / ratio
    return self.resize(new_width, new_height)

  def resize(self, new_width, new_height):
    new_width = (int)(new_width)
    new_height = (int)(new_height)
    width, height = self.img.size
    ratio = width / height
    new_ratio = new_width / new_height

    logging.debug("Resize image from {}x{} to {}x{} with ratio {} vs {}".format(width, height, new_width, new_height, ratio, new_ratio))

    if self.img.mode in ("RGBA", "P"): 
      logging.info("File is in RGBA mode, converting to RGB")
      self.img = self.img.convert("RGB")

    self.img = self.img.resize((new_width, new_height), Image.ANTIALIAS)

    new_path = FileUtils.get_resized_image_name(self.path, self.prefix, self.postfix)
    new_path = os.path.normpath(new_path)
    base_dir = os.path.dirname(new_path)

    FileUtils.mkdir_ine(base_dir)

    logging.debug("Write new image to {}".format(new_path))

    quality = 100

    while True:
      self.img.save(new_path, format='jpeg', quality=quality, exif=self.mk_exif_from_metadata())
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
