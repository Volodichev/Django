from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils import timezone
from django.urls import reverse


class Category(MPTTModel):
    """Модель категорий блога"""
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)
    description = models.TextField(verbose_name="Описание", max_length=1000, default="", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField(verbose_name="Шаблон", max_length=500, default="blog/post_list.html")
    published = models.BooleanField(verbose_name="Отображение", default=True)
    paginated = models.PositiveIntegerField(verbose_name="Новостей на странице", default=5)
    sort = models.PositiveIntegerField(verbose_name="Порядок", default=0)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ('sort',)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Модель тегов блога"""
    name = models.CharField(verbose_name="Тег", max_length=100)
    slug = models.SlugField(verbose_name="url", max_length=100)
    published = models.BooleanField(verbose_name="Отображение", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель постов блога"""
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(verbose_name="Заголовок", max_length=500)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=500, blank=True, null=True)
    mini_text = models.TextField(verbose_name="mini_text", max_length=5000)
    text = models.TextField(verbose_name="text", max_length=1000000)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField(verbose_name="Фото", upload_to="post/", null=True, blank=True)

    slug = models.SlugField(verbose_name="url", max_length=100)
    tags = models.ManyToManyField(to=Tag, verbose_name="Теги", blank=True, related_name="tag")
    category = models.ForeignKey(
        to=Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True
    )
    template = models.CharField(verbose_name="Шаблон", max_length=500, default="blog/post_detail.html")
    published = models.BooleanField(verbose_name="Отображение", default=True)
    viewed = models.PositiveIntegerField(verbose_name="Просмотров", default=0)
    status = models.BooleanField(verbose_name="Для зарегистрированных", default=False)
    sort = models.PositiveIntegerField(verbose_name="Порядок", default=0)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

    def get_tags(self):
        return self.tags.all()

    def get_comments_count(self):
        return self.comments.count()

    def get_category_template(self):
        return self.category.template

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["sort", "-published_date"]



class Comment(models.Model):
    """Модель комментариев блога"""
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    post = models.ForeignKey(
        to=Post,
        verbose_name="Статья",
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField(verbose_name="Комментарий")
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


