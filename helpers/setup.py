from setuptools import setup

setup(
    name="ppedv_inhouse_test_package",
    version="0.0.3",
    url="https://ppedv.de",
    description="Ein Testupload zur Packageerstellung",
    author="Marius Sommer",
    py_modules=["greeters", "mathstuff"]
)


# pip install twine
# Zum uploaden
# Konsolenbefehl für den Upload:
# twine upload -r testpypi dist/*
# Für upload auf "richtige" Siete
# twine upload -r pypi dist/*