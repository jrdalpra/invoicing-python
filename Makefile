USERID=$(shell id -u)
GROUPID=$(shell id -g)

help:
	@echo ''
	@echo 'Available commands:'
	@echo ''
	@echo 'requirements.txt ................... compile requirements.txt using pip-compile'
	@echo 'requirements-dev.txt ............... compile requirements-dev.txt using pip-compile'
	@echo 'env ................................ create environment specific files'
	@echo 'test ............................... run all tests'
	@echo 'run ................................ execute the web application'
	@echo ''


requirements_output = requirements.txt requirements-dev.txt

requirements-dev.txt: requirements.txt

$(requirements_output): %txt: %in
	@docker-compose run --rm piptools pip-compile -v --generate-hashes --no-emit-index-url --no-header --output-file $@ $<

env:
	@cp .env-sample .env

test:
	@./bin/run.sh pytest -vv

run:
	@docker-compose up runtime