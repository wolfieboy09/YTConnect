from .user import user
from .session import Session

# <--- Handling Exceptions --->
class ConnectionAbortedError(Expectation):
    pass

class ConnectionError(Expectation):
    pass

class ConnectionRefusedError(Expectation):
    pass

class ResponceCodeNot200(Expectation):
    pass

class APIKeyNotGiven(Expectation):
    pass
