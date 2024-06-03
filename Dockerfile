ARG VARIANT=3.12
FROM python:${VARIANT} as builder

ENV PYTHONDONTWRITEBYTECODE True

WORKDIR /opt
COPY pyproject.toml requirements.lock ./

# hadolint ignore=DL3013,DL3042
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock


FROM python:${VARIANT}-slim
COPY --from=builder /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

ENV PYTHONUNBUFFERED True

WORKDIR /

COPY ./app /app
COPY ./entrypoint.sh /

RUN chmod 755 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

EXPOSE 8080
