from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
#from .serializer import*
#from djapp.serializer import EmployeeSerializer
#from myproject.djapp.serializer import EmployeeSerializer
from myapp.serializer import CandidateSerializer

from myapp.models import*
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  myapp.serializer import CandidateSerializer
from rest_framework import status
# Create your views here.



@api_view(['POST'])
def post_candidate_details(request):
    if request.method == "POST":
        username = request.data.get('username')
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        pasword = request.data.get('pasword')
        confirm_pasword = request.data.get('confirm_pasword')

        if candidate.objects.filter(email=email).exists():
            return Response({'message': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if pasword != confirm_pasword:
            return Response({'message': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CandidateSerializer(data={
                    'username': username,
                    'email': email,
                    'mobile': mobile,
                    'pasword': pasword,
                    'confirm_pasword': confirm_pasword
                })

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_candidate(request):
    if request.method == "POST":
        email = request.data.get('email')
        pasword = request.data.get('pasword')
        candidate_details = candidate.objects.filter(email=email).first()
        if candidate_details:
    
            if candidate_details.pasword == pasword:
                return Response ({'message':'logged in succesfully'})
                
            else:
                return Response({'message':'incorrect password,try again.'})

        else:
            return Response({'message':'email does not exits.'})
