from time import sleep

from celery.task import task
from django.contrib.auth import get_user_model
User = get_user_model()

@task(name="send verify code")
def send_verify(username):
    # try:
    #     user=User.object.get(username=username)
    # except User.DoesNotExists:
    #     return None
    sleep(10)
    print(" user name in celery ",username)

