from django.shortcuts import render, redirect
import os
from django.urls import reverse_lazy
from django.contrib import messages
from demo.apps.user.models import User
from django.http import JsonResponse
import datetime
import requests
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db.models import Q


def inicio(request):
    usuarios = [x for x in User.objects.all() if x.score and x.username_scorm and x.id_user_scorm]
    if usuarios:
        last_user = max([x.id for x in usuarios])
    else:
        last_user = None
    return render(request,"inicio.html",{
        "usuarios": sorted(usuarios, key=lambda x: float(x.score), reverse=True) if usuarios else [],
        "last_user": last_user
    })


def avatar(request):
    list_avatars = [
        [1,'https://images.unsplash.com/photo-1603322199363-14380ec2ba31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 'Avatar uno'],
        [2,'https://images.unsplash.com/photo-1546753051-f9cbab09c91b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80', 'Avatar dos'],
        [3,'https://images.unsplash.com/photo-1603322199363-14380ec2ba31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 'Avatar tres'],
        [4,'https://images.unsplash.com/photo-1603322199363-14380ec2ba31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 'Avatar cuatro'],
        [5,'https://images.unsplash.com/photo-1603322199363-14380ec2ba31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 'Avatar cinco'],
        [6,'https://images.unsplash.com/photo-1603322199363-14380ec2ba31?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 'Avatar seis'],
    ]

    return render(request,"avatar.html",{
        "list_avatars": list_avatars,
    })