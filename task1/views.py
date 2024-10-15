from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.
def task3_1(request):
    return render(request, 'platform.html')


def task3_2(request):
    Buyers = Buyer.objects.all()
    context = {
        'Buyers': Buyers,
    }
    return render(request, 'services.html', context)


def task3_3(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'games.html', context)


def task3_4(request):
    return render(request, 'cart.html')


def menu(request):
    return render(request, 'menu.html')


users = ['Sergey', 'Petr', 'Lida']
info = {}


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data["age"]

            print(f"'Name' {username}")
            print(f"'password' {password}")
            print(f"'repeat_password' {repeat_password}")
            print(f"'age' {age}")

            if password == repeat_password and age >= 18 and username not in users:
                users.append(username)
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse(f"Ошибка, {info['error']}!")
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse(f"Ошибка, {info['error']}!")
            if username in users:
                info['error'] = f'Пользователь {username} уже существует'
                return HttpResponse(f"Ошибка, {info['error']}!")

    else:
        form = UserRegister()
    return render(request, 'registration_2.html', {'form': form})


def sign_up_by_html(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        subscribe = request.POST.get('subscribe') == 'on'

        print(f"'Name' {name}")
        print(f"'password' {password}")
        print(f"'repeat_password' {repeat_password}")
        print(f"'age' {age}")
        print(f"'subscribe' {subscribe}")
        if password == repeat_password and age >= 18 and name not in users:
            users.append(name)
            return HttpResponse(f"Приветствуем, {name}!")
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if name in users:
            info['error'] = f'Пользователь {name} уже существует'
            return HttpResponse(f"Ошибка, {info['error']}!")
    return render(request, 'registration_page.html', context=info)


def paginations(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'paginator.html', {'page_obj': page_obj})

