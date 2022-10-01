#decorator to stop Logged in user to loginpage

from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_view')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func