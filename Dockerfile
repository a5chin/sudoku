ARG VARIANT=3.12
FROM python:${VARIANT}

WORKDIR /opt
COPY pyproject.toml requirements.lock ./

# hadolint ignore=DL3013,DL3042
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock

WORKDIR /

COPY ./app /app
COPY ./entrypoint.sh /


RUN chmod 755 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

ENV PYTHONUNBUFFERED True

EXPOSE 8080
