FROM ubuntu:18.04

RUN apt-get update -y \
    && apt-get install tesseract-ocr -y \
    && apt-get install software-properties-common -y

RUN add-apt-repository ppa:ubuntuhandbook1/apps -y \
    && apt-get update -y \
    && apt-get install mupdf mupdf-tools -y

RUN apt-get -y install python3-pip \
    && pip3 install pip --upgrade \
    && apt-get clean \
    && apt-get autoremove

ADD . /home/App
WORKDIR /home/App
COPY requirements.txt ./
COPY . .

RUN pip3 install -r requirements.txt

VOLUME ["./data"]

CMD ["python3", "dodfminer"]
