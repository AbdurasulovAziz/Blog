from rest_framework.response import Response
from rest_framework.views import APIView
from account.permissions import AuthorOrReadOnly
from account.models import Followers, CustomUser
from account.serializers import UserSerializer
from blog.models import Article
from blog.serializers import ArticleSerializer
from rest_framework import generics


class ArticleList(generics.ListAPIView):
    """Получение всех статей в базе"""

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetail(generics.RetrieveAPIView):

    """Получение статьи по ее идентификатору"""

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class MyArticleList(generics.ListCreateAPIView):

    """Получение/Создание личных статей"""

    permission_classes = [AuthorOrReadOnly]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        current_user = self.request.user.id
        return Article.objects.filter(author_id=current_user).order_by('-data')


class SubArticleList(generics.ListAPIView):

    """Получение статей подписок
    (Тех на кого подписан пользователь)"""

    serializer_class = ArticleSerializer

    def get_queryset(self):
        current_user = self.request.user.id
        queryset = Article.objects.filter(
            author__user_name__in=Followers.objects.values_list('user__user_name').filter(
                follower=current_user))
        return queryset


class ArticleOrProfileSearch(APIView):
    """Поиск статьи"""

    def get(self, request, *args, **kwargs):
        article = Article.objects.filter(title__regex=kwargs.get('name')).values('id')
        account = CustomUser.objects.filter(user_name__regex=kwargs.get('name')).values('user_name')
        return Response({'articles': article, 'accounts': account})

