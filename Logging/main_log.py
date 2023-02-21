import logging
import logging.handlers
import sys
import json
import logging.config
import os
import time
def filter_info_and_below(level): 
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level
    return filter

def filter_debug(level): 
    level = getattr(logging, level)
    
    def filter(record):
        return record.levelno == level
    return filter

def start_logging(): 
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
    start_logging()
    logging.info("this is info")
    logging.debug("This is debug")
    logging.warning("This is a warning")
    logging.error("This is an error")
    logging.critical("This is critical")
    print("This is a print statement")
    logger = logging.getLogger("Conditional")
    target = logging.FileHandler(filename = "conditional.log")
    #logger.addHandler(target)
    handler = logging.handlers.MemoryHandler(100, flushLevel = logging.ERROR, target = target, flushOnClose=False)
    logger.addHandler(handler)
    logger.info("New info 1")
    logger.debug("New debug 1")
    logger.warning("new warning 1")
    #logger.error("new error")
    print("Shouldn't have logged conditionally")
    handler.close()
