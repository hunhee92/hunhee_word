from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('nickname', 'image', 'email')
        help_texts = {
            'username': _('숫자,문자,@/./+/-/_ 만 가넝.'),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # 각 필드의 레이블 변경
        self.fields['username'].label = '아이디'
        self.fields['nickname'].label = '닉네임'
        self.fields['image'].label = '이미지'
        self.fields['password1'].label = '패스워드'
        self.fields['password2'].label = '패스워드 확인'
        self.fields['email'].label = '이메일'

        # 각 필드의 도움말 텍스트 변경
        self.fields['password1'].help_text = '8자 이상 문자 포함'
        self.fields['password2'].help_text = '이전과 동일한 비밀번호를 입력하세요'
