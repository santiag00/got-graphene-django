FROM python:3.6.2

RUN pip install virtualenv && \
  virtualenv /opt/venv && \
  /bin/bash -c "source /opt/venv/bin/activate"

ENV PATH="/opt/venv/bin:${PATH}"

WORKDIR /app

RUN apt-get update && apt-get install -y sqlite3
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", \
     "/app/manage.py", \
     "runserver", \
     "0.0.0.0:80" ]
