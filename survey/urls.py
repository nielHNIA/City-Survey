from django.urls import path

app_name = 'survey'

from . import views
#import survey.api_views

urlpatterns = [

        # path('api/cities/', survey.api_views.CityList.as_view()),
         #path('api/cities/<int:id>/', survey.api_views.CityRetrieveUpdateDestroy.as_view()),

         path('', views.HomeView.as_view(), name='index'),
         path('states/', views.StateListView.as_view(), name="states"),

         path('cities/', views.CityView.as_view(), name="cities"),
         #path('states/<int:id/>', views.StateView.as_view(), name="state"),
         path('newcity/', views.NewCityView.as_view(), name="new_city"),
        # path('cities/<slug:pk>/update', views.UpdateCityView.as_view(), name="update_city"),

]
