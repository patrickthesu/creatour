from django import forms
from .models import TouristProductEthap, TouristProduct, Review

class EthapForm (forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
    class Meta:
        model = TouristProductEthap
        fields = ["title", "description", "image"]

class ReviewForm (forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
    class Meta:
        model = Review
        fields = ["rate" ,"comment", "touristProduct", "user"]

class TouristProductForm (forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
    class Meta:
        model = TouristProduct
        fields = ["title", "description", "price", "headerImage", "timeWillTake", "ethaps" ]
