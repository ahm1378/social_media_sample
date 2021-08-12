from django import forms
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='password_repeat'
    )

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords are not match")
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("user already exits")
        return self.cleaned_data

    def save(self):
        return User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
            widget=forms.PasswordInput
        )

    def clean(self):
        print(self.cleaned_data['username'])
        if not User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("username is incorrect")
        user = authenticate(**self.cleaned_data)
        print(user)
        if user is None:
            raise forms.ValidationError("Password is incorrect")
        self.cleaned_data['user'] = user
        return self.cleaned_data
