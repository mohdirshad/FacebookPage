from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = "login.html"


class UpdatePage(View):
    def post(self, request):
    	data = request.data
        return render(request, 'updatepage.html',data)
