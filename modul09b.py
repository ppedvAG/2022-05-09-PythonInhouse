import logging

# Erstellt einen eigenen Logger mit Namen 09b Logger
logger = logging.getLogger("09b Logger")
logger.debug("blabla")

# Kann nicht über absicConfig konfiguriert werden
# Brauchen dafür Handler

# Haben die Log-Datei und den log-Stream erstellt
c_handler = logging.StreamHandler() # Gibt in der Konsole aus
f_handler = logging.FileHandler("09b.log") # Gibt in der Datei aus
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Anpassen des Formats
c_format = logging.Formatter("%(name)s %(levelname)s %(process)d %(asctime)s - %(message)s")
f_format = logging.Formatter("%(name)s %(levelname)s %(process)d %(asctime)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Hinzufügen der Handler zum logger

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("Warnung")
logger.debug("Debug")
logger.critical("Kritisch")




