FROM wakeup706/rpi-python-opencv:latest
RUN [ "cross-build-start" ]

RUN pip install paho-mqtt

WORKDIR /data
CMD [ "bash" ]
