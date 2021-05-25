import json
import logging

class Config:

  _CONFIG_PATH = 'config.json'

  def default(conf, key, value):
    if not (key in conf.keys()):
      logging.debug('Set default value for previous version config {}={}'.format(key, value))
      conf[key] = value
    return conf

  def read():
    default_conf = {
      'max_size_kb': '200',
      'standard_width': '1200',
      'last_open_path': '',
      'save_dir': 'output',
      'image_title': '',
      'image_subject': '',
      'image_comments': '',
      'image_authors_copyright': '',
      'window_width': '600',
      'window_height': '600'
    }
    
    try:
      conf = json.load(open(Config._CONFIG_PATH, 'r'))
      conf = Config.default(conf, 'save_dir', 'output')
      conf = Config.default(conf, 'image_title', '')
      conf = Config.default(conf, 'image_subject', '')
      conf = Config.default(conf, 'image_comments', '')
      conf = Config.default(conf, 'image_authors_copyright', '')
      conf = Config.default(conf, 'window_width', '600')
      conf = Config.default(conf, 'window_height', '600')
    except:
      logging.debug('Load default config')
      conf = default_conf

    logging.debug('Config load')
    return conf

  def write(key: str, value):
    conf = Config.read()
    logging.debug("Convert value to str(value)")
    conf[key] = str(value)
    logging.debug('Write config {}'.format(conf))
    json.dump(conf, open(Config._CONFIG_PATH, 'w'))
    return conf
    