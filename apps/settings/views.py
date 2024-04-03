import redis
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from apps.telegram.models import Telegram
from apps.telegram.views import admin_id, bot
from apps.settings.models import Settings

class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Settings.objects.latest('id')
        return context


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