import logging
import inspect
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
  pass












#   def getLogger(self):
#     loggerName= inspect.stack()[1][3]
#     logger=logging.getLogger(loggerName)
#     fileHandler=logging.FileHandler('logfile.log')
#     formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
#     fileHandler.setFormatter(formatter)
#     logger.addHandler(fileHandler)  #filehandler objects
#     logger.setLevel(logging.DEBUG)
#     return logger
  