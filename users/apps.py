from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # TODO: 学习这个
    def ready(self):
        import users.signals
