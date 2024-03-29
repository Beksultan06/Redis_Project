import redis
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from apps.settings.models import PageView, Post
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from django.views.generic import TemplateView

from apps.telegram.models import Telegram
from apps.telegram.views import get_text, admin_id, bot


class IndexView(TemplateView):
    template_name = 'base/index.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content']

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Ошибка сервера")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'auth/register.html', {'form': form})

class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            if message:
                Telegram.objects.create(name=name, email=email, message=message)
            bot.send_message(admin_id, f"Оставлен отзыв\nИмя пользователя: {name}\nНомер телефона: {email}\nСообщение: {message}")

            return redirect('index')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})