from django import forms
from .models import TouristProductEthap

class EthapForm (forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
    class Meta:
        model = TouristProductEthap
        fields = ["title", "description", "image"]
