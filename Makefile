install:
	pip install .
run-api: install
	python examples/api.py
run-api-dev: install
	python crewai/__init__.py