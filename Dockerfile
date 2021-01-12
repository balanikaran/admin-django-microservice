# choosing the base image
FROM python:3.9

# helps in getting python logs
ENV PYTHONUNBUFFERED 1

# setting up work directory
WORKDIR /app

# copy requirements file
COPY requirements.txt /app/requirements.txt

# installing requirements
RUN pip install -r requirements.txt

# copying all the files from local to container
COPY . /app

# running server inside/on the container along with the port inside the container
# shifted this command to compose file
# CMD python manage.py runserver 0.0.0.0:8000