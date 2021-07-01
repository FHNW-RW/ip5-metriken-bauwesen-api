FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# install requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/

# copy required code
COPY ./app /app/app
COPY ./src /app/src
COPY ./models /app/models
COPY ./transformer /app/transformer
