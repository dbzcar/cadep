from django import forms

from app.municipio.models import Municipio

class MunicipioForm(forms.ModelForm):

	class Meta:
		model = Municipio

		fields = [
		'codigo',
		'nombre',
		#'departamento',
			]

		labels= {
		'codigo': 'Codigo',
		'nombre': 'Nombre',
		#'departamento': 'Departamento',
		
		}

		widgets= {
        'codigo': forms.TextInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        #'departamento': forms.Select(attrs={'class':'form-control'}),
		}
