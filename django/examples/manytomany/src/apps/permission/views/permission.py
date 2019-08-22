from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

from ..models import PermissionModel
from ..serializers.permission import PermissionSerializer


class PermissionView(APIView):

    def get(self, req):
        permissions = PermissionModel.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        res = {
            'status': 200,
            'msg': 'successfully',
            'data': serializer.data
        }
        return Response(res)

    def post(self, req):
        serializer = PermissionSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res = {
            'status': 200,
            'msg': 'method post',
        }
        return Response(res)

    def put(self, req, id):
        res = {
            'status': 200,
            'msg': 'method put',
        }
        return Response(res)

    def delete(self, req, id):
        res = {
            'status': 200,
            'msg': 'method delete',
        }
        return Response(res)