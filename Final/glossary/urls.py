from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # optional: homepage
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='glossary/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Glossary related
    path('glossary/', views.glossary, name='glossary'),  # updated to use glossary (not glossary_view)
    path('glossary/add/', views.create_term, name='create_term'),
    path('glossary/edit/<int:term_id>/', views.edit_term, name='edit_term'),
    path('glossary/delete/<int:term_id>/', views.delete_term, name='delete_term'),
    path('glossary/favorite/<int:term_id>/', views.toggle_favorite, name='toggle_favorite'),  # needed for favoriting
    path('glossary/search/', views.search_terms, name='search_terms'),  # live search
    path('profile/', views.profile, name='profile'),  # user profile
]
