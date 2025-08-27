install:
	uv sunc

gendiff:
	uv run gendiff 

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*whl

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
	
check: 
	test lint


.PHONY: install lint build test