
# Setup for local testing
setup:
	-rm -rf venv # Start with a fresh venv if one exists

	pip3 install virtualenv
	virtualenv -p python3 venv
	venv/bin/pip3 install -r requirements.txt

# Setup for local development
setup_dev:
	venv/bin/pip3 install -r requirements-dev.txt

clean:
	-rm -rf build dist

# Build a source distribution
build:
	venv/bin/python3 setup.py sdist bdist_wheel

# Publish a release to PyPi
# NOTE: This depends on having a correctly configured ~/.pypirc
# NOTE: https://docs.python.org/3.7/distutils/packageindex.html
release:
	venv/bin/python3 -m twine upload dist/*

test:
	venv/bin/python3 setup.py test

# For local debugging (this script ignored by git)
debug:
	venv/bin/python3 debug.py

install:
	venv/bin/python3 setup.py install
