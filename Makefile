install:
	pip install .

run-dev: install
	uvicorn .crewai.api.main:app --reload --host 0.0.0.0