from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url='tube/'), name='root'), # 이렇게도 가능
    path('', RedirectView.as_view(pattern_name='tube:post_list'), name='root'), # ''주소일때, tube앱의 post_list url로 가겠다.
    path('admin/', admin.site.urls),
    path('tube/', include('tube.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 미디어 url 추가