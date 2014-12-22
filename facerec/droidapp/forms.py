from django import forms
from droidapp.models import Page, Category

class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128, help_text="Please enter category")

	class Meta:
		model=Category
		fields=('name',)

class PageForm(forms.ModelForm):
	title=forms.CharField(max_length=128, help_text="Please enter Title")
	url=forms.URLField(max_length=200, help_text="Please enter URL")

	def clean(self):
		cleaned_data=self.cleaned_data
		url=cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url='http://'+url
			cleaned_data['url']=url
		return cleaned_data

	class Meta:
		model=Page
		fields=('title', 'url')
