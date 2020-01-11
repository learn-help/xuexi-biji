from django import forms as django_forms
from django.contrib.auth import password_validation
from django.contrib.auth import forms
from django.utils.translation import gettext, gettext_lazy as _

from .models import UserInfo

class UserRegisterForm(forms.UserCreationForm):
    password1 = django_forms.CharField(
        label=_("Password"),
        strip=False,
        widget=django_forms.PasswordInput(attrs={'autocomplete': 'new-password', 'onblur': 'SavePassword1(this.value)', 'onkeyup': 'SavePassword1(this.value)', 'onfocus': 'SavePassword1(this.value)'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = django_forms.CharField(
        label=_("Password confirmation"),
        widget=django_forms.PasswordInput(attrs={'autocomplete': 'new-password', 'onblur': 'SavePassword2(this.value)', 'onkeyup': 'SavePassword2(this.value)', 'onfocus': 'SavePassword2(this.value)'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True, 'onblur': 'SaveUsername(this.value)', 'onkeyup': 'SaveUsername(this.value)', 'onfocus': 'SaveUsername(this.value)'})

class EmailForm(django_forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['email']
        labels = {'email': '您的电子邮件地址'}

class VerifyForm(django_forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['check_code']
        labels = {'check_code': '您收到的验证码'}
