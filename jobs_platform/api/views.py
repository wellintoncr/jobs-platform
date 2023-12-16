from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from api.models import Job
from django.contrib.auth.models import User
from api.serializers import JobSerializer, UserSerializer
from rest_framework import mixins, generics, renderers, viewsets
from rest_framework.reverse import reverse
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'jobs': reverse('job-list', request=request, format=format)
#     })

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def meta_name(self, request, *args, **kwargs):
        job = self.get_object()
        return Response(job.meta_name)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class JobMetaName(generics.GenericAPIView):
#     queryset = Job.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         job = self.get_object()
#         return Response(job.meta_name)

# class JobList(generics.ListCreateAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)

# class JobDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class JobList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class JobDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# class JobList(APIView):
#     def get(self, request, format=None):
#         jobs = Job.objects.all()
#         serializer = JobSerializer(jobs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = JobSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class JobDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Job.objects.get(pk=pk)
#         except Job.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         job = self.get_object(pk)
#         serializer = JobSerializer(job)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         job = self.get_object(pk)
#         serializer = JobSerializer(job, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         job = self.get_object(pk)
#         job.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def job_list(request):
#     if request.method == 'GET':
#         jobs = Job.objects.all()
#         serializer = JobSerializer(jobs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = JobSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def job_detail(request, pk):
#     try:
#         job = Job.objects.get(pk=pk)
#     except Job.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = JobSerializer(job)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = JobSerializer(job, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         job.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# @csrf_exempt
# def job_list(request):
#     if request.method == 'GET':
#         jobs = Job.objects.all()
#         serializer = JobSerializer(jobs, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = JobSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.erros, status=400)
    
# @csrf_exempt
# def job_detail(request, pk):
#     try:
#         job = Job.objects.get(pk=pk)
#     except Job.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = JobSerializer(job)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = JobSerializer(job, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         job.delete()
#         return HttpResponse(status=204)