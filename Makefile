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
	@echo 'migrations ......................... create new migrations'
	@echo 'migrate ............................ apply existing migrations'
	@echo 'superuser .......................... create a superuser to test the app'
	@echo 'shell .............................. run a "sh" inside the "web" container'
	@echo ''


requirements_output = requirements.txt requirements-dev.txt

requirements-dev.txt: requirements.txt

$(requirements_output): %txt: %in
	@docker-compose run --rm piptools pip-compile -v --generate-hashes --no-emit-index-url --no-header --output-file $@ $<

env:
	@cp .env-sample .env

test:
	@./bin/run.sh pytest -vv

static:
	@./bin/run.sh python manage.py collectstatic --no-input

run: migrations migrate static
	@docker-compose up web

migrations:
	@./bin/run.sh python manage.py makemigrations

migrate:
	@./bin/run.sh python manage.py migrate

superuser:
	@./bin/run.sh python manage.py createsuperuser

shell:
	@./bin/run.sh sh

django-shell:
	@./bin/run.sh python manage.py shell

.PHONY: requirements-dev.txt requirements.txt