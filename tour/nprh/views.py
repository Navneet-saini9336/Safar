from django.shortcuts import render
from .models import demotable
from  .forms import demoforms

# Create your views here.
def index(request):
	return render(request,"nprh/index.html")
def explore(request):
	return render(request,"nprh/explore.html")
def travelreg(request):
	return render(request,"nprh/travelreg.html")
def login(request):
	return render(request,"nprh/login.html")
def explore2(request):
	return render(request,"nprh/explore2.html")
def p1(request):
	return render(request,"nprh/p1.html")
def p2(request):
	return render(request,"nprh/p2.html")
def privacy(request):
	return render(request,"nprh/privacy.html")
def medical(request):
	return render(request,"nprh/medical.html")
def local_transport(request):
	return render(request,"nprh/local_transport.html")
def term_and_condition(request):
	return render(request,"nprh/term_and_condition.html")
def work(request):
	return render(request,"nprh/work.html")
def our_process(request):
	return render(request,"nprh/our_process.html")
def insight(request):
	return render(request,"nprh/insight.html")
def contact(request):
	return render(request,"nprh/contact.html")
def bookform(request):
	return render(request,"nprh/bookform.html")
def registr(request):
	return render(request,"nprh/registr.html")
def create_views(request):
	context = {}
	form = demoforms(request.POST or None)
	if form.is_valid():
		form.save()
	context['form'] = form
	return render(request,"nprh/demo.html", context)