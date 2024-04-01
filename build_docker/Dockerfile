FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

#RUN python3 -i https://pypi.download.ucsb.edu/simple/ -m pip install --upgrade pip

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

#COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]
