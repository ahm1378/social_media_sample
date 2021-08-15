from django.views.generic import FormView, UpdateView, DetailView
from user.utils import find_user_byid_followers, find_user_byid_followering
from relation.models import Relation
from user.forms import RegisterForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import login, get_user_model
User = get_user_model()


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = 'login'

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


class UserDetail(DetailView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'user/seeprofile.html'

    def get_context_data(self, **kwargs):

        content = super().get_context_data(**kwargs)
        user = self.get_object()
        content['post_count'] = user.posts.count()
        content['followers_count'] = user.followers.count()
        content['followings'] = user.followings.values()
        content['followers'] = user.followers.values()
        content['followers_count'] = user.followers.count()
        content['user_name_followers'] = find_user_byid_followers(content, User)
        content['user_name_followings'] = find_user_byid_followering(content, User)
        content['FollowFlag'] = Relation.objects.filter(from_user=self.request.user, to_user=user).exists()
        return content
