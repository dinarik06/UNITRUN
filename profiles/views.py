from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CustomLoginForm, RegistrationForm
from .models import User, Profile
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() # Сохраняем пользователя
            User.objects.create(user=user)  # Создаем профиль для пользователя
            login(request, user)  # Автоматически выполняем вход
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # Если запрос GET, создаем форму на основе профиля пользователя
        form = ProfileForm(instance=request.user.profile)
    
    # Получаем профиль пользователя
    profile = request.user.profile
    
    # Передаем данные в контекст, включая количество монет
    context = {
        'form': form,
        'coins': profile.coins,
        'username': request.user.username,  # Добавляем монеты в контекст
    }
    
    # Рендерим шаблон с контекстом
    return render(request, 'profile.html', context)

@login_required
def liveapril_case(request):
    return render(request, "cases/LiveAprilCase.html")

@login_required
def cat_case(request):
    return render(request, "cases/CatCase.html")

@login_required
def unit_case(request):
    return render(request, "cases/UnitCase.html")

@login_required
def legendary_case(request):
    return render(request, "cases/LegendaryCase.html")

@login_required
def ps2_case(request):
    return render(request, "cases/PS2Case.html")

#######

@login_required
def liveapril_case_open(request):
    return render(request, "cases/LiveAprilCase.html")

@login_required
def cat_case_open(request):
    return render(request, "cases/CatCase.html")

@login_required
def unit_case_open(request):
    return render(request, "cases/UnitCase.html")

@login_required
def legendary_case_open(request):
    return render(request, "cases/LegendaryCase.html")

@login_required
def ps2_case_open(request):
    return render(request, "cases/PS2Case.html")



@csrf_exempt
@login_required
def update_balance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            balance = data.get('balance', 0)

            # Обновляем баланс пользователя
            profile = request.user.profile
            profile.coins += balance  # coins — поле с монетами в модели Profile
            profile.save()

            return JsonResponse({'status': 'success', 'new_balance': profile.coins})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@login_required
@login_required
def spend_balance(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = data.get('amount', 0)

        profile = request.user.profile

        # Проверяем, достаточно ли монет
        if profile.coins < int(amount):
            return JsonResponse({'success': False, 'error': 'Недостаточно монет на балансе.'})

        # Списываем монеты
        profile.coins -= int(amount)
        profile.save()

        return JsonResponse({'success': True, 'new_balance': profile.coins})

    return JsonResponse({'success': False, 'error': 'Неверный метод запроса.'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправляем на страницу профиля
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

def tapalka(request):
    return render(request, "tapalka.html")