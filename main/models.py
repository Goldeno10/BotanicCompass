from django.db import models


class PlantData(models.Model):
    scientific_name = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'plant_data'


class HausaName(models.Model):
    plant_data = models.ForeignKey(PlantData, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='hausa_name')
    name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'hausa_name'


class CommonName(models.Model):
    plant_data = models.ForeignKey(PlantData, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='common_name')
    name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'common_name'


class Synonym(models.Model):
    plant_data = models.ForeignKey(PlantData, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='synonym')
    name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'synonym'
