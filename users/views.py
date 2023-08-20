from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from .serializers import ReferralCreateSerializer, GetPhoneNumberSerializer, ReferralSerializer
from .charts.key_generator import referral_key_generator, phone_key_generator
from .models import ReferralModel

# Create your views here.
def authentication_view(request):
    return render(request, 'authentication/authentication.html')

def profile_view(request):
    PhoneNumber = request.GET.get('PhoneNumber', '')
    return render(request, 'profile/profile.html', {'PhoneNumber': PhoneNumber})


class PhoneNumberAuthorizationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GetPhoneNumberSerializer(data=request.data)

        if serializer.is_valid():
            generated_number = phone_key_generator(4)
            return Response({'GeneratedNumber': generated_number}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReferralCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReferralCreateSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.validated_data['Code'] = referral_key_generator(6)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response('Номер уже зарегистрирован', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReferralCodePatch(APIView):
    def patch(self, request, *args, **kwargs):
        PhoneNumber = kwargs.get('PhoneNumber') 
        ReferralCode = request.data.get('ReferralCode')
        referral = ReferralModel.objects.all()
        
        try:
            referral_user= referral.get(PhoneNumber=PhoneNumber)
            print(PhoneNumber)
            print(referral_user.PhoneNumber)
            try:
                referral.get(Code=ReferralCode)

                if not referral_user.ReferralCode:
                    referral_user.ReferralCode = ReferralCode
                    referral_user.save()
                else:
                    return Response({'error': 'Реферальный код уже был добавлен'},
                                     status=status.HTTP_400_BAD_REQUEST)
            except ReferralModel.DoesNotExist:
                return Response({'error': 'Реферальный код не существует'},
                                 status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': 'Код успешно добавлен'},status=status.HTTP_200_OK)
        except ReferralModel.DoesNotExist:
            return Response({'error': 'Номер телефона не найден'},status=status.HTTP_404_NOT_FOUND)
        
class ReferralCodeList(APIView):
    def get(self, request, PhoneNumber, *args, **kwargs):
        try:
            user = ReferralModel.objects.get(PhoneNumber=PhoneNumber)
            referrals = ReferralModel.objects.filter(ReferralCode=user.Code)
            serializer = ReferralSerializer(referrals, many=True)
            return Response(serializer.data)
        except ReferralModel.DoesNotExist:
            return Response({'error': 'Пользователь не найден'},status=status.HTTP_404_NOT_FOUND)

        
        