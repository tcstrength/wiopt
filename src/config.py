import json
import logging

class Config:

  _CONFIG_PATH = 'config.json'

  def read():
    default_conf = {
      'max_size_kb': '200',
      'standard_width': '1200',
      'last_open_path': '',
      'last_prefix': 'resized_',
      'last_postfix': ''
    }
    
    try:
      conf = json.load(open(Config._CONFIG_PATH, 'r'))
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
    