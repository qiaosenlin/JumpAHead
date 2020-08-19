from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
	
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
	date_of_birth = forms.DateField(help_text='Date of Birth')

	class Meta:
		model = get_user_model()
		fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2', )


class UpdateProfileForm(ModelForm):
	email = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
	class Meta:
		model = get_user_model()
		fields = ('email',)
	
	def __init__(self, *args, **kwargs):
		super(UpdateProfileForm, self).__init__(*args, **kwargs)
		