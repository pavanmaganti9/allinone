from django import forms

class NameForm(forms.Form):
    #name = forms.CharField()
	name = forms.CharField(label='Name', max_length=100)
	email = forms.EmailField(label='Email ', max_length=100)
	message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
	
