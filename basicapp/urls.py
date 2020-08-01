from django.conf.urls import url
from basicapp import views
from django.contrib.auth import views as auth_views
from ApplMang import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.AboutView.as_view(),name='home'),
    url(r'^application/(?P<pk>\d+)$',views.ApplicationDetailView.as_view(),name='application_detail'),
    url(r'^application/new/$',views.ApplicationView.as_view(),name='application'),
    url(r'^register/$',views.RegisterView,name='register'),
    url(r'^login/$',views.LoginView,name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),

    url(r'^apply/$',views.student_view,name='apply'),
    url(r'^application/(?P<pk>\d+)/approve',views.approve_application,name='approve'),
    url(r'^application/(?P<pk>\d+)/reject',views.reject_application,name='reject'),
    url(r'^hod_cse/$',views.CSEApplication,name='hod_cse'),
    url(r'^hod_ece/$',views.ECEApplication,name='hod_ece'),
    url(r'^hod_ce/$',views.CEApplication,name='hod_ce'),
    url(r'^hod_ee/$',views.EEApplication,name='hod_ee'),
    url(r'^hod_me/$',views.MEApplication,name='hod_me'),
    url(r'^hod_ei/$',views.EIApplication,name='hod_ei'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)