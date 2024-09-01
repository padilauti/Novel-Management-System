from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView,
    UpdateView,
    TemplateView,
    )

from django.urls import reverse_lazy
from .mixins import IsPenulisMixin, IsPembacaMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# load model
from .models import Novel
from .forms import NovelForm



def is_penulis(user):
    return user.groups.filter(name='penulis').exists()

class ForbiddenView(TemplateView):
    template_name = 'forbidden.html'






class NovelUpdateView(LoginRequiredMixin,UpdateView,IsPenulisMixin):
    form_class = NovelForm
    model = Novel
    template_name = "novel/novel_update.html"

    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NovelDeleteView(LoginRequiredMixin,DeleteView,IsPenulisMixin):
    model = Novel
    template_name = "novel/novel_delete_confirmation.html"
    success_url = reverse_lazy('novel:manage')

    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class NovelManageView(LoginRequiredMixin,ListView,IsPembacaMixin):
    model = Novel
    template_name = "novel/novel_manage.html"
    context_object_name = 'novel_list'

class NovelCreateView(LoginRequiredMixin,CreateView,IsPenulisMixin):
    form_class = NovelForm
    template_name = "novel/novel_create.html"

    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class NovelPerKategori():
    model = Novel

    def get_latest_novel_each_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []

        for kategori in kategori_list:
            novel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(novel)

        return queryset



class NovelKategoriListView(ListView):
    model = Novel
    template_name = "novel/novel_kategori_list.html"
    context_object_name = 'novel_list'
    ordering = ['-published']
    paginate_by = 3
    
    def get_queryset(self):
        self.queryset= self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()
    
    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)
       

        

class NovelListView(LoginRequiredMixin, ListView):
    model = Novel
    template_name = "novel/novel_list.html"
    login_url = '/login/'
    context_object_name = 'novel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)



    
class NovelDetailView(DetailView):
    model = Novel
    template_name = "novel/novel_detail.html"
    context_object_name = 'novel'

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})

        novel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({'novel_serupa':novel_serupa})


        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

