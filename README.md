----Example for Asynchronous processing using Celery----


Step 1 - Up and running with RabbitMQ!

Celery requires a backend infrastucture which can hold the tasks for asynchronous processing. Redis, RabbitMQ or something else can be used. This example uses RabbitMQ.

This example also uses docker to provide basic infrastructure for celery. Following commands will get RabbitMQ up and running in the system. But the pre-requisite is docker. The same example can be run without docker as well.

$ docker pull rabbitmq
$ docker run --name rabbit --network host rabbitmq

The above two commands will download the official version of rabbitmq image in the system and will start a container using the host network mapping for simplicity.


Step 2 - Installing celery

It is always good to have a virtual environment setup for any new infrastructure setup which will not interfare with the old one. Thogh not a pre-requisite for this example.

$ pip install celery

Fire the above command and we are done!



Step 3 - Run the celery from within the celery task module

For this example to run, go the directory which contains the task module and fire the below command

$ celery -A celery_task worker --loglevel=info

The above command should bring up the celery and log should look calm!



Step 4 - Run the app

Now the last step is to start the python command line interface from the app directory and invoke the program as following

>> from celery_task import *
>> sum.delay(1,2)


That's it! This should allow us to run our very simple program and the output could be seen from the celery log.
