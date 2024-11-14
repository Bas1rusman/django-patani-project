from django.contrib import admin
from .models import Item, Person, Proyek, Petani

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'ktp_number')


@admin.register(Proyek)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('id_proyek', 'type_proyek', 'nama_proyek', 'lokasi_proyek')

@admin.register(Petani)
class ProyekAdmin(admin.ModelAdmin):
    list_display = ('id_petani', 'presentase_keuntungan', 'jatuh_tempo', 'rata_rata_keuntungan')

