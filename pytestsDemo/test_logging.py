import logging
def test_logging():
  logger = logging.getLogger(__name__)

  filehandler = logging.FileHandler("logfile.log")
  formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s:")
  filehandler.setFormatter(formatter)

  logger.setLevel(logging.INFO)
  logger.addHandler(filehandler)
  logger.debug("A debug statement")
  logger.info("The information statement")
  logger.warning("The warning statement")
  logger.error("The error statement")
  logger.critical("The critical issue")