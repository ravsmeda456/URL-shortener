from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import urlForm
from .models import url
from django.contrib import messages
import random, string
import validators
# Create your views here.

it = 0

def shortUrl(request):
    if request.method == 'POST':
        form = urlForm(request.POST)
        actual_url = request.POST['actual_url']
        if validators.url(actual_url):
            if len(url.objects.all().filter(actual_url=actual_url)) == 0:
                global it
                k = int(random.choice(string.digits))
                it += 1; temp = 'short-url'+ str(it)
                short_url = temp + ''.join(random.choices(string.ascii_letters + string.digits, k=k))
                url_obj = url(short_url=short_url, actual_url=actual_url)
                url_obj.save()
                messages.success(request,'successfully created the new short URL. Click on View URLs to view them')
                #print(k, temp ,short_url, actual_url)
            else:
                messages.info(request, "Url already exists please click on 'View URLs button' for shortened urls ")
        else:
            messages.error(request, "Please enter a valid URL")
    else:
        form = urlForm()
    return render(request, 'create.html', {'form': form})


def view_urls(request):
    all_urls = url.objects.all()
    return render(request, 'view.html', {'urls': all_urls})

def redirect_urla(request, id):
    url_obj = url.objects.all().filter(short_url=id)
    print(url_obj)
    if len(url_obj)==0:
        messages.error(request, "The Given URL us not created yet.. please check the URL.")
        return HttpResponseRedirect(reverse_lazy('urlapp:shortUrl'))
    return redirect(url_obj[0].actual_url)