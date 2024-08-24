import atexit
import json
import logging
import logging.config
import pathlib

            
def setup_logging():
    config_file = pathlib.Path("logging_config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)

    start_queue_listener()


def start_queue_listener():
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.handlers.QueueHandler):
            handler.listener.start()
            atexit.register(handler.listener.stop)

logger = logging.getLogger("my_app")


setup_logging()




def main():
    logger.debug("Debug message", extra={"x": "hello"})
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Exception message")


if __name__ == "__main__":
    main()