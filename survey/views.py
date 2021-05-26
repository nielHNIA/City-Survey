from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count, F, Max, Sum


from .models import *
from .forms import *
# Create your views here.




class HomeView(TemplateView):
    template_name = 'survey/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['states'] = State.objects.all()
        total_city_in_state = State.objects.annotate(cities = Count('city'))
        #total_states = State.objects.aggregate(sum=Sum('states'))
        #print(total_states)

        print(vars(State.objects.all()[0]))
        #print(total_city_in_state)
        #print(vars(total_city_in_state[0]))
        #print(total_city_in_state)
        #x = total_city_in_state[0]
        #print(x.cities)

        context['total_city_in_state'] = total_city_in_state


        return context


class CityView(ListView):
    template_name = 'survey/cities.html'
    model = City


def city(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'survey:city_detail.html', {'city': city})


class NewCityView(CreateView):
    model = City
    template_name = "survey/new_city.html"
    form_class = CreateCityForm

class UpdateCityView(UpdateView):
    template_name = "survey/update_city.html"
    model = City
    form_class = CreateCityForm


class StateListView(TemplateView):
    template_name = 'survey/states.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['states'] = State.objects.all()
        total_city_in_state = State.objects.annotate(cities = Count('city'))
        context['total_city_in_state'] = total_city_in_state
        print(vars(total_city_in_state[0]))
        return context
"""total_city_in_state

def states(request):
    States = State.objects.all()
    cities = City.objects.all()
    total_city_in_state = State.objects.annotate(cities = Count('city'))
    context = {'states': states, 'cities': cities, 'total_city_in_state': total_city_in_state}
    x = total_city_in_state[0]
    print(x.cities)
    return render(request, 'survey/states.html', context)


def state(request, state_id):
    state = models.objects.get(id=state_id)
    cities = state.city_set.all()
    context = {'state': state, 'cities': cities}

    return render(request, 'survey/state.html', context)

"""

class StateView(DetailView):
    template_name = 'survey/state.html'
    model = State
    context_object_name = 'state'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state = State.objects.get(id=id)
        print(var(state[0]))

        cities = state.city_set.all()
        context['state'] = state
        context['cities'] = cities


        return context






class NewStateView(CreateView):
    model = State
    template_name = "survey/new_state.html"
    form_class = CreateStateForm

class UpdateCityView(UpdateView):
    template_name = "survey/update_state.html"
    model = State
    form_class = CreateCityForm
