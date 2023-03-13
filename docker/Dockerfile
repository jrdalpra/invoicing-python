FROM python:3.9.1-slim-buster as base

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN useradd -m localuser

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && \
    apt-get update && \
    apt-get install -y libpq-dev libffi-dev libssl-dev openssl util-linux build-essential vim gdb

ENV PATH "${PATH}:/home/localuser/.local/bin"

WORKDIR /app

COPY --chown=localuser:localuser . /app
RUN chown -R localuser:localuser /app

FROM base as piptools
RUN pip install pip-tools

FROM base as requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN cd /tmp/ && pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

FROM requirements as requirementsdev
COPY ./requirements-dev.txt /tmp/requirements-dev.txt
RUN cd /tmp/ && pip install --no-cache-dir --disable-pip-version-check -r requirements-dev.txt

FROM requirementsdev as development
USER localuser

CMD ["gunicorn", "invoicing.wsgi", "--reload", "-c", "config/gunicorn.py"]
