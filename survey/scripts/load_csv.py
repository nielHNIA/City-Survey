import csv

from survey.models import City, State

def run():
    fhand = open('./cities_r2.csv')
    reader = csv.DictReader(fhand)
    State.objects.all().delete()
    City.objects.all().delete()

    for row in reader:
        print(row)
        s, created = State.objects.get_or_create(name=row['state_name'], state_code=row['state_code'])
        city = City(name = row['name_of_city'], state = s)

        city.dist_code = row['dist_code']
        city.population_total = row['population_total']
        city.population_male = row['population_male']
        city.population_female = row['population_female']
        city.population_child_total = row['0-6_population_total']
        city.population_child_male = row['0-6_population_male']
        city.population_child_female = row['0-6_population_female']
        city.literate_total = row['literates_total']
        city.literate_male = row['literates_male']
        city.literate_female = row['literates_female']
        city.sex_ratio = row['sex_ratio']
        city.child_sex_ratio = row['child_sex_ratio']
        city.effective_literacy_rate_total =  row['effective_literacy_rate_total']
        city.effective_literacy_rate_male = row['effective_literacy_rate_male']
        city.effective_literacy_rate_female = row['effective_literacy_rate_female']
        city.location = row['location']
        city.total_graduates = row['total_graduates']
        city.male_graduates = row['male_graduates']
        city.female_graduates = row['female_graduates']
        city.save()





"""for row in DictReader(open('./cities_r2.csv')):
    city = City()
    city.name = row['name_of_city']
    city.state_code = row['state_code']
    city.dist_code = row['dist_code']
    city.population_total = row['population_total']
    city.population_male = row['population_male']
    city.population_female = row['population_female']
    city.population_child_total = row['0-6_population_total']
    city.population_child_male = row['0-6_population_male']
    city.population_child_female = row['0-6_population_female']
    city.literate_total = row['literates_total']
    city.literate_male = row['literates_male']
    city.literate_female = row['literates_female']
    city.sex_ratio = row['sex_ratio']
    city.child_sex_ratio = row['child_sex_ratio']
    city.effective_literacy_rate_total =  row['effective_literacy_rate_total']
    city.effective_literacy_rate_male = row['effective_literacy_rate_male']
    city.effective_literacy_rate_female = row['effective_literacy_rate_female']
    city.location = row['location']
    city.total_graduates = row['total_graduates']
    city.male_graduates = row['male_graduates']
    city.female_graduates = row['female_graduates']"""
