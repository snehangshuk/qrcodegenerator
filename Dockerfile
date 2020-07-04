FROM python:3
MAINTAINER: Snehangshu Karmakar <snehangshu@gmail.com>
ADD qrcode.py /
RUN pip install pystrich
CMD [ "python", "./qrcode.py" ]