class UserConsumer(object):

    def __init__(self, username=None, data=None):
        self.username = username
        self.data = data

    class Meta:
        managed = False


class UserProducer(object):

    def __init__(self, username, token, data):
        self.username = username
        self.data = data
        self._token = token

    class Meta:
        managed = False
