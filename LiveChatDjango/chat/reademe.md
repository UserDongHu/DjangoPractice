# 구현 방향

1. 채팅방 별로 다른 채널레이어 그룹에 추가
- 웹소켓 요청 url에 채팅방 이름 포함, 이를 그룹명으로 활용
- ex) URL /ws/chat/**django**/chat/ -> 그룹명 "chat-django"

2. 채널레이어 그룹명 네이밍 규칙에 맞게, 그룹명 지정하기
-그룹명 문자열에는 한글 불가

3. Room 모델을 활용한 채팅방 목록 관리