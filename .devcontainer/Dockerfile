FROM debian:bookworm-slim as builder

WORKDIR /opt

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

COPY ./.python-version ./pyproject.toml ./requirements* ./
RUN rye pin "$(cat .python-version)" && \
    rye sync


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm
COPY --from=builder /opt/rye /opt/rye

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"
ENV PYTHONUNBUFFERED True

RUN rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

# hadolint ignore=DL3008,DL3009
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg

# [ref] https://cloud.google.com/sdk/docs/install?hl=ja#deb
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# hadolint ignore=DL3008,DL3009
RUN apt-get update && \
    apt-get install -y --no-install-recommends\
        google-cloud-cli \
        google-cloud-sdk-gke-gcloud-auth-plugin

RUN chown -R vscode $RYE_HOME
