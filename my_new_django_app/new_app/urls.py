from django.urls import path
from new_app import views

urlpatterns = [
    # path('posts/2003/', views.special_case_2003),
    # path('posts/<int:year>/', views.year_archive),
    # path('posts/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('file_saver/', views.file_saver),
    path('get_sc_pt/', views.get_sc_pt),
    path('get_username/', views.get_username),
    path('content/', views.content),
    path('ny_days/', views.ny_days),
    path('random/', views.random_numb),
    path('date/', views.date_time),
    path('', views.my_first_view),
    path('my-cat/', views.cat_image_view),
    path('json-response/', views.json_view),
    path('streaming-response/', views.streaming_view),
    path('name_age/', views.name_age),
    path('current_time/', views.current_time),
    path('posts/<int:blog_post_id>/', views.blog_post_view),
    path('add-blog-post/', views.add_blog_post),
    path('recent/', views.recent_blog_post)
]