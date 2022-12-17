import logging

logging.basicConfig(format='%(asctime)s :%(levelname)s :%(message)s',
                    datefmt='%d/%m/%y %I:%M:%S %A', #%H in place of %I to see the time in 24h format
                    level=logging.DEBUG,
                    filename='LogReport/logFormat.log',
                    filemode='w') # w >>to override a >>append


logging.debug("debug executed")
logging.info("Information: ")
logging.warning("Warnings: ")
logging.error("a major error has occured")
logging.critical("Critical Issue")


#OUTPUT:
#previous records will be erased