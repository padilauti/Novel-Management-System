from django.forms import ModelForm

from .models import Novel


class NovelForm(ModelForm):
    class Meta:
        model = Novel
        fields = [
            'judul',
            'isi',
            'kategori',
        ]






