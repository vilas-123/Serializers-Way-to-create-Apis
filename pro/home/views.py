from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PeopleSerializer


@api_view(['GET','POST','DELETE'])
def index(request):
    courses={
      'course_name':'python',
      'learn':['flask','django'],
      'course_provider':'beehyv'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
    elif request.method == 'POST':
        data = request.data
        print(data['age'])
    return Response(courses)
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def person(request,pid=None):
    if request.method == 'GET':
        if pid:
            objs = Person.objects.filter(id=pid)
        else:
            objs = Person.objects.all()

        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PUT':

        data = request.data

        try:

            instance = Person.objects.get(id=data.get('id'))

        except Person.DoesNotExist:

            return Response({'error': 'Person does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PeopleSerializer(instance, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PATCH':

        data = request.data

        try:

            instance = Person.objects.get(id=data.get('id'))

        except Person.DoesNotExist:

            return Response({'error': 'Person does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PeopleSerializer(instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})
