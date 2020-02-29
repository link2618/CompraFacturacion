from django import forms

from .models import Proveedor, ComprasEnc

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = Proveedor
        # Se excluyen los campos que no queremos mostrar en el formulario
        exclude = ['um', 'fm', 'uc', 'fc']
        # Elementos html que van a usar
        widget = {'descripcion': forms.TextInput}

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


class ComprasEncForm(forms.ModelForm):
    #Renderizamos la fecha de compra
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    # Le decimos que va a mostrar el formulario
    class Meta:
        model = ComprasEnc
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['proveedor', 'fecha_compra', 'observacion', \
                'no_factura', 'fecha_factura', 'sub_total', \
                'descuento', 'total']

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
        # Campos de solo lectura
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
