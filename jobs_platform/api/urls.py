from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
# from api.views import  JobViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet, basename='job')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]

# job_list = JobViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# job_detail = JobViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# job_meta_name = JobViewSet.as_view({
#     'get': 'meta_name'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('jobs/', job_list, name='job-list'),
#     path('jobs/<int:pk>', job_detail, name='job-detail'),
#     path('jobs/<int:pk>/meta_name', job_meta_name, name='job-meta-name'),
#     path('users/', user_list, name='users-list'),
#     path('users/<int:pk>', user_detail, name='user-detail')
# ])

# urlpatterns = [
#     path('', views.api_root),
#     path('jobs/', views.JobList.as_view(), name='job-list'),
#     path('jobs/<int:pk>/', views.JobDetail.as_view(), name='job-detail'),
#     path('jobs/<int:pk>/meta_name/', views.JobMetaName.as_view(), name='job-meta-name'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)