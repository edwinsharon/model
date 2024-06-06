from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import person
from .serializers import Peopleserializer

person.objects.all()

@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == 'GET':
        people_details={
            'name':'edwin',
            'age':22,
            'place':'idukki',
        } 
        return Response(people_details)
    elif request.method == 'POST':
        people_details={
            'name':'sharon',
            'age':22,
            'place':'idukki',
        }    
        return Response(people_details) 
    elif request.method == 'PUT':
        people_details={
            'name':'edwin',
            'age':22,
            'place':'idukki',
        }     
        return Response(people_details)
    
@api_view(['GET','POST'])
def people(request):
    if request.method == 'GET':
        objs = person.objects.all()
        serializer = Peopleserializer(objs,many=True)
        return Response(serializer.data)
    else:
        data=request.data
        serializer=Peopleserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(request,serializer.errors)
