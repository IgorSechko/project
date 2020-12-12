from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .filters import UserExtFilter
from .algorithm import evaluate
from .forms import CardForm, RegisterForm, UserExtensionRegForm, UserExtensionEditForm, MessageForm
from .models import Card, UserExtension, Relation
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages as msgs


@login_required(login_url='login_or_register')
def profile(request):
    return render(request, "relfinder/profile_main.html")


@login_required(login_url='login_or_register')
def profilesettings(request):
    userEx = request.user.userExtension
    form = UserExtensionEditForm(instance=userEx)
    if request.method == 'POST':
        form = UserExtensionEditForm(
            request.POST, request.FILES, instance=userEx)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return HttpResponse("Форма заполнена неверно")
    return render(request, "relfinder/profile_settings.html", {'form': form})


@login_required(login_url='login_or_register')
def similarities(request):
    all_relations = Relation.objects.all()
    user_relations = all_relations.filter(referenced_by__user=request.user)

    return render(request, "relfinder/profile_similarities.html", {'user_relations': user_relations})


@login_required(login_url='login_or_register')
def mycards(request):
    return render(request, "relfinder/profile_mycards.html")


@login_required(login_url='login_or_register')
def logoutUser(request):
    logout(request)
    return redirect('login_or_register')


def login_or_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            reqType = request.POST.get('type')
            if reqType == 'login':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                else:
                    return HttpResponse("the user doesn't exist")

            elif reqType == 'register':
                userRegForm = RegisterForm(request.POST)
                userExRegForm = UserExtensionRegForm(request.POST)
                if userRegForm.is_valid() and userExRegForm.is_valid():
                    user = userRegForm.save()
                    userEx = userExRegForm.save(commit=False)
                    userEx.user = user
                    userEx.save()
                    msgs.success(request, "Регистрация прошла успешно! Выполните вход.")
                    return render(request, 'relfinder/login_or_register.html')
                else:
                    return HttpResponse("Form is invalid")
            elif reqType == 'ajax':
                username = request.POST['username']
                if User.objects.filter(username=username).count():
                    return HttpResponse("этот логин уже занят")
                else:
                    return HttpResponse("")
                

            else:
                return HttpResponse("an error occurred")

        else:
            return render(request, 'relfinder/login_or_register.html')


@login_required(login_url='login_or_register')
def create(request):
    return render(request, "relfinder/profile_createcard.html")


@login_required(login_url='login_or_register')
def save_form_data(request, *args, **kwargs):
    form = CardForm(request.POST or None)
    if form.is_valid():                 
        obj = form.save(commit=False)   
        obj.user = request.user
        obj.save()
        evaluate(obj)
    else:
        return HttpResponse("Форма заполнена некорректно")
    return redirect("profile")


@login_required(login_url='login_or_register')
def get_user(request, pk):
    if request.user.id == int(pk):
        return redirect('profile')
    try:
        user = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Пользователь не существует")

    return render(request, "relfinder/profile_viewuser.html", {'user': user})


@login_required(login_url='login_or_register')
def viewcard(request, pk):
    try:
        card = Card.objects.get(id=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Карточка не существует")
    showButtons = False
    if card.user == request.user:
        showButtons = True
    return render(request, "relfinder/profile_viewcard.html", {'card': card, 'showButtons': showButtons})


@login_required(login_url='login_or_register')
def update_card(request, pk):
    card = Card.objects.get(id=pk)
    if card.user == request.user:
        if request.method == 'POST':
            form = CardForm(request.POST, instance=card)
            if form.is_valid():
                Q_obj = Q(referenced_by=card) | Q(referencing=card)
                Relation.objects.filter(Q_obj).delete()
                newCard = form.save()
                evaluate(newCard)
                return redirect('viewcard', newCard.id)
            else:
                return HttpResponse("Форма заполнена некорректно")
        elif request.method == 'GET':
            return render(request, "relfinder/profile_updatecard.html", {'card':card})
        else:
            return HttpResponse("Неизвестный метод отправки формы")
    else:
        return HttpResponse("Вы не можете изменять карточки других пользователей")


@login_required(login_url='login_or_register')
def delete_card(request, pk):
    card = Card.objects.get(id=pk)
    if card.user == request.user:
        card.delete()
    else:
        return HttpResponse("Вы не можете удалять карточки других пользователей")
    return redirect('mycards')


@login_required(login_url='login_or_register')
def usersearch(request):
    userExtensions = UserExtension.objects.all().exclude(
        id=request.user.userExtension.id)

    userFilter = UserExtFilter(request.GET, userExtensions)
    userExtensions = userFilter.qs

    context = {
        'userExtensions': userExtensions,
        'userFilter': userFilter,
    }
    return render(request, "relfinder/profile_usersearch.html", context)


@login_required(login_url='login_or_register')
def messages(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        obj = form.save(commit=False)   # returns object instance
        obj.written_by = request.user
        obj.save()
        return redirect(request.POST['redirect'])
    elif request.method == "GET":
        wbmessages = request.user.wbMessages_set
        wt_users = wbmessages.values_list('written_to', flat=True).distinct()
        wtmessages = request.user.wtMessages_set
        wb_users = wtmessages.values_list('written_by', flat=True).distinct()
        ids = set(list(wt_users) + list(wb_users))
        users = User.objects.filter(id__in=ids)
        return render(request, "relfinder/profile_messages.html", {'users': users})


@login_required(login_url='login_or_register')
def dialogue(request, pk):
    messagesToPkUser = request.user.wbMessages_set.filter(written_to=pk)
    messagesByPkUser = request.user.wtMessages_set.filter(written_by=pk)
    messages = messagesToPkUser | messagesByPkUser
    messages = messages.order_by('datetime')
    return render(request, "relfinder/profile_dialogue.html", {'messages': messages, 'userPk': pk})
