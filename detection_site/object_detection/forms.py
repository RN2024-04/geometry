from django import forms

class TriangleForm(forms.Form):
    cathetus_a = forms.FloatField(required=False, label='Катет A')
    cathetus_b = forms.FloatField(required=False, label='Катет B')
    hypotenuse = forms.FloatField(required=False, label='Гипотенуза')
