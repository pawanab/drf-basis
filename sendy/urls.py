from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendy.views import SnippetList, SnippetDetail, UserList, UserDetail, api_root, SinppetHighlight


urlpatterns = [
    path('', api_root),
    path('snippet', SnippetList.as_view(),name='snippet-list'),
    path('snippet/<int:pk>/highlight', SinppetHighlight.as_view(),name='snippet-highlight'),
    path('snippet/<int:pk>', SnippetDetail.as_view(),name='snippet-detail'),
    path('user/', UserList.as_view(),name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(),name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)