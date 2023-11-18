from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ProfileView(APIView):
    '''
    인증 받은 유저가 접근이 가능해야 합니다.
    인증 받은 유저가 접근한 경우, "반갑습니다, {유저 이메일} 님!"을 출력해야한다.
    "permission_classes = [IsAuthenticated]"을 통해 인증 유무를 판단한다.
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'test_message': f'반갑습니다, {str(request.user)} 님!',
        }
        print(f'profile {content}')
        return Response(content)