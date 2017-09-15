FROM wakeup706/rpi-python-opencv:latest

RUN pip install paho-mqtt

WORKDIR /data
CMD [ "bash" ]
