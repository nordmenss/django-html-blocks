from django.conf import settings
from django.contrib import admin
from html_blocks.models import *
from ckeditor_widget.widgets import *

if 'modeltranslation' in (settings.INSTALLED_APPS):
    from modeltranslation.admin import TranslationAdmin

    class html_block_admin(TranslationAdmin):
        list_display = ('title','position',)
        formfield_overrides = {
           RichTextField:{"widget":CKEditorWidget(config_name='default')},
        }
        class Media:
            js = (
                settings.MEDIA_URL+'js/admin/force_jquery.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
                settings.MEDIA_URL+'js/admin/tabbed_translation_fields.js',
            )
            css = {
                'screen': (settings.MEDIA_URL+'css/admin/tabbed_translation_fields.css',),
            }
else:
    from django.contrib import admin
    class html_block_admin(admin.ModelAdmin):
        list_display = ('title','position',)

admin.site.register(html_block, html_block_admin)
