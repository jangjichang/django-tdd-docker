.PHONY: req
req:
	pipenv lock --requirements > requirements.txt

.PHONY: req-dev
req-dev:
	pipenv lock --dev --requirements > requirements-dev.txt

.PHONY: test
test:
	docker-compose exec movies pytest
