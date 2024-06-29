from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from apps.telegram.forms import TelegramForm
from apps.telegram.views import admin_id, bot
from apps.settings.models import Settings
from django.core.cache import cache
import pickle

class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Settings.objects.latest('id')
        return context

class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def post(self, request):
        form = TelegramForm(request.POST)

        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            bot.send_message(admin_id, f"Оставлен отзыв\nИмя пользователя: {name}\nНомер телефона: {email}\nСообщение: {message}")

            try:
                # Попытка сохранить форму в кэше Redis
                cache.set(f"contact_form_{request.user.id}", form, timeout=3600)  # Сохраняем на 1 час
            except pickle.PicklingError as e:
                # Обработка ошибки PicklingError
                print(f"Ошибка сериализации данных: {e}")

            return redirect('index')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        # Проверяем, есть ли кэшированная форма для текущего пользователя
        cached_form = cache.get(f"contact_form_{request.user.id}")
        if cached_form:
            form = cached_form
        else:
            form = TelegramForm()
        return render(request, self.template_name, {'form': form})