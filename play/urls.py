from django.conf.urls import url


from .views import graph, play_count_by_month, get_sample_data

urlpatterns = [
    url(r'^$', graph),
    url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
    url(r'^api/get_sample_data', get_sample_data, name='get_sample_data'),
]
