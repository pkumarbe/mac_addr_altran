FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN pip install maclookup
ENTRYPOINT ["python", "mac_addr_app.py"]
CMD [ "" ]
