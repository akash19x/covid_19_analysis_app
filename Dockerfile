FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev \
    && pip install cython

RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "covid19_india_analysis.py" ]
