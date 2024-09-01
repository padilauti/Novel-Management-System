from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect





class IsPenulisMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='penulis').exists()
    
    def handle_no_permission(self):
        return redirect('forbidden')

class IsPembacaMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='pembaca').exists()
    
    def handle_no_permission(self):
        return redirect('forbidden')