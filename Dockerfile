FROM python:3.10-alpine
WORKDIR /code
RUN python3 -m venv venv
COPY * /code/
RUN venv/bin/pip install -r /code/requirements.txt
EXPOSE 8008
CMD ["venv/bin/python3", "/code/main.py"]
