FROM python:3.12-alpine 
COPY . /application
WORKDIR /application             
RUN pip install -r requirements.txt
CMD python application.py 