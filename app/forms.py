from django import forms
from .models import Documents
class DocForm(forms.ModelForm):
	class Meta:
		model = Documents
		fields = ('doc1','doc2')
