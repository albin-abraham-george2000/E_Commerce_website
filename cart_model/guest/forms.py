from django import forms as f
from admin_panel.models import UserInfo


class LoginForm(f.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("email", "password")
        # modify existing validation message
        error_messages = {"password": {"required": "Blank is not allowed !"}}

    def clean(self):
        data = self.cleaned_data
        email = str(data.get("email")).strip()
        pwd = str(data.get("password")).strip()
        # new validations
        if (len(email) == 0):
            self.add_error("email", "Blank is not allowed !")
        if (len(pwd) < 4):
            self.add_error("password", "Minimum 4 characters needs !")
