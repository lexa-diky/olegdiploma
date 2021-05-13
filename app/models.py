from django.db import models


class AdminFormModel(models.Model):
    id = models.IntegerField("_id", primary_key=True)
    title = models.TextField("title")
    fields = models.TextField("available_fields")


class MySuperModel(models.Model):
    id = models.IntegerField("_id", primary_key=True)
    field1 = models.TextField("field1", null=True)
    field2 = models.TextField("field2", null=True)
    field3 = models.TextField("field3", null=True)
