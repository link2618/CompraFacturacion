from django.db import models

# Importamos la clase modelo madre que creamos en Bases
from bases.models import ClaseModelo

# Create your models here.
# Al herredar de ClaseModelo Ya tiene todos sus atributos
class Categoria(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la Categoria', unique=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    #Para guardar la descripcion en mayuscula
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    # Para que no le agrege la letra s
    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la Sub Categoria')

    def __str__(self):
        return "{}: {}".format(self.categoria.descripcion, self.descripcion)

    #Para guardar la descripcion en mayuscula
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    # Para que no le agrege la letra s y que no se repita la descripcion
    class Meta:
        verbose_name_plural = "Sub Categorias"
        # Para que no se repita la descripcion
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la Marca', unique=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    #Para guardar la descripcion en mayuscula
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    # Para que no le agrege la letra s y que no se repita la descripcion
    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la Unidad de Medida', unique=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    #Para guardar la descripcion en mayuscula
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    # Para que no le agrege la letra s y que no se repita la descripcion
    class Meta:
        verbose_name_plural = "Unidad de Medida"


class Producto(ClaseModelo):
    codigo = models.CharField('Codigo', max_length=20, unique=True)
    codigo_barra = models.CharField('Codigo de Barras', max_length=50)
    descripcion = models.CharField('Descripcion', max_length=200)
    precio = models.FloatField('Precio', default=0)
    existencia = models.IntegerField('Existencia', default=0)
    ultima_compra = models.DateField('Ultima Compra', null=True, blank=True)

    # Llaves foraneas
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    # Para que no le agrege la letra s y que no se repita la descripcion
    class Meta:
        verbose_name_plural = "Productos"
        # Para que no se repita la descripcion
        unique_together = ('codigo', 'codigo_barra')
