from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token # 토큰 모델 Token.objects.get()이런식으로 토큰 확인 가능
from rest_framework.validators import UniqueValidator # 중복 검사(회원 가입할 때 동일한 아이디가 있는지 검사 등)
from django.contrib.auth.password_validation import validate_password # 비밀번호 유효성 검사
from django.contrib.auth.models import User # User 모델(기본 User모델 사용시 사용자명, 비밀번호, 이메일 필드만 사용 가능 => 상속받아 커스터마이징 가능)
from django.contrib.auth import authenticate

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())] # 중복 검사
    )
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())] # 중복 검사
    )
    password = serializers.CharField(
        write_only = True, # 쓰기 전용
        required = True, 
        validators = [validate_password] # 비밀번호 유효성 검사
    )
    password2 = serializers.CharField( # 비밀번호 확인 필드
        write_only = True, 
        required = True
    )
    
    class Meta:
        model = User
        fields = '__all__'
        
    def validate(self, attrs): # 직렬화되기전 데이터 검사. attrs : Serializer에 제출된 데이터
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        return attrs
    
    def create(self, validated_data): # 직렬화된 데이터를 기반으로 새로운 객체를 생성. validated_data : 유효성 검사를 마친 데이터
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시 아이디와 비밀번호만 필요

    def validate(self, data):
        user = authenticate(**data) # 직렬화되기전 data로 사용자를 인증햇 인증에 성공한경우 사용자 객체를 반환.
        if user: # 사용자 인증이 됐으면 사용자 토큰 반환
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError("유효하지 않은 로그인입니다.")