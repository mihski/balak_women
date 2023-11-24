from django.urls import path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name="home"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('about/', about, name='about'),
 #   path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),

]

