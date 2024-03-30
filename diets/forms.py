from django import forms
from .models import Cliente, Analitica


class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 
            'apellidos', 
            'f_inicio', 
            'f_nacimiento', 
            'direccion', 
            'telefono', 
            'fumador', 
            'activo', 
            'transito_intestinal_normal',
            'hidratacion',
            'alergias',
            'tratamientos',
            'habitos',
            'observaciones',
            'altura' 
        ]

class AnaliticaForm(forms.ModelForm):
    class Meta:
        model = Analitica
        fields = [
            'fecha', 
            'cliente', 
            'azucar', 
            'tiroides', 
            'acido_urico', 
            'anemia'
        ]