from django.urls import path
from thread_app import views


urlpatterns=[
    path('concurrent/',views.Thread_pool.as_view()),
    path('asyncio/',views.Asyncio.as_view()),
   path('multiprocess/',views.Multiprocessing.as_view()),
    path('http/',views.Httpx.as_view()),
    path('aiohttp/',views.Aiohttp.as_view())

]