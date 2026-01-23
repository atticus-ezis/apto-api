from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class VerifyUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "email": user.email,
                "username": user.username,
                "groups": [group.name for group in user.groups.all()],
            }
        )
