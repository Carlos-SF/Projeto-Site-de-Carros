from django import forms
from cars.models import Brand,Car

#----------------------------------
# METODO ANTIGO USANDO forms.Form
#----------------------------------

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageFgitclsield()


# def save(self):
#     car  = Car(
#         model = self.cleaned_data['model'],
#         brand = self.cleaned_data['brand'],
#         factory_year = self.cleaned_data['factory_year'],
#         model_year = self.cleaned_data['model_year'],
#         plate = self.cleaned_data['plate'],
#         value = self.cleaned_data['value'],
#         photo = self.cleaned_data['photo'],
#     )
#     car.save()
#     return car 

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    #validação para cadastrar carros com valor minimode R$ 20.000
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value','Valor minimo deve ser de RS 20.000')
        return value
    
    #validação para ano de fabricaçao minimo de 1970
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1970:
            self.add_error('factory_year','Não é possivel cadastrar carros fabricados antes de 1970')
        return factory_year

        
    