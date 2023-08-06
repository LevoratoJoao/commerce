from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("category/<str:name>", views.category_view, name="category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("categories", views.categories_view, name="categories"),
    path("create", views.create_view, name="create")
]
