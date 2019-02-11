from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request ,*args, **kwargs):
    print(args)
    print(kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html", {})

def contact_view(request,*args,**kwargs):
    #return HttpResponse('<h1>Contact Page</h1>')
    return render(request, "contact.html", {})

def About_view(request,*args,**kwargs):
    my_context = {
        "title": "This is about us",
        "my_numer": 123,
        "my_list":[123,12334,343,"ABC"],
        "my_html":"<h1>Hello wolrd</h1>"
    }
    #return HttpResponse('<h1>About Page</h1>')
    return render(request, "about.html", my_context)

def Social_view(request,*args,**kwargs):
    return HttpResponse('<h1>Social Page</h1>')

