from django.db import models
from ckeditor.fields import RichTextField


class BotUser(models.Model):
    class Lang(models.TextChoices):
        UZ = 'uz'
        RU = 'ru'
        EN = 'en'

    class State(models.IntegerChoices):
        NOTHING = 0

    chat_id = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    bot_state = models.IntegerField(default=State.NOTHING)
    lang = models.CharField(max_length=2, default=Lang.UZ)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name or ''])

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class MessageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Template.Type.MESSAGE)


class KeyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Template.Type.KEY)


class SmileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=Template.Type.SMILE)


class Template(models.Model):
    class Type(models.IntegerChoices):
        MESSAGE = 1
        KEY = 2
        SMILE = 3

    templates = models.Manager()
    messages = MessageManager()
    keys = KeyManager()
    smiles = SmileManager()

    type = models.IntegerField(choices=Type.choices)
    title = models.CharField(max_length=255)
    body_uz = RichTextField()
    body_ru = RichTextField()
    body_en = RichTextField()

    def gettext(self, lang):
        return getattr(self, f'body_{lang}')

    def getall(self):
        return (self.body_uz, self.body_ru, self.body_en)

    def __str__(self):
        return self.body_uz
