from django import forms

class DateInput(forms.DateInput):
	input_type = 'date'

class addForm(forms.Form):
	sub_name = forms.CharField(label='sub_name', max_length=100)
	sub_price = forms.DecimalField(decimal_places=2, label="sub_price")
	sub_date = forms.DateField(widget=forms.SelectDateWidget, label='sub_date')
	sub_exp = forms.DateField(widget=forms.SelectDateWidget, label='sub_exp')

class editForm(forms.Form):
	sub_name = forms.CharField(label='sub_name', max_length=100)
	sub_price = forms.DecimalField(decimal_places=2, label="sub_price")
	sub_date = forms.DateField(widget=forms.SelectDateWidget, label='sub_date')
	sub_exp = forms.DateField(widget=forms.SelectDateWidget, label='sub_exp')