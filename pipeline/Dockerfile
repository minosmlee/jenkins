FROM python:3.8 AS builder
COPY app/requirements.txt .

RUN pip3 install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./app .

ENV PATH=/root/.local:$PATH
CMD [ "python3", "./main.py" ]