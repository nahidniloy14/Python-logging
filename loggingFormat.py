
import logging

logging.basicConfig(format='%(asctime)s :%(levelname)s :%(name)s :%(message)s',
                    datefmt='%d/%m/%y %I:%M:%S',
                    level=logging.DEBUG,
                    filename='LogReport/logFormat.log')
logging.debug("debug executed")
logging.info("Information: ")
logging.warning("Warnings: ")
logging.error("a major error has occured")
logging.critical("Critical Issue")
#
# 17/12/22 10:19:06 :DEBUG :root :debug executed
# 17/12/22 10:19:06 :INFO :root :Information:
# 17/12/22 10:19:06 :WARNING :root :Warnings:
# 17/12/22 10:19:06 :ERROR :root :a major error has occured
# 17/12/22 10:19:06 :CRITICAL :root :Critical Issue
