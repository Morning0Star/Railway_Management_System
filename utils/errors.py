class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

class BadRequestError(AppError):
    def __init__(self, message='Bad Request'):
        super().__init__(message, 400)

class AuthenticationError(AppError):
    def __init__(self, message='Authentication Failed'):
        super().__init__(message, 401)

class NotFoundError(AppError):
    def __init__(self, message='Resource Not Found'):
        super().__init__(message, 404)

class ConflictError(AppError):
    def __init__(self, message='Conflict'):
        super().__init__(message, 409)

class InternalServerError(AppError):
    def __init__(self, message='Internal Server Error'):
        super().__init__(message, 500) 