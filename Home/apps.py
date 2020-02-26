from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'Home'

    def ready(self):
        from Home.views import TestClass
        TestClass.test_func(repeat=10, repeat_until=None)
