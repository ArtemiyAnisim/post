# Create your views here.

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, \
    Http404, JsonResponse


from django.shortcuts import render
from django.http import HttpResponseNotFound


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def posts(request):
    return HttpResponse("Весь набор постов")


def post(request, id):
    return HttpResponse(f"Номер поста {id}")


def comments(request, id):
    return HttpResponse(f"Количесво комментариев у поста {id} ")


def likes(request, id):
    return HttpResponse(f"Количесво лайков у поста {id}")


def popular(request):
    return HttpResponse("Популярные посты.")


def last(request):
    return HttpResponse("Последние опубликованные ")


def about(request):
    return HttpResponse("about")


def contacts(request):
    return HttpResponse("contacts")


def redirect(request):
    return HttpResponseRedirect("/about")


def permanent(request):
    return HttpResponsePermanentRedirect("/contacts")


def set(request):
    username = request.GET.get("username", "undefined")
    login = request.GET.get("login", "undefined")
    response = HttpResponse(f"Hello {username}. Login {login}")
    response.set_cookie("username", username)
    response.set_cookie("login", login)
    return response


def get(request):
    username = request.COOKIES.get("username", "undefined")
    login = request.COOKIES.get("login", "undefined")
    return HttpResponse(f"Hello {username}. Login {login}")


def error(request):
    return HttpResponseNotFound(f"Ошибка загрузки страницы")


def access(request):
    login = request.GET.get("login", "undefined")
    password = request.GET.get("password", "undefined")
    if login == "admin" and password == "admin":
        return HttpResponse("Все нормально")
    else:
        return HttpResponse("Отсутствует доступ")


class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name


class PersonEncoder(DjangoJSONEncoder):
    def defult(self, obj):
        if isinstance(obj,Person):
            return {"name": obj.name,"age":obj.age}
        return super().default(obj)


def set_cookie(request):
    username = request.GET.get('username', 'undefined')
    login = request.GET.get('login', 'undefined')

    response = HttpResponse("Cookies set successfully")
    response.set_cookie('username', username)
    response.set_cookie('login', login)

    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'undefined')
    login = request.COOKIES.get('login', 'undefined')

    return HttpResponse(f"Stored Cookies - Username: {username}, Login: {login}")