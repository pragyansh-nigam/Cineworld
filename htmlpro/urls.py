from django.urls import path
from . import views

urlpatterns=[
				path("home",views.home),
				path("swades",views.swades),
				path("tdk",views.tdk),
				path("got",views.got),
				path("cast",views.cast),
				path("signup",views.signup),
				path("login",views.login)
			]