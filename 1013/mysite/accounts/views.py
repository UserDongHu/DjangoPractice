from django.conf import settings
from django.contrib.auth.decorators import login_required # 로그인된 사용자에 의해서만 접근되도록 제한하는 데코레이터 import
from django.contrib.auth.views import LoginView, LogoutView # auto 앱의 기능 사용
from django.shortcuts import render
from django.views.generic import CreateView # 장고에서 제공하는 제네릭 뷰. 미리 정의된 뷰 패턴을 제공
from .forms import CreateUserForm # forms.py 에서 내가 새로 만든 form 을 import
# from django.contrib.auth.forms import UserCreationForm # 기본으로 제공되는 modelform에서 수정하지않고 쓰려면 forms.py없이 바로 이렇게 씀

# def signup(request):
#     pass

signup = CreateView.as_view( # 회원가입
    form_class = CreateUserForm, # forms.py 에서 만든 model을 사용
    # form_class = UserCreationForm # 장고에서 제공하는 UserCreationForm사용
    template_name = 'accounts/form.html', # 랜더링할 템플릿의 경로 지정
    success_url = settings.LOGIN_URL, # 객체가 성공적으로 생성된 후 이동할 URL
)

# def login(request):
#     pass

login = LoginView.as_view( # 로그인
    template_name = 'accounts/form.html',
    # next_page = settings.LOGIN_URL,
)

# def logout(request):
#     pass

logout = LogoutView.as_view( # 로그아웃
    next_page = settings.LOGOUT_URL, # 로그아웃에 성공한후 다음으로 이동시킬 URL
)

# 로그인된 사용자에 의해서만 접근되도록 제한하는 데코레이터
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')