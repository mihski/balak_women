from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView,CreateView

from .forms import AddPostForm
from .models import Women, Category
from .serializers import WomenSerializer

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context['title'] = "главная cтраница"
        context["cat_selected"] = 0
        cats = Category.objects.all()
        context["cats"] = cats
        return context


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        cats = Category.objects.all()
        context["cats"] = cats
        return context


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = "post_slug"
    context_object_name = "post"


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


# def index(request):
#     posts = Women.objects.all()
#     context = {
#         "posts": posts,
#         "menu": menu,
#         "title": "Главная страница"
#     }
#     return render(request, 'women/index.html', context=context)



# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# def delete(self, request):
#     del_str = Women.objects.filter(pk=6)
#     del_str.delete()
#     return Response({"post": del_str})
