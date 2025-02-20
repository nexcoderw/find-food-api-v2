from rest_framework import status
from account.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginView(APIView):
    permission_classes = []  # No authentication required for login

    def post(self, request, *args, **kwargs):
        """Handle login and return JWT tokens with detailed validation messages."""
        serializer = LoginSerializer(data=request.data)

        # If serializer is valid, send back the JWT tokens
        if serializer.is_valid():
            return Response(
                {
                    "access": serializer.validated_data['access'],
                    "refresh": serializer.validated_data['refresh']
                },
                status=status.HTTP_200_OK
            )

        # If validation fails, return detailed error messages
        return Response(
            {"detail": "Validation error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
