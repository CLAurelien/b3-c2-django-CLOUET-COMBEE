from django import forms

from sites.models import Sites


class SiteForm(forms.ModelForm):
    class Meta:
        model = Sites
        wigets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'
