FROM python:3.8-alpine
RUN python3.8 -m pip install flask
RUN python3.8 -m pip install flask-talisman
EXPOSE 443
EXPOSE 5050
COPY app/ /app
WORKDIR /app
CMD python3.8 main.py

