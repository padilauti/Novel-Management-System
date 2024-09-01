from django.urls import path, re_path


from .views import (
    NovelListView,
    NovelDetailView,
    NovelKategoriListView,
    NovelCreateView,
    NovelManageView,
    NovelDeleteView,
    NovelUpdateView,
    )

urlpatterns =[
    re_path(r'^manage/update/(?P<pk>\d+)$', NovelUpdateView.as_view(), name='update'),
    re_path(r'^manage/delete/(?P<pk>\d+)$', NovelDeleteView.as_view(), name='delete'),
    path('manage/', NovelManageView.as_view(), name='manage'),
    path('tambah/', NovelCreateView.as_view(), name='create'),
    re_path(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$', NovelKategoriListView.as_view(), name='category'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', NovelDetailView.as_view(), name='detail'),
    re_path(r'^(?P<page>\d+)$', NovelListView.as_view(), name='list'),
]