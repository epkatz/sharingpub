from django.http import HttpResponseRedirect
from django.shortcuts import render
from thepub.forms import ShareableForm
from thepub.models import Shareable, UserProfile


def index(request):
    form = ShareableForm()
    context = {'username': request.user.username,
               'form': form}
    return render(request, 'index.html', context)


def share(request):
    if request.method == 'POST':
        form = ShareableForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_profile = UserProfile(id=request.user.id)
            u = Shareable(url=cd['url'], shared_by=user_profile)
            u.save()
            return HttpResponseRedirect('/')
