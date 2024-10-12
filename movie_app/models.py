import uuid
from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(
        verbose_name="Комментарий", null=True, blank=True, default=""
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", auto_now=True, null=True, blank=True
    )

    class Meta:
        abstract = True


class Directory(Base):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=150,
        null=False,
        blank=True,
        default="",
        db_index=True,
    )
    is_group = models.BooleanField(verbose_name="Это группа", default=False)
    is_mark = models.BooleanField(verbose_name="Пометка", default=False)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ("name",)
        abstract = True


class Genre(Directory):
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(Directory):
    description = models.TextField(
        verbose_name="Описание",
        null=False,
        blank=True,
        default="",
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name="Жанр",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="movies",
    )
    cover = models.ImageField(
        verbose_name="Обложка", upload_to="images/", blank=True, null=True
    )
    release = models.IntegerField(verbose_name="Год выпуска", blank=True, default=0)
    rate = models.IntegerField(verbose_name="Рейтинг", blank=True, default=0)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
