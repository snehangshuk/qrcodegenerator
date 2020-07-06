FROM python:3.8

MAINTAINER Snehangshu Karmakar "snehangshu@gmail.com"


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./qrcode-gen-img /app/qrcode-gen-img

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
