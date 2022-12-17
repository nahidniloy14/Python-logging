
import logging

logging.basicConfig(format='%(asctime)s :%(levelname)s :%(message)s',
                    datefmt='%d/%m/%y %I:%M:%S %p %A', #%H in place of %I to see the time in 24h format
                    level=logging.DEBUG,
                    filename='LogReport/logFormat.log')


logging.debug("debug executed")
logging.info("Information: ")
logging.warning("Warnings: ")
logging.error("a major error has occured")
logging.critical("Critical Issue")

""""
# 17/12/22 10:26:53 Saturday :DEBUG :debug executed
# 17/12/22 10:26:53 Saturday :INFO :Information: 
# 17/12/22 10:26:53 Saturday :WARNING :Warnings: 
# 17/12/22 10:26:53 Saturday :ERROR :a major error has occured
# 17/12/22 10:26:53 Saturday :CRITICAL :Critical Issue
"""
