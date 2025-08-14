## About project
1. Here we are developing a project using fastapi and mysql with docker

## Create project Directory
```
atul@atul-Lenovo-G570:~$ mkdir websys
```

## go to in this directory
```
atul@atul-Lenovo-G570:~$ cd websys
```


## How to use Docker in this project
1. create the docker file in project root directory 
```
atul@atul-Lenovo-G570:~/websys$ touch Dockerfile
```

2. Manually write below code in dockerfile
```
# Use the official Python image
FROM python:3.12.8

# Set the working directory. It means project root directory
WORKDIR /websys

# This command put requirements.txt in container in specific directory. Requirements library will be install in docker container
COPY ./requirements.txt /websys/requirements.txt


# This command will install dependancies in docker container
RUN pip install --no-cache-dir --upgrade -r /websys/requirements.txt

# copy source code files and directory in docker container
COPY ./app /websys/app

# this is default command. It will run after container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

```