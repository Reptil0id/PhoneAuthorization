from django.urls import path
from users.views import (PhoneNumberAuthorizationView, ReferralCreateAPIView, 
                         ReferralCodePatch, ReferralCodeList)

urlpatterns = [
    path('phone/authentication', PhoneNumberAuthorizationView.as_view(),
          name='phone-authentication'),
    path('referral/create', ReferralCreateAPIView.as_view(), name='referral-create'),
    path('referral/patch/<str:PhoneNumber>/', ReferralCodePatch.as_view(), name='referral-patch'),
    path('referral/list/<str:PhoneNumber>/', ReferralCodeList.as_view(), name='referral-list'),
]