from django import forms
from . import models

class SaveText(forms.ModelForm):
	class Meta:
		model = models.Convert
		fields = ['words',]