# set base image (host OS)
FROM python:3.8

LABEL djotiham (SOA 2020)

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY resources/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY resources .

RUN chmod -R 777 .

# # command to run on container start
CMD [ "/bin/bash"]
# # ENTRYPOINT [ "python", "./run.py" ]