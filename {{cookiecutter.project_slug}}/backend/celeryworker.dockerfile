FROM python:3.7

WORKDIR /app/

# Install Poetry
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && \
#     poetry config virtualenvs.create false

# RUN curl -sSL https://install.python-poetry.org | python - && #| POETRY_HOME=/opt/poetry python && \
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && \
#     poetry config virtualenvs.create false

# RUN curl -sSL https://install.python-poetry.org | python - #| POETRY_HOME=/opt/poetry python && \
    # cd /usr/local/bin && \
    # ln -s /opt/poetry/bin/poetry && \
    # poetry config virtualenvs.create false

# RUN curl https://install.python-poetry.org | python
# RUN cd /usr/local/bin && \
# RUN ln -s /opt/poetry/bin/poetry && \
# RUN poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
# COPY ./app/pyproject.toml ./app/poetry.lock* /app/
COPY ./app/requirements.txt /app/requirements.txt

# Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false
# RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
# ARG INSTALL_JUPYTER=false
# RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"

ENV C_FORCE_ROOT=1

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

COPY ./app/worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD ["bash", "/worker-start.sh"]
