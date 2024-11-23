from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('explore/', views.explore, name='explore'),
path('travelreg/', views.travelreg, name='travelreg'),
path('login/', views.login, name='login'),
path('explore2/', views.explore2, name='explore2'),
path('p1/', views.p1, name = 'p1'),
path('p2/', views.p2, name = 'p2'),
path('privacy/', views.privacy, name = 'privacy'),
path('medical/', views.medical, name = 'medical'),
path('local_transport/', views.local_transport, name = 'local_transport'),
path('term_and_condition/', views.term_and_condition, name = 'term_and_condition'),
path('work/', views.work, name = 'work'),
path('our_process/', views.our_process, name = 'our_process'),
path('insight/', views.insight, name = 'insight'),
path('contact/', views.contact, name = 'contact'),
path('bookform/', views.bookform, name = 'bookform'),
path('registr/', views.registr, name = 'registr'),
path('demoview/', views.create_views, name = 'create_views'),
]