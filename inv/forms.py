from django import forms

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

class CategoriaForm(forms.ModelForm):
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = Categoria
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['descripcion', 'estado']
        # Etiquetas para los campos
        labels = {'descripcion': "Descripcion de la Categoría", "estado":"Estado"}
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


class SubCategoriaForm(forms.ModelForm):
    # Modificar la consulta que hace django a la base de datos para enlistar categorias
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = SubCategoria
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['categoria', 'descripcion', 'estado']
        # Etiquetas para los campos
        labels = {'descripcion': "Sub Categoría", "estado":"Estado"}
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
        # Asignamos un valor por defecto para el select de categoria
        self.fields['categoria'].empty_label = "Seleccione Categoría"


class MarcaForm(forms.ModelForm):
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = Marca
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['descripcion', 'estado']
        # Etiquetas para los campos
        labels = {'descripcion': "Descripcion de la Marca", "estado":"Estado"}
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


class UMForm(forms.ModelForm):
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = UnidadMedida
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['descripcion', 'estado']
        # Etiquetas para los campos
        labels = {'descripcion': "Descripcion de la Unidad de Medida", "estado":"Estado"}
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


class ProductoForm(forms.ModelForm):
    # Modificar la consulta que hace django a la base de datos para enlistar categorias
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.filter(estado=True).order_by('descripcion')
    )
    unidad_medida = forms.ModelChoiceField(
        queryset=UnidadMedida.objects.filter(estado=True).order_by('descripcion')
    )
    subcategoria = forms.ModelChoiceField(
        queryset=SubCategoria.objects.filter(estado=True).order_by('descripcion')
    )
    # Le decimos que va a mostrar el formulario
    class Meta:
        model = Producto
        # Elementos que va a mostar el formulario, lo que puede cambiar el usuario
        fields = ['codigo', 'codigo_barra', 'descripcion', 'estado', \
                'precio', 'existencia', 'ultima_compra', \
                'marca', 'unidad_medida', 'subcategoria']
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
        # Estos campos no seran editables para el usuario
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True
