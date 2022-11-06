
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomProfileManager(BaseUserManager):

    def create_user(self, login, email, password, **other_fields):

        if not login:
            raise ValueError('Login must be set')

        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(login=login, email=email, user_name=login,
                          **other_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(login, email, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField('Логин', unique=True, max_length=255)
    email = models.EmailField('Email', unique=True)
    user_name = models.CharField('Username', unique=True, max_length=255, blank=True)
    first_name = models.CharField('Имя', max_length=255, blank=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    avatar = models.ImageField('Аватарка', upload_to='media/', blank=True, null=True,
                               default='media/userdefault.png')
    status = models.CharField('Статус', max_length=255, blank=True)
    country = models.CharField('Страна', max_length=100, blank=True)
    city = models.CharField('Город', max_length=100, blank=True)
    birth = models.DateField('День рождения', auto_now=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomProfileManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'


class Followers(models.Model):
    user = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Подписчики'
        verbose_name = 'Подписчик'

    # def __str__(self):
    #     return self.user
