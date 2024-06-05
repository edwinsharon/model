from rest_framework.decorators import api_view
from rest_framework.response import Response


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