class BadRequestError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(BadRequestError, self).__init__(message)


class GatewayError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(GatewayError, self).__init__(message)


class ServerError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(ServerError, self).__init__(message)


class NotFoundError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(NotFoundError, self).__init__(message)
