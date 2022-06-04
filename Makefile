.PHONY: help start unit-tests integration-tests tests-coverage test
.DEFAULT: help

help:
	@echo "make start"
	@echo "          Run python project"
	@echo "----------"
	@echo "make unit-tests"
	@echo "          Run unit tests"
	@echo "----------"
	@echo "make integration-tests"
	@echo "          Run integration tests"
	@echo "----------"
	@echo "make tests-coverage"
	@echo "          Generate code coverage report"
	@echo "----------"
	@echo "make test"
	@echo "          Run unit tests, integration tests and generate code coverage report"
	@echo "----------"

start:
	poetry run start

unit-tests:
	poetry run pytest -vv tests/unit

integration-tests:
	poetry run pytest -vv tests/integration

tests-coverage:
	poetry run pytest --cov-report html:tests/results --cov=app tests/

test: unit-tests integration-tests tests-coverage
