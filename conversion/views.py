from django.shortcuts import render, redirect
from .models import Convert
from . import forms
# Create your views here.
def convert_view(request):
	if request.method == 'POST' :
		form = forms.SaveText(request.POST)
		
		if form.is_valid():
			form.save()
			posts = Convert.objects.latest('date')
			#posts.words = ' '.join(format(ord(x), 'b') for x in posts.words)
			posts.words = ' '.join(map(bin,bytearray(posts.words,'utf8')))


			#posts = map(bin,bytearray(posts))
			args = {'posts':posts}
			return render(request,'conversion/converting.html', args)
	
	
	else:
		return render(request,'conversion/converting.html')
