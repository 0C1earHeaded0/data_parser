FROM python

ARG SCRIPTS_DIR=python_scripts
RUN mkdir -p ${SCRIPTS_DIR}
WORKDIR ${SCRIPTS_DIR}

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install psycopg2-binary

COPY . .