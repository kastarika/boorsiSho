from django.contrib import admin

# Register your models here.

from . import models

admin.site.register( models.Company )
admin.site.register( models.FinancialRatio )
admin.site.register( models.Category )
admin.site.register( models.Industry )
admin.site.register( models.FinancialYear )