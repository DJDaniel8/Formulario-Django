from django import forms
from .models import Alumno

class DateInput(forms.DateInput):
    input_type = 'date'
    # Agrega el atributo "pattern" para especificar el formato de fecha dd/mm/yyyy
    input_formats = ['%d/%m/%Y']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombre', 'apellidos', 'correoElectronico', 'fechaNacimiento']
        widgets = {
            'fechaNacimiento': DateInput(),
        }
