from django.contrib import admin
from .models import *

admin.site.site_header = '妙妙护工评价系统'
admin.site.site_title = '妙妙护工评价系统后台'

admin.site.register(User)
admin.site.register(Authority)
admin.site.register(Hospital)
admin.site.register(Carer)
admin.site.register(Evaluation)

