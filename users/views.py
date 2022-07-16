from django.shortcuts import render

# Response Class to send http/json response 
from rest_framework.response import Response
# Base Class View for extending custom class as a view
from rest_framework.views import APIView


# Class based Sign Up View
class SignUpView(APIView):
    
    # Validate & Sanitize Input

    # Check for already existing user 

    # Store in DB & Return    
    def post(self,request,*args,**kwargs):

        # Store In DB


        # Generate Auth Token & set as cookie        
        headers={}

        # Return 
        return Response(
            status=200,
            content_type="application/json",
            headers=headers,
            data={'success':1,'error':None,'result':'user created successfully'}
            )

    
# Sign In
class SignInView(APIView):
    
    # Validate & Sanitize user input

    # Look Up in DB
    def get(self,request,*args,**kwargs):

        # Generate Auth Token & Log In user
        headers={}

        return Response(
            status=200,
            content_type="application/json",
            headers=headers,
            data={'success':1,'error':None,'result':'logged in'}
            )

# Log out 
class LogoutView(APIView):
    # Remove token from user cookies 
    # Black list jwt 
    def get(self,request):
        return Response(status=200,
                        content_type="application/json",
                        data={'success':1,'result':'logged out','error':None},
                        )