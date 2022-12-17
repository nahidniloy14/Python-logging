import logging

logging.basicConfig(filename='LogReport/logdemo2.log')
logging.debug("debug executed")
logging.info("Information: ")
logging.warning("Warnings: ")
logging.error("a major error has occured")
logging.critical("Critical Issue")
