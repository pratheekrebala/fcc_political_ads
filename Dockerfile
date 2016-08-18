FROM python:2.7

#Make sure app directory exists
RUN mkdir -p /usr/src/app

#Copy over the requirements first. This allows us to cache the installation of modules
COPY /requirements.txt /usr/src/app/requirements.txt

#Set work context
WORKDIR /usr/src/app

#Install required packages.
RUN sudo pip install mercurial
RUN sudo pip install -r requirements.txt

#Copy files over
COPY / /usr/src/app

ENTRYPOINT ["/bin/bash"]