
setup:
	pip3 install virtualenv
	virtualenv -p python3 venv
	venv/bin/pip3 install -r requirements.txt
	
	# For publishing releases
	venv/bin/pip3 install twine

clean:
	-rm -rf build dist

build:
	venv/bin/python3 setup.py sdist bdist_wheel

test:
	venv/bin/python3 setup.py test

debug:
	venv/bin/python3 debug.py

release:
	venv/bin/python3 -m twine upload dist/*

install:
	venv/bin/python3 setup.py install
