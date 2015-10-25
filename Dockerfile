FROM python:2-onbuild

#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app

#COPY . /usr/src/app
EXPOSE 8080
#RUN pip install -r requirements.txt
CMD python start.py

