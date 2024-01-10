install:
	pip install .
run-api: install
	python examples/api.py
run-dev: install
	uvicorn .crewai.api:app --reload --host 0.0.0.0