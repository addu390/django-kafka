from .models import UserConsumer


def dict_to_user(obj, ctx):
    if obj is None:
        return None

    return UserConsumer(username=obj['username'], data=obj['data'])


def user_to_dict(user, ctx):
    return dict(username=user.username,
                data=user.data)
