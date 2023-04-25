from django import forms

from .models import Person, Contact

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'p_no' : forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'persontage' : forms.TextInput(attrs={'placeholder': '12TH %'}),
            'maths_marks': forms.TextInput(attrs={'placeholder': 'MATHS MARKS'})

        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control mb-30'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'email', 'class': 'form-control mb-30'}),
            'message' : forms.TextInput(attrs={'placeholder': 'message', 'class': 'form-control mb-30'})
        }