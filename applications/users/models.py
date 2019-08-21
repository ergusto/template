from django.contrib.auth.models import AbstractUser
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your models here.
class User(AbstractUser):
    pass

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token
