from django.db import models
from django.conf import settings
from django.utils import timezone

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query)
        )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    descripition = models.TextField('Descrição')
    topics = models.TextField('Tópicos')
    workload = models.IntegerField('Carga horária')

    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/cursos/%i/" % self.pk

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"
        ordering = ['name']



class Turma(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    inscricao_inicio = models.DateField()
    inscricao_fim = models.DateField()
    arquivado = models.BooleanField()
    curso = models.ForeignKey(Course, on_delete=models.CASCADE)
    monitor = models.CharField(max_length=45)
    link_aula = models.CharField(max_length=150, null=True, blank=True)
    link_inscricao = models.CharField(max_length=150, null=True, blank=True)
    escolha_local = (
        ('TG', 'Taguatinga'),
        ('AS', 'Asa Norte')
    )
    local = models.CharField(
        max_length=10,
        choices= escolha_local,
        default='TG'
    )

    def __str__(self):
        nome = self.curso.__str__() + " " + self.data_inicio.__str__()
        return nome
    def get_absolute_url(self):
        return "/cursos/%i/" % self.pk



'''
class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0,'Pendente'),
        (1,'Aprovado'),
        (2,'Cancelado'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Usuário",
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course, verbose_name='Curso', related_name='enrollments'
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=1, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)
'''