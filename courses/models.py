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
    descripition = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de início', null=True, blank=True
    )

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


class Announcement(models.Model):
    '''course = models.ForeignKey(Course, verbose_name="Curso")'''
    tittle = models.CharField('Título', max_length=100)
    content = models.TextField("Conteúdo")

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

class Comment(models.Model):
    '''announcement = models.ForeignKey(Announcement, verbose_name='Anúncio', related_name='comments')'''
    comment = models.TextField("Comentário")

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['created_at']

class lesson(models.Model):
    name = models.CharField('Nome', max_length=100)
    desccription = models.TextField('Descrição', blank=True)
    number = models.IntegerField('Numero (ordem)', blank=True, default=0)
    release_date = models.DateField('Data de liberação', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.release_date:
            today = timezone.now().date()
            return self.release_date >= today
        return False

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['number']


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