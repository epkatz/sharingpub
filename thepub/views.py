from django.http import HttpResponseRedirect
from django.shortcuts import render
from thepub.forms import ShareableForm
from thepub.shareable_service import save_shareable, get_shareables_for_user


def index(request):
    form = ShareableForm()
    user = request.user
    shareables = get_shareables_for_user(user)
    context = {'username': user.username,
               'form': form,
               'shareables': shareables}
    return render(request, 'index.html', context)


def share(request):
    if request.method == 'POST':
        form = ShareableForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            save_shareable(request.user, cd['url'])
            return HttpResponseRedirect('/')
