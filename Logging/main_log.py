import logging
import sys
import json
import logging.config
import os
def filter_info_and_below(level): 
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level
    return filter

json_config = 'log_config.json'
if (os.path.exists(json_config)):
    with open(json_config, 'rt') as f: 
        config = json.load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(filename="main.log", level=logging.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

'''
console = logging.StreamHandler()
console.setLevel(logging.WARNING)

formatter = logging.Formatter('%(name)s: %(levelname)s - %(message)s')
console.setFormatter(formatter)

#add stream handler to root logger
logging.getLogger('').addHandler(console)
'''


if __name__ == '__main__':
    logging.info("this is info")
    logging.debug("This is debug")
    logging.warning("This is a warning")
    logging.error("This is an error")
    logging.critical("This is critical")
    print("This is a print statement")