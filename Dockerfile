FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app/app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
ENV MAX_WORKERS=1
COPY ./src /app/app
