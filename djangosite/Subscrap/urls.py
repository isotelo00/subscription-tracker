from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SubscriptionPostView, SubscriptionDetailView, SubscriptionCreateView

urlpatterns = [
    path('', views.home, name='subscrap-home'),
    path('create/', views.createSub),
    path('edit/', views.editSub),
    #path('testMain/', views.testMain),
    path('testMain/', SubscriptionPostView.as_view(), name='user-page'),
    path('sub/<int:pk>/', SubscriptionDetailView.as_view(), name='user-detail-page'),
    path('sub/new/', SubscriptionCreateView.as_view(), name='user-create-page'),
    #path('Login/', views.login, name='subscrap-login'),
    #path('Signup/', views.signup, name='subscrap-signup'),
    path('', include("django.contrib.auth.urls")),

]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
