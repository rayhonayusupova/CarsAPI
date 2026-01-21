from rest_framework.exceptions import APIException

class CustomValidationError(APIException):
    status_code=400
    default_code='bad_request'
    default_detail='error exists'

    def __init__(self, detail=None, code=None):
        if detail:
            self.details={
                'message':detail,
                'code':code
            }
        else:
            self.details={
                'message':self.default_detail,
                'code':self.default_code            
            }