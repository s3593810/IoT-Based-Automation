import logging


class SenseHatApp_logging:
    logger = logging.getLogger(name='AppLogger')

    def __init__(self):
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(asctime)s:%(module)s:%(lineno)s:%(levelname)s] %(message)s'
        )
        filehandler = logging.FileHandler('SenseHatApp.log')
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)
