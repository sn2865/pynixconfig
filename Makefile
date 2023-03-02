#########
# LINTS #
#########

lint:  ## run static analysis with flake8
	python3 -m black --check example_project_python linuxconfig.py
	python -m flake8 example_project_python setup.py

#########
# TESTS #
#########

test:
	python -m pytest -v linuxconfig