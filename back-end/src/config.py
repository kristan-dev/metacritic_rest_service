#%%
import logging
import yaml
import os

#if you want to utilize a config file try this.

def parse_config():
    config_path = "conf/config.yml"
    # current_path = os.path.dirname(os.path.abspath(__file__))
    with open(config_path) as file:
        cfg = yaml.load(file, Loader=yaml.FullLoader)

    return cfg

cfg = parse_config()
pass

# uncomment to test
# webdriver_config = cfg['webdriver']['phantomjs']['macos']
# pass
