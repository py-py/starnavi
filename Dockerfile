FROM python:3.6-alpine

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x boot.sh

ENV ENVIRONMENT dev

CMD ./boot.sh

# docker build -t starnavi . --no-cache
# docker run --name starnavi -d -p 8000:8000 starnavi
