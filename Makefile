all: install

install:
	@poetry install

package-install:
	@pip install --user --index-url https://test.pypi.org/simple/ \
	    --extra-index-url https://pypi.org/simple/ altvec-page-loader

lint:
	@poetry run flake8 page_loader

test:
	@poetry run pytest -v

build: lint test
	@poetry build

publish:
	@poetry publish -r testing

.PHONY: all install package-install lint test build publish
