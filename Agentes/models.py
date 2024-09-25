from django.db import models

# Create your models here.

class Sector (models.Model):
    nombre = models.CharField(max_length=30)
    

    def __str__ (self):
        textosector = "{0}"
        return textosector.format(self.nombre)


class Area (models.Model):
    nombre = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector,null=True,blank=True,on_delete=models.CASCADE)

    def __str__ (self):
        textoarea = "{0}"
        return textoarea.format(self.nombre)


class Agente(models.Model):
    legajo = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)
    area = models.ForeignKey(Area,null=True,blank=True,on_delete=models.CASCADE)


    def __str__ (self):
        textoagente = "{0}"
        return textoagente.format(self.nombre)


compensar=[
    (0, 'A compensar'),
    (1,'Compensar')
]

class Compensatorio(models.Model):
    #legajo=models.CharField(max_length=4)
    legajo= models.ForeignKey(Agente,null=True,blank=False,on_delete=models.CASCADE)
    diaCompensatorio=models.DateField()
    horas=models.IntegerField()
    detalle=models.CharField(max_length=100)
    motivo=models.IntegerField(null=False,blank=False,choices=compensar)

    def __str__ (self):
        comp = "{0}{1}{2}{3}"
        return comp.format(self.legajo, self.diaCompensatorio, self.horas, self.detalle)
    

vacaciones=[
    (0, 'A tomar'),
    (1,'Tomar')
]

class Vacaciones(models.Model):
    #legajo=models.CharField(max_length=4)
    legajo= models.ForeignKey(Agente,null=True,blank=False,on_delete=models.CASCADE)
    diaVacaciones=models.DateField()
    dias=models.IntegerField()
    detalle=models.CharField(max_length=100)
    motivo=models.IntegerField(null=False,blank=False,choices=vacaciones)

    def __str__ (self):
        comp = "{0}{1}{2}{3}"
        return comp.format(self.legajo, self.diaVacaciones, self.dias, self.detalle)


permisos=[
    (0, 'Compensatorio**'),
    (1,'Comisión***'),
    (2, 'Art. 155 (Trámite)****'),
    (3,'Permiso Especial'),
    (4, 'Citación Judicial'),
    (5, 'Donación de sangre'),
    (6,'Licencia Ordinaria Anual'),
    (7, 'Licencia por Matrimonio'),
    (8,'Licencia Matrimonio Hijos'),
    (9, 'Licencia Nacimiento Hijos'),
    (10,'Licencia Examen'),
    (11, 'Licencia Fallecimiento de Pariente*')
]

mes=[
   
    (2, 'Febrero'),
    (3,'Marzo'),
    (4, 'Abril'),
    (5, 'Mayo'),
    (6,'Junio'),
    (7, 'Julio'),
    (8,'Agosto'),
    (9, 'Septiembre'),
    (10,'Octubre'),
    (11, 'Noviembre'),
    (12, 'Diciembre')
]
class Articulo(models.Model):
    #legajo=models.CharField(max_length=4)
    legajo= models.ForeignKey(Agente,null=True,blank=False,on_delete=models.CASCADE)
    diaCreacion=models.DateField()
    diaArticulo=models.DateField()
    permiso=models.IntegerField(null=False,blank=False,choices=permisos)
    cantidadDias=models.IntegerField(null=True,blank=True)
    cantidadHoras=models.TimeField(null=True,blank=True)
    parentesco=models.CharField(max_length=50,null=True,blank=True)
    com=models.CharField(max_length=100,null=True,blank=True)
    nitro=models.IntegerField(null=True,blank=True, choices=mes)
    art155=models.CharField(max_length=100,null=True,blank=True)
    

    def __str__ (self):
        comp = "{0}{1}"
        return comp.format(self.legajo, self.diaArticulo)
