FROM python:3.11

WORKDIR /home/

RUN echo "just for initiation institutions!"

RUN git clone https://github.com/chunccc1004/Pinterest.git

WORKDIR /home/Pinterest/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=Pinterest.settings.deploy && python manage.py migrate --settings=Pinterest.settings.deploy && gunicorn Pinterest.wsgi --env DJANGO_SETTINGS_MODULE=Pinterest.settings.deploy --bind 0.0.0.0:8000"]