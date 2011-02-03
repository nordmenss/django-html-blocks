from django.db import models
from ckeditor.fields import RichTextField

class html_block(models.Model):
    title=models.CharField(max_length=150)
    position=models.CharField(max_length=150)
    content=RichTextField(blank = True, null = True,unique=True)

    class Meta():
        db_table = 'html_blocks'
        ordering=('-title','position')