from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    state_code  = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/states"

class City(models.Model):
    name = models.CharField(max_length=100)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    dist_code = models.IntegerField(default=0)
    population_total = models.IntegerField(default=0)
    population_male = models.IntegerField(default=0)
    population_female = models.IntegerField(default=0)
    population_child_total = models.IntegerField(default=0)
    population_child_male = models.IntegerField(default=0)
    population_child_female = models.IntegerField(default=0)
    literate_total = models.IntegerField(default=0)
    literate_male = models.IntegerField(default=0)
    literate_female = models.IntegerField(default=0)
    sex_ratio = models.IntegerField(default=0)
    child_sex_ratio = models.IntegerField(default=0)
    effective_literacy_rate_total = models.FloatField(default = 0.0)
    effective_literacy_rate_male = models.FloatField(default=0.0)
    effective_literacy_rate_female = models.FloatField(default=0.0)
    location = models.CharField(max_length=100, blank=True, null=True)
    total_graduates = models.IntegerField(default=0)
    male_graduates = models.IntegerField(default=0)
    female_graduates = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'cities'




    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return "/cities"
