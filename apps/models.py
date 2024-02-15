from django.db import models
from django_resized import ResizedImageField
from django.db.models import DateField
class Project(models.Model):
    title = models.CharField(max_length=255)
    image = ResizedImageField(size=[400, 150], crop=['middle', 'center'], upload_to='project/images',
                              default='project/default.png')
    created_at = DateField(auto_now_add=True)



