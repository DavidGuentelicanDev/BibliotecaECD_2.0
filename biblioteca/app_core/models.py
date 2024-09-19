from django.db import models
from django.contrib.auth.models import AbstractUser


#MODELO BASE DE DATOS BIBLIOTECA

#pais
class Pais(models.Model):
    id_pais     = models.SmallAutoField(primary_key=True)
    nombre_pais = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return str(self.nombre_pais)


#editorial
class Editorial(models.Model):
    id_editorial          = models.SmallAutoField(primary_key=True)
    nombre_editorial      = models.CharField(unique=True, max_length=50)
    pais                  = models.ForeignKey(Pais, on_delete=models.CASCADE)
    informacion_editorial = models.TextField(blank=True, null=True)
    logo                  = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return str(self.nombre_editorial)


#libro
class Libro(models.Model):
    #categorias
    CATEGORIAS = [
        (1, 'Novela'),
        (2, 'Poesía'),
        (3, 'Cuentos'),
        (4, 'Dramaturgia'),
        (5, 'Cartas'),
        (6, 'Ensayo'),
        (7, 'Filosofía'),
        (8, 'Historia'),
        (9, 'Atlas y Enciclopedias')
    ]

    #estados de libro
    ESTADOS_LIBRO = [
        (1, 'Recepcionado - En proceso'), #libro recien registrado pero aun no disponible
        (2, 'Disponible'),
        (3, 'Reservado'),
        (4, 'Prestado'),
        (5, 'Devuelto - En proceso'), #libro devuelto pero aun no disponible
        (6, 'En reparación'),
        (7, 'Extraviado temporalmente'), #extraviado pero aun no de forma definitiva
        (8, 'Perdido')
    ]

    #atributos
    codigo       = models.PositiveSmallIntegerField(primary_key=True)
    titulo       = models.CharField(max_length=100)
    subtitulo    = models.CharField(max_length=100, blank=True, null=True)
    resena       = models.TextField(blank=True, null=True)
    categoria    = models.PositiveSmallIntegerField(choices=CATEGORIAS)
    editorial    = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    portada      = models.ImageField(upload_to='', blank=True, null=True)
    estado_libro = models.PositiveSmallIntegerField(choices=ESTADOS_LIBRO, default=1)

    def __str__(self):
        if (self.subtitulo):
            return f'{self.titulo}. {self.subtitulo}'
        else:
            return str(self.titulo)


#autor
class Autor(models.Model):
    id_autor          = models.SmallAutoField(primary_key=True)
    nombre_autor      = models.CharField(unique=True, max_length=50)
    pseudonimo        = models.CharField(unique=True, max_length=50, blank=True, null=True)
    pais              = models.ForeignKey(Pais, on_delete=models.CASCADE)
    informacion_autor = models.TextField(blank=True, null=True)
    imagen            = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        if (self.pseudonimo):
            return str(self.pseudonimo)
        else:
            return str(self.nombre_autor)


#autor por libro
class AutorPorLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('libro', 'autor')

    def __str__(self):
        return f'{self.libro} - {self.autor}'


#usuario
class Usuario(AbstractUser):
    #roles
    ROLES = [
        (1, 'Administrador'),
        (2, 'Bibliotecario'),
        (3, 'Asistente'),
        (4, 'Cliente')
    ]

    #atributos
    rut      = models.CharField(unique=True, max_length=10)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    username = models.EmailField(unique=True)
    rol      = models.PositiveSmallIntegerField(choices=ROLES, default=4)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#reserva
class Reserva(models.Model):
    #estados
    ESTADOS_RESERVA = [
        (1, 'Provisoria'), #estado cuando el cliente carga el primero libro al carrito
        (2, 'Confirmada'), #estado cuando el cliente confirma la reserva
        (3, 'Lista para retiro'), #lista para ser retirada
        (4, 'Retirada'), #reserva retirada por el cliente
        (5, 'Devuelta'), #reserva devuelta
        (6, 'Cancelada') #reserva cancelada por el cliente o la biblioteca
    ]

    #atributos
    numero                  = models.AutoField(primary_key=True)
    usuario                 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion          = models.DateTimeField(auto_now_add=True) #creacion de la reserva cuando el cliente carga el primer libro en el carrito
    cantidad_libros         = models.PositiveSmallIntegerField(default=0) #cantidad de libros agregados a la reserva
    fecha_confirmacion      = models.DateField(blank=True, null=True) #fecha en que el cliente confirma la reserva
    fecha_compromiso        = models.DateField(blank=True, null=True) #fecha en que la biblioteca se comprometa a tener lista la reserva
    fecha_lista_retiro      = models.DateField(blank=True, null=True) #fecha real de lista para retirar
    fecha_maxima_retiro     = models.DateField(blank=True, null=True) #fecha maxima en que el cliente puede retirar antes de que se cancele la reserva
    fecha_retiro            = models.DateField(blank=True, null=True) #fecha en que el cliente retira la reserva
    fecha_maxima_devolucion = models.DateField(blank=True, null=True) #fecha maxima que tiene el cliente para devolver los libros desde la fecha de retiro
    fecha_devolucion        = models.DateField(blank=True, null=True) #fecha en que el cliente devuelve la reserva
    fecha_cancelacion       = models.DateField(blank=True, null=True) #fecha de cancelacion de la reserva, ya sea por el cliente o por la biblioteca
    estado_reserva          = models.PositiveSmallIntegerField(choices=ESTADOS_RESERVA, default=1)
    ultima_actualizacion    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.numero} - {self.usuario}'


#detalle reserva
class DetalleReserva(models.Model):
    id_detalle_reserva = models.BigAutoField(primary_key=True)
    reserva            = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    libro              = models.ForeignKey(Libro, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('reserva', 'libro')

    def __str__(self):
        return f'{self.reserva} - {self.libro}'
