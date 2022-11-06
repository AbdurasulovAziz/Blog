from django.urls import path
from blog import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('article/<int:pk>', views.ArticleDetail.as_view()),
    path('search/<str:name>', views.ArticleOrProfileSearch.as_view()),
    path('myarticles/', views.MyArticleList.as_view()),
    path('subarticles/', views.SubArticleList.as_view()),

]