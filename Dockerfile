# set base image (host OS)
FROM python:rc-alpine

RUN apk --no-cache add mosquitto
RUN apk add curl
# Install nodejs for the dashboard
#RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apk add --update npm
RUN npm install -g serve
RUN apk add git
RUN apk add tzdata
RUN apk add musl-utils
RUN apk add xsel

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY GivTCP/ ./GivTCP
COPY WebDashboard/ ./WebDashboard

COPY startup.py startup.py

ENV NUMINVERTERS=1
ENV INVERTER_IP_1="10.0.0.111"
ENV NUMBATTERIES_1=2
ENV MQTT_OUTPUT="True"
ENV MQTT_ADDRESS="127.0.0.1"
ENV MQTT_USERNAME=""
ENV MQTT_PASSWORD=""
ENV MQTT_TOPIC=""
ENV MQTT_PORT=1883
ENV LOG_LEVEL="Error"
ENV DEBUG_FILE_LOCATION=""
ENV PRINT_RAW=True
ENV SELF_RUN=True
ENV SELF_RUN_LOOP_TIMER=5
ENV INFLUX_OUTPUT=False
ENV INFLUX_URL=""
ENV INFLUX_TOKEN=""
ENV INFLUX_BUCKET=""
ENV INFLUX_ORG=""
ENV HA_AUTO_D=True
ENV HADEVICEPREFIX="GivTCP"
ENV PYTHONPATH="/app"
ENV DAYRATE=0.138
ENV NIGHTRATE=0.05
ENV EXPORTRATE=0.041
ENV HOSTIP="10.0.0.230"
ENV DAYRATESTART="04:30"
ENV NIGHTRATESTART="00:30"
ENV TZ="Europe/London"
ENV WEB_DASH=False
ENV WEB_DASH_PORT=3000
ENV SMARTTARGET=True
ENV GEAPI=""
ENV SOLCASTAPI=""
ENV SOLCASTSITEID=""

EXPOSE 6345 1883 3000

CMD ["python3", "/app/startup.py"]