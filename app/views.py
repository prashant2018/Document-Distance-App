from django.shortcuts import render
from app.forms import DocForm
from app.models import Documents
from app import logicFile 

def index(request):
	if request.method == 'GET':
		form = DocForm()
		return render(request,'app/index.html',{'form':form})
	else:
		form = DocForm(request.POST)
		#data = form.cleaned_data
		#f1 = form.cleaned_data['doc1']
		#f2 = form.cleaned_data['doc2']
		f1 = form['doc1'].value()		
		f2 = form['doc2'].value()
		result = logicFile.main_prog(f1,f2)
		return render(request,'app/result.html',{'result':result})
			
		

	
