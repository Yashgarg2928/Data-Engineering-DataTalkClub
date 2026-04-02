# Data-Engineering-DataTalkClub

## 1. Docker Setup (Linux)
**What is Docker and why do we use it ?**
Docker a is a open-source platform which a devloper can use to make a isolated container inside your mashine which has its own configuration. Docker has many images including ubuntu, python which we can use to setup that contaion with any version we want and build and run our application inside that so that our application would not depend on our system configurations and will work every where.

It is state less by default means ones a container is closed it does not retain any memory.

1. install Docker from official website

2. Check if installed 
   `docker --version`

3. Run a simple container 
   `docker run hello-world`

4. You can see all docker images which are there on your device by this command 
   `docker images`

5. run ubuntu image using -it module 
   `docker run -it ubuntu`
   this starts a ubuntu container inside our system that runs ubunutu 

6. In the same way we can start use a python image and also specify the entrypoint if we don't specify the entry point it will durectlly enter into python 
   `docker run -it --entrypoint=bash python:3.13.11-slim` (this is a smaller version of python)
   using --entrypoint argumnet we are defining to start from bash not the default choice python

7. As we know docker container is state-less but we need to store data somewhere so we use volume -v to do that 
    we can use any folder to map it to docker image like this (in this example we have a test folder inside working directory)
   `docker run -it --rm $(pwd)/test:/app/test --entrypoint=bash python:3.13.11`
   in this example using pwd we are taking the path of working directory then maping test folder to /app/test folder inside docker container you can view these folder using 
   `ls` inside docker container



## Data Pipeline
A Data Pileline is a service that take data as input and outputs data. Example a simple Data Pipline can be a service which downloads csv data from web and stores it inside postgreSQL. 

[Workshop-1](/workshop-1/)

   
