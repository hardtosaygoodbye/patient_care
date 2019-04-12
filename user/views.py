from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
from decimal import Decimal

def token2user(token):
    try:
        authority = Authority.objects.get(token = token)
    except:
        raise Http404
    return authority.user

class UserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not (username and password):
            return Response({'detail': 'username,password required'}, 404)
        users = User.objects.filter(username = username)
        if len(users) != 0:
            return Response({'detail': '该用户名已注册'}, 400)
        userSerializer = UserSerializer(data = request.data)
        if not userSerializer.is_valid():
            return Response(userSerializer.errors, 400)
        userSerializer.save()
        try:
            user = User.objects.get(username = username)
        except:
            return Response({'detail': '注册失败'}, 400)
        userSerializer = UserSerializer(user)
        authority = Authority(user = user)
        return Response({
            'code': 0, 
            'user': userSerializer.data, 
            'token': authority.token
        })
    def put(self, request):
        token = request.data.get('token')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not (token and old_password and new_password):
            return Response({'detail': 'username,old_password,new_password\
            required'}, 404)
        user = token2user(token)
        if user.password != old_password:
            return Response({"detail": "用户密码错误"}, 400)
        user.password = new_password
        user.save()
        userSerializer = UserSerializer(user)
        return Response({
            'code': 0,
            'user': userSerializer.data
        })

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not (username and password):
            return Response({'detail': 'username, password required'}, 404)
        try:
            user = User.objects.get(username = username,\
            password = password)
        except:
            return Response({'detail': '用户名或者密码错误'}, 400)
        userSerializer = UserSerializer(user)
        authority = Authority(user = user)
        return Response({
            'code': 0,
            'user': userSerializer.data,
            'token': authority.token
        })

class HospitalView(APIView):
    def get(self, request):
        hospitals = Hospital.objects.all()
        hospitalSerializers = HospitalSerializer(hospitals, many = True)
        return Response({'code': 0, 'hospitals': hospitalSerializers.data})

class CarerView(APIView):
    def get(self, request):
        hospital_id = request.GET.get('hospital_id')
        if not hospital_id:
            return Response({'detail': 'hospital required'}, 404)
        try:
            hospital = Hospital.objects.get(pk = hospital_id)
        except:
            return Response({'detail': 'hospital not exist'}, 400)
        carers = Carer.objects.filter(hospital = hospital)
        carerSerializers = CarerSerializer(data = carers, many = True)
        return Response({'code': 0, 'carers': carerSerializers.data})

class EvaluationView(APIView):
    def post(self, request):
        token = request.data.get('token')
        carer_id = request.data.get('carer_id')
        scores = request.data.get('scores')
        tip = request.data.get('tip')
        side = request.data.get('side')
        if not (token and carer_id and scores and tip and side):
            return Response({'detail': 'token,carer_id,scores,tip,side\
            required'}, 404)
        score_arr = scores.split(",")
        score_arr = [Decimal(i) for i in score_arr]
        user = token2user(token)
        side = int(side)
        try:
            carer = Carer.objects.get(pk = carer_id)
        except:
            return Response({'detail': 'carer not found'}, 404)
        evalutation = Evaluation(
            user = user,
            carer = carer,
            q1 = score_arr[0],
            q2 = score_arr[1],
            q3 = score_arr[2],
            q4 = score_arr[3],
            q5 = score_arr[4],
            q6 = score_arr[5],
            q7 = score_arr[6],
            q8 = score_arr[7],
            q9 = score_arr[8],
            q10 = score_arr[9],
            q11 = score_arr[10],
            q12 = score_arr[11],
            q13 = score_arr[12],
            q14 = score_arr[13],
            q15 = score_arr[14],
            q16 = score_arr[15],
            q17 = score_arr[16],
            q18 = score_arr[17],
            tip = tip,
            side = side
        )
        evaluation.save()
        # 求平均值
        total_score = 0.0
        for score in score_arr:
            total_score = total_score + score
        average_score = total_score/18.0
        if side == 0:
            # 医院
            carer.hospital_score =\
            (carer.hospital_score*carer.hospital_num+average_score)\
            /(carer.hospital_num+1)
            carer.hospital_num = carer.hospital_num + 1
        elif side == 1:
            # 病人
            carer.patient_score =\
            (carer.patient_score*carer.patient_num+average_score)\
            /(carer.patient_num+1)
            carer.patient_num = carer.patient_num + 1
        elif side == 2:
            # 家属
            carer.family_score =\
            (carer.family_score*carer.family_num+average_score)\
            /(carer.family_num+1)
            carer.family_num = carer.family_num + 1
        carer.total_score = \
        0.5*carer.patient_score+0.25*carer.family_score+0.25*carer.hospital_score
        carer.save()
        return Response({'detail': '评价成功'})

class SuggestionView(APIView):
    def post(self, request):
        token = request.data.get('token')
        msg = request.data.get('msg')
        if not (token and msg):
            return Response({"detail":"token,msg required"}, 404)
        user = token2user(token)
        suggestion = Suggestion(user = user, msg = msg)
        suggestion.save()
        return Response({"code":0, "detail":"反馈成功"})
