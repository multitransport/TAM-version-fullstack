FROM python:3.8-slim-buster
WORKDIR /tam
ADD . /tam
RUN pip install -r requirements.txt
CMD ["python3", "run.py"]
