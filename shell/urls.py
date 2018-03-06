from django.conf.urls import url, include # Notice we added include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('django_socketio.urls')),
    url(r'^', include('apps.first_app.urls')) # And now we use the include function to pull in our first_app.urls...
]

urlpatterns += [
    url("", include('django_socketio.urls')),
]