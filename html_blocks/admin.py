from django.conf import settings
from django.contrib import admin

if 'modeltranslation' in (settings.INSTALLED_APPS):
    from modeltranslation.admin import TranslationAdmin

    class html_block_Admin(TranslationAdmin):
        list_display = ('title','position',)
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
    class html_block_Admin(admin.ModelAdmin):
        list_display = ('title','position',)

admin.site.register(html_block, html_block_Admin)
