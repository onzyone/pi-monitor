import os 
import sys 
import logging.config 
import ConfigParser 
from yaml import load 
  
class PropertiesHelper(): 
      
    def set_logger(self, conf_file): 
        try: 
            if conf_file is not None: 
                logging.config.dictConfig(conf_file) 
        except: 
            print "Error setting up logging: ", sys.exc_info()[0] 
  
    def get_yaml_config(self, *args, **kwargs): 
          
        self.default_config_file = kwargs.get('default_config_file', None) 
        self.use_override = kwargs.get('use_override', True) 
        self.filename = kwargs.get('filename', None) 
        
        config = None
        try: 
            if not self.default_config_file: 
                default_config_file = os.path.join(__file__[:__file__.rfind('lib')], 'config', self.filename)  
            conf_file = None
            # override 
            if self.use_override and os.path.exists(os.path.join(os.getenv("HOME"), 'config', self.filename)): 
                conf_file = os.path.join(os.getenv("HOME"), 'config', self.filename) 
            elif default_config_file is not None and os.path.exists(default_config_file): 
                conf_file = default_config_file 
            if conf_file is not None: 
                config = load(open(conf_file, 'r')) 
            return config 
        except: 
            print "Error loading yaml config: ", sys.exc_info()[0] 
            raise
              
    def get_configparser_config(self, *args, **kwargs): 
  
        self.filename = kwargs.get('filename', None) 
        self.section = kwargs.get('section', None) 
        
        config = None
        try: 
            if not self.default_config_file: 
                default_config_file = os.path.join(__file__[:__file__.rfind('lib')], 'config', self.filename)  
            conf_file = None
            # override 
            if self.use_override and os.path.exists(os.path.join(os.getenv("HOME"), 'config', self.filename)): 
                conf_file = os.path.join(os.getenv("HOME"), 'config', self.filename) 
            elif default_config_file is not None and os.path.exists(default_config_file): 
                conf_file = default_config_file 
            if conf_file is not None: 
                config = ConfigParser.SafeConfigParser() 
                config.read(self.propertiesFile) 
                propertiesDict = dict(config._sections[self.section], raw=True) 
            return propertiesDict 
        except: 
            print "Error loading configparser config: ", sys.exc_info()[0] 
            raise