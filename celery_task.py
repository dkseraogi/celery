from celery import Celery

app = Celery('tasks',broker='amqp://localhost//')


@app.task
def sum(a,b):
	return a+b
