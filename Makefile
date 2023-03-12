#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python -m pip install -e .[develop]

build:  ## build the python library
	python setup.py build build_ext --inplace

install:  ## install library
	python -m pip install .
	
#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python -m black --check scripts setup.py
	python -m flake8 scripts setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black scripts/ setup.py

#########
# TESTS #
#########

test:
	python -m pytest -v scripts/tests

coverage:  ## clean and run unit tests with coverage
	python -m pytest -v scripts/tests --cov=scripts --cov-branch --cov-fail-under=50 --cov-report term-missing