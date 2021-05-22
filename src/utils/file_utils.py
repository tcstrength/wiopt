import os
import logging
from os import listdir, stat
from os.path import isfile, join

import subprocess
import sys


class UnsupportedPlatformException(Exception):
    pass


def _show_file_darwin(path: str):
    subprocess.check_call(["open", "--", path])

def _show_file_linux(path: str):
    subprocess.check_call(["xdg-open", "--", path])

def _show_file_win32(path: str):
    subprocess.check_call(["explorer", "/select", path])

_show_file_func = {'darwin': _show_file_darwin, 
                   'linux': _show_file_linux,
                   'win32': _show_file_win32}

class FileUtils:
  @staticmethod
  def get_resized_image_name(file_location: str, prefix: str, postfix: str):
    filename = file_location.split('/')[-1]
    location = file_location.split('/')[0:-1]
    filename = filename.split('.')
    filename[0] += postfix
    filename[0] = prefix + filename[0]
    filename = '.'.join(filename)
    new_path = '/'.join(location) + '/' + filename
    return new_path

  @staticmethod
  def get_file_size(path: str):
    stats = os.stat(path)
    return stats.st_size

  @staticmethod
  def get_file_ext(path: str):
    _,tail = os.path.splitext(path)

    if tail != '':
      return tail[1:].lower()

    return tail

  @staticmethod
  def get_file_name(path: str):
    _,tail = os.path.split(path)
    return tail

  @staticmethod
  def is_image(path: str):
    image_exts = ['bmp', 'jpg', 'jpeg', 'png', 'webp', 'tiff']
    ext = FileUtils.get_file_ext(path)

    if ext in image_exts:
      return True

    return False

  @staticmethod
  def list_images_with_stats(path: str, ignore_prefix: str):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return_stats = list()

    for f in files:
      f = os.path.join(path, f)

      if (FileUtils.is_image(f) == False):
        logging.debug('File is not an image {}'.format(f))
        continue

      name = FileUtils.get_file_name(f)

      logging.debug('Check file name starts with {}'.format(ignore_prefix))
      if (ignore_prefix != '' and name.startswith(ignore_prefix)):
        logging.debug('File {} starts with {}, ignored'.format(name, ignore_prefix))
        continue

      logging.debug('Get stat of file {}'.format(f))

      file_stat = {
        'sizeKB': int(FileUtils.get_file_size(f) / 1024),
        'name': name,
        'format': FileUtils.get_file_ext(f),
        'path': f
      }

      logging.debug('Stats returned {}'.format(file_stat))

      return_stats.append(file_stat)

    return return_stats

  show_file = _show_file_func[sys.platform]