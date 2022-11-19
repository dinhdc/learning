from django.contrib import admin
from app.models import RuleModel
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RuleResource(resources.ModelResource):

    class Meta:
        model = RuleModel
        fields = ['code', 'profitability', 'activity',
                  'liquidity', 'debt', 'market', 'label']


class RuleAdmin(ImportExportModelAdmin):
    resource_classes = [RuleResource]


admin.site.register(RuleModel, RuleAdmin)
