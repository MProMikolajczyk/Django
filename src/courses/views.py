from django.shortcuts import render
from django.views import View

# BASE VIEW CLASS = VIEW
class CourseView(View):
    template_name = 'about.html'
    def get(self,request, id=None, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})
    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request,'about.html',{})