from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))
def home(request):
	#string=u"I use django to make website"
	#return render(request,'home.html',{'string':string})
	#TutorialList=["Html","CSS","JQuery","Python","Django"]
	#return render(request,'home.html',{'Tutorial':TutorialList})
	#info_dict={'site':u'zchweb','content':u'zchprctice'}
	#return render(request,'home.html',{'info_dict':info_dict})
	List=map(str,range(100))
	return render(request,'home.html',{'List':List})
