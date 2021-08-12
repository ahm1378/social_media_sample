from django.views.generic import FormView, UpdateView
from user.forms import RegisterForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import login, get_user_model
User = get_user_model()


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


def index(request):
    return render(request, 'user/home.html', context={'user': request.user.username})


class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'avatar', 'bio', 'website']
    template_name = 'user/profile.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user
