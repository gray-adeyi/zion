
from django.urls import path

app_name = 'core'

from .views import (
    Index,
    AboutUs,
    FAQView,
    PrayerRequestView,
    PrayerRequestList,
)

from .apiviews import (
    WebsiteInfo
)

urlpatterns = [
    path(
        '', 
        Index.as_view(), 
        name='index'),
    path(
        'about/',
        AboutUs.as_view(),
        name='about_us'
    ),
    path(
        'faq/', 
        FAQView.as_view(), 
        name = 'faq'),
    path(
        'prayer-request/',
        PrayerRequestView.as_view(),
        name= 'prayer_request'),
    path(
        'prayer-request/all/',
        PrayerRequestList.as_view(),
        name='prayer_request_list'
    ),
]

apiurlpatterns = [
    path(
        'api/websiteinfo/', 
        WebsiteInfo.as_view(), 
        name='website_info'),
]

urlpatterns += apiurlpatterns
