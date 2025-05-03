install:
	uv sunc

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*whl