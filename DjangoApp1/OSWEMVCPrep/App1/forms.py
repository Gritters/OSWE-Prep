from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a clean title")
        
class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={}))
    price       = forms.DecimalField()