from django import forms

from app.municipio.models import Municipio

class MunicipioForm(forms.ModelForm):

	class Meta:
		model = Municipio

		fields = [
		'nombre',
		#'departamento',
			]

		labels= {

		'nombre': 'Nombre',
		#'departamento': 'Departamento',
		
		}

		widgets= {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
		#'departamento': forms.Select(attrs={'class':'form-control'}),
		}