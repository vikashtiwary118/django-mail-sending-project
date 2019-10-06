from django import forms

class ContactForm(forms.Form):
	mails = forms.CharField(max_length=100)
	subjects = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	cc = forms.CharField(max_length=1000)
	bcc = forms.CharField(max_length=1000)
    
