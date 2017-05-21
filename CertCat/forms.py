from django import forms
from django.forms import ModelForm
from .models import *

from CertificateCatalog import settings


class ReadCertForm(forms.Form):
    file = forms.FileField(label='Please upload certificate:')

    def clean_file(self):
        file = self.cleaned_data['file']

        if file:
            file_type = file.content_type.split('/')[1]
            if file_type not in settings.TASK_UPLOAD_FILE_TYPES or len(file.name.split('.')) == 1:
                raise forms.ValidationError('File type is not supported')

        return file


class CertSubjORMForm(ModelForm):
    class Meta:
        model = cert_subj
        fields = '__all__'
        widgets = {'notafter': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
                   'notbefore': forms.DateTimeInput(attrs={'class': 'datetimepicker'})}

    def save(self):
        obj = super(CertSubjORMForm, self).save()
        return obj


class CertSubjRawForm(forms.Form):
    OU = forms.CharField(required=False)
    C = forms.CharField(required=False)
    CN = forms.CharField(required=False)
    O = forms.CharField(required=False)
    L = forms.CharField(required=False)
    ST = forms.CharField(required=False)
    CN = forms.CharField(required=False)
    street = forms.CharField(required=False)
    title = forms.CharField(required=False)
    emailAddress = forms.CharField(required=False)
    serial = forms.CharField(required=False)
    notafter = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}))
    notbefore = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'class': 'datetimepicker'}))

