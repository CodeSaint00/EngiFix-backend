from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, StudentRegisterSerializer, TechnicianRegisterSerializer

class StudentRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = [permissions.AllowAny]

class TechnicianRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TechnicianRegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "role": user.role,
            "is_verified": user.is_verified,
        })

class TechnicianListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(role=User.Role.TECHNICIAN)

class VerifyTechnicianView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            technician = User.objects.get(pk=pk, role=User.Role.TECHNICIAN)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        technician.is_verified = True
        technician.save()
        return Response(UserSerializer(technician).data)