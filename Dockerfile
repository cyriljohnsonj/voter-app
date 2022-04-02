FROM python:3.8-alpine

RUN adduser -D worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . .

COPY main.py /home/worker
COPY templates /home/worker/templates
COPY static /home/worker/static

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
