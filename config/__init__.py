from configparser import ConfigParser

global_config = ConfigParser(interpolation=None)
global_config.read("config/dev.ini")
