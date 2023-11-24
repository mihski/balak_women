FROM  python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt install iputils-ping -y

RUN   pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

RUN python manage.py collectstatic

#CMD ["python","manage.py","runserver","0.0.0.0:9000"] 

#CMD ["gunicorn","--bind"," 0.0.0.0:9000","drfsite.wsgi:application"] 