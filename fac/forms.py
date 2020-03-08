from django import forms

from .models import  Cliente

class ClienteForm(forms.ModelForm):
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = Cliente
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['nombres', 'apellidos', 'tipo', \
                'celular', 'estado']
        # Se excluyen los campos que no queremos mostrar en el formulario
        exclude = ['um', 'fm', 'uc', 'fc']

    # Para que los elementos tenga la clase de boostrap
    def __init__(self, *args, **kwargs):
        # para que los elementos se inicialicen
        super().__init__(*args, **kwargs)
        # Recorremos todos los campos que va a mostar
        for field in iter(self.fields):
            # al campo que esta recorriendo le asigna un widget y se actualiza la clase
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
