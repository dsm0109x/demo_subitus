from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from demo.apps.user.models import User
import string
import random


@csrf_exempt
@api_view(
    ["POST",]
)
@permission_classes((AllowAny,))
def send_data(request):
    username = request.data.get("username")
    id_user = request.data.get("userid")
    id_course = request.data.get("courseid")
    score = request.data.get("score")
    avatar = request.data.get("avatar")
    id_level = request.data.get("levelid")
    if username is None or id_course is None or score is None or id_level is None:
        return Response(
            {"error": "Please provide the data ):"},
            status=HTTP_400_BAD_REQUEST,
        )
    else:
        all_users = [x for x in User.objects.all() if x.id_user_scorm == id_user]
        if all_users:
            u = all_users[0]
        else:
            randomm = ''.join(random.choices(string.ascii_uppercase, k=10))
            u = User.objects.create(username=id_user, email="{}@gmail.com".format(randomm), password="hola1234", score=score)
            u.username_scorm = username
            u.avatar = avatar
            u.id_user_scorm = id_user
            u.id_course_scorm = id_course
            u.id_level_scorm = id_level
            u.save()

        return Response(
            {
                "code": 200,
                "reason": "OK"
            },
            status=HTTP_200_OK,
        )


@csrf_exempt
@api_view(
    ["GET",]
)
@permission_classes((AllowAny,))
def last_user(request):
    last_user = User.objects.all()
    last_user = [x for x in last_user if x.score]
    last_user = max([x.id for x in last_user])
    return Response(
        {
            "last_user": last_user,
        },
        status=HTTP_200_OK,
    )