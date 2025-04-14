FROM python:3.12.1-slim AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry-home"\
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc && \
    apt-get clean

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Definir diretório de trabalho
WORKDIR $PYSETUP_PATH

# Copiar arquivos de dependência # importante para evitar erro do poetry
COPY poetry.lock pyproject.toml ./
COPY README.md ./  

# Instalar dependências sem pacotes de dev
RUN poetry install --no-root

# Definir pasta da aplicação
WORKDIR /app

# Copiar todo o restante do projeto
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
