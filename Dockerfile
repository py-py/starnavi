FROM python:3.6-alpine

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x boot.sh

ENV ENVIRONMENT prod

CMD ./boot.sh

# docker build -t starnavi .
# docker run -d -p 8000:8000 starnavi
