FROM python:3.10.12

WORKDIR /app

COPY . .

RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip \
    && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
