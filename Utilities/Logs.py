import logging


class Log:
    @staticmethod
    def logger():
        # setup logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='.\\TestExecution_Logs\\automation.log', mode='a')
        handler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # add formatter to handler
        handler.setFormatter(formatter)

        # add handler to logger
        logger.addHandler(handler)

        return logger
