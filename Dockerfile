FROM python:3.11-slim
ENV PIP_THREADS=1

WORKDIR /tasc_client

COPY requirements.txt .
# --progress-bar off need to prevent error "can't create new thread" on low versions docker
RUN python -m pip install -U --progress-bar off pip && \
    pip install --no-cache-dir -r requirements.txt --progress-bar off --default-timeout=100

COPY . .
RUN chmod a+x ci/docker/*.sh

CMD ["bash", "ci/docker/app.sh"]
