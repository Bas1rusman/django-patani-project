from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=200)  
    email = models.EmailField(unique=True)  
    ktp_number = models.CharField(max_length=16, unique=True)  
    address = models.TextField()  

    def __str__(self):
        return self.full_name  


class Proyek(models.Model):
    id_proyek = models.AutoField(primary_key=True)
    type_proyek = models.CharField(max_length=50)
    nama_proyek = models.CharField(max_length=100)
    lokasi_proyek = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_proyek


class Petani(models.Model):
    id_petani = models.AutoField(primary_key=True)  
    presentase_keuntungan = models.DecimalField(max_digits=5, decimal_places=2)  
    jatuh_tempo = models.DateField()  
    rata_rata_keuntungan = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.id_petani  
