all: install

.PHONY: install
install:
	@poetry install

.PHONY: package-install
package-install:
	@pip install --user --index-url https://test.pypi.org/simple/ \
	    --extra-index-url https://pypi.org/simple/ altvec-page-loader

.PHONY: lint
lint:
	@poetry run flake8 page_loader

.PHONY: test
test:
	@poetry run pytest -v

build: lint test
	@poetry build

.PHONY: publish
publish:
	@poetry publish -r test-repo

.PHONY: all build
