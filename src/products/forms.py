from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'your title '}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'your title ',
            'class':'new-class-name two',
            'id':'my-id-for-textarea',
            'row':120,
            'cols':120
        }
    ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError('This is not valid titile')

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not valid email')
        return email

class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'your title '}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'your title ',
            'class':'new-class-name two',
            'id':'my-id-for-textarea',
            'row':120,
            'cols':120
        }
    ))
    price = forms.DecimalField(initial=199.99)