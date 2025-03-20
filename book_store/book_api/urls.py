from django.urls import path,include
from .views import AuthorViewSet,CategoryViewSet,BookViewSet,ReviewViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'authors',AuthorViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'books',BookViewSet)
router.register(r'reviews',ReviewViewSet)
urlpatterns = [
    path('',include(router.urls)),
 ]