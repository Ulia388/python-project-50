install:
	uv sunc

gendiff -h:
	uv run gendiff -h

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*whl