FROM python:3.6-alpine3.7
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN apk add py-pip
RUN apk add --no-cache python3-dev
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install numpy
RUN pip --no-cache-dir install -r requirements.txt
CMD ["python3", "app.py"]