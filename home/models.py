from django.db import models

# Create your models here.
class Monitor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField(max_length=100)
    link_monitoria = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    wpp = models.CharField(max_length=9)
    escolha_local = (
        ('TG', 'Taguatinga'),
        ('AS', 'Asa Norte')
    )
    local = models.CharField(
        max_length=10,
        choices=escolha_local,
        default='TG'
    )
    arquivado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome