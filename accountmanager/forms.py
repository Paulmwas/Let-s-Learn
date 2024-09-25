from django import forms
from .models import ProfileData

class StudentProfileData(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = ['profile_picture', 'user_name', 'study_level', 'email', 'bio']

        widgets = {
            'user_name' : forms.TextInput(attrs={'id':'username', 'class':'form-control'}),
            'study_level' :forms.NumberInput(attrs={'id':'study_level', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'id':'email', 'class':'form-control'}),
            'bio':forms.Textarea(attrs={'id':'bio', 'class':'form-control'})
        }