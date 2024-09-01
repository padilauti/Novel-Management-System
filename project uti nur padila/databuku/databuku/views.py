from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from novel.views import NovelPerKategori


class DataBukuHomeView(LoginRequiredMixin, TemplateView, NovelPerKategori):
    template_name = "index.html"
    login_url = '/login/'

    def get_context_data(self):
        querysets = self.get_latest_novel_each_kategori()
        context = {
            'latest_novel_list':querysets
        }

        return context
       



    