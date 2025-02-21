from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()