from django import forms
from app.models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('image',)