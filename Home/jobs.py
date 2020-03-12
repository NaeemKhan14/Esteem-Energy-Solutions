from apscheduler.schedulers.background import BackgroundScheduler
from .views import TestClass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(TestClass.test_func, 'interval', minutes=1)
    scheduler.start()
