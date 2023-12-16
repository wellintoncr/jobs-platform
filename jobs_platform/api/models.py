from django.db import models

# Create your models here.
class Job(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='jobs', on_delete=models.CASCADE, default=None)
    meta_name = models.TextField(default="Default")

    @property
    def full_name(self):
        return f"{self.name} mais uma série de coisas"

    def save(self, *args, **kwargs):
        self.meta_name = f'{self.name} com sobrenome'
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['id']