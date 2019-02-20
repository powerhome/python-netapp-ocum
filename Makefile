
setup:
	pip3 install virtualenv
	virtualenv -p python3 venv
	venv/bin/pip3 install -r requirements.txt

test:
	venv/bin/python3 setup.py test

debug:
	venv/bin/python3 debug.py

install:
	venv/bin/python3 setup.py install
