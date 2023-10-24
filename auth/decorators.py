from rest_framework.response import Response
from rest_framework import status

def is_self_or_admin_authentication(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.id == kwargs['id'] or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return Response({
                "error":"access denied"
            },status=status.HTTP_400_BAD_REQUEST)

    return wrapper_func

def is_admin_authentication(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return Response({
                "error":"access denied"
            },status=status.HTTP_400_BAD_REQUEST)

    return wrapper_func