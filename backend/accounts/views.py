from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    data = {
        "message":f"Hello {request.user.first_name}, welcome to your user area"
    }
    return Response(data)