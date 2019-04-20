from django.shortcuts import render, HttpResponseRedirect
import string, random
from .models import Links
from django.shortcuts import redirect

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def index(request):
    links = Links.objects.all()
    return render(request, 'index.html', {'all_links':links})

def generate(request):
    ori_link = request.POST.get('ori_link')
    
    if ori_link is not None:
        new_link = random_string()
        link = Links(new_url=new_link, original_url=ori_link)
        link.save()

        result_link = 'http://127.0.0.1:8000/'+new_link
    return render(request, 'result.html', {'newlink':result_link})

def redirect_to(request, shlink):
    query_set = Links.objects.filter(new_url=shlink).values('original_url').get()
    link = query_set['original_url']
    return redirect(link)