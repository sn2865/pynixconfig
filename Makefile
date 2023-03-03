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