from cmath import log
import logging

logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="w",
                    format="%(levelname)s %(process)d %(asctime)s - %(message)s",
                    datefmt="%d-%m-%Y %H:%M:%S")

logging.debug("Ich werde im log eingetragen")

def say_hello():
    logging.info("Die Funktion say_hello wurde aufgerufen")
    print("Hello")
    

say_hello()

# Stufen im logger:
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG

logging.critical("Kritischer Fehler festgestellt")
logging.warning("warning")
logging.error("Fehler")