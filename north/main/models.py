from django.db import models

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


class Line(models.Model):
    slug = models.CharField(
        "Слаг",
        max_length=256,
    )
    title = models.CharField(
        "Тайтл",
        max_length=256
    )
    slug_china = models.CharField(
        "Слаг китайский",
        max_length=256,
    )
    title_china = models.CharField(
        "Тайтл китайский",
        max_length=256
    )
    slug_eng = models.CharField(
        "Слаг английский",
        max_length=256,
    )
    title_eng = models.CharField(
        "Тайтл английский",
        max_length=256
    )
    order = models.IntegerField(
        "Очередь"
    )

    class Meta:
        verbose_name = "Линейка"
        verbose_name_plural = "Линейки"
        ordering = ("order", "title", "slug")

    def __str__(self) -> str:
        return self.title


class TagTabacco(models.Model):
    title = models.CharField(
        "Тайтл",
        max_length=256
    )
    title_eng = models.CharField(
        "Тайтл английский",
        max_length=256
    )
    title_china = models.CharField(
        "Тайтл китайский",
        max_length=256
    )
    color = models.CharField(
        "Цвет",
        max_length=256,
        help_text="Цвет в hex"
    )
    text_color = models.CharField(
        "Цвет текста",
        max_length=256,
        help_text="Цвет в hex"
    )

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title


class WeightTabacco(models.Model):
    weight = models.IntegerField(
        "Вес"
    )

    class Meta:
        verbose_name = "Вес"
        verbose_name_plural = "Веса"
        ordering = ("weight",)

    def __int__(self) -> int:
        return self.weight

    def __str__(self) -> str:
        return str(self.weight)


class Tabacco(models.Model):
    name = models.CharField(
        "Название",
        max_length=256
    )
    name_china = models.CharField(
        "Название китайское",
        max_length=256
    )
    name_eng = models.CharField(
        "Название английский",
        max_length=256
    )
    line = models.ManyToManyField(
        Line
    )
    tag = models.ManyToManyField(
        TagTabacco
    )
    weight = models.ManyToManyField(
        WeightTabacco
    )
    image = models.ImageField(
        "Картинка",
    )
    description = models.TextField(
        "Описание",
        null=True,
        blank=True
    )
    description_china = models.TextField(
        "Описание китайское",
        null=True,
        blank=True
    )
    description_eng = models.TextField(
        "Описание английский",
        null=True,
        blank=True
    )
    order = models.IntegerField(
        "Очередь",
        default=0,
    )

    class Meta:
        verbose_name = "Табак"
        verbose_name_plural = "Табаки"
        ordering = ("order",)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    full_name = models.CharField(
        "ФИО",
        blank=True,
        null=True,
        max_length=255
    )
    company_name = models.CharField(
        "Название компании",
        blank=True,
        null=True,
        max_length=255
    )
    city = models.CharField(
        "Город",
        blank=True,
        null=True,
        max_length=255
    )
    contact = models.CharField(
        "Контакты",
        blank=True,
        null=True,
        max_length=1024
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ("-id",)

    def __str__(self) -> str:
        return str(self.full_name)


class MapCountry(models.Model):
    country = models.CharField(
        "Страна",
        blank=True,
        null=True,
        max_length=255
    )
    country_eng = models.CharField(
        "Страна eng",
        blank=True,
        null=True,
        max_length=255
    )
    country_china = models.CharField(
        "Страна china",
        blank=True,
        null=True,
        max_length=255
    )

    class Meta:
        verbose_name = "Страна точки"
        verbose_name_plural = "Страны точек"
        ordering = ("-id",)

    def __str__(self) -> str:
        return str(self.country)


class MapPoint(models.Model):
    name = models.CharField(
        "Название",
        blank=True,
        null=True,
        max_length=255
    )
    city = models.CharField(
        "Город",
        blank=True,
        null=True,
        max_length=255
    )
    city_eng = models.CharField(
        "Город eng",
        blank=True,
        null=True,
        max_length=255
    )
    city_china = models.CharField(
        "Город china",
        blank=True,
        null=True,
        max_length=255
    )
    address = models.CharField(
        "Адрес",
        blank=True,
        null=True,
        max_length=255
    )
    address_eng = models.CharField(
        "Адрес eng",
        blank=True,
        null=True,
        max_length=255
    )
    address_china = models.CharField(
        "Адрес china",
        blank=True,
        null=True,
        max_length=255
    )
    contact = models.CharField(
        "Контакт",
        blank=True,
        null=True,
        max_length=255
    )
    website = models.CharField(
        "Сайт",
        blank=True,
        null=True,
        max_length=255
    )
    soc_max = models.CharField(
        " MAX",
        blank=True,
        null=True,
        max_length=255
    )
    soc_telegram = models.CharField(
        "Telegram",
        blank=True,
        null=True,
        max_length=255
    )
    soc_vk = models.CharField(
        "VK",
        blank=True,
        null=True,
        max_length=255
    )
    soc_inst = models.CharField(
        "Instagram",
        blank=True,
        null=True,
        max_length=255
    )
    is_active = models.BooleanField(
        verbose_name="Активен?",
        help_text="Активен?",
        blank=True,
        null=True,
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата создания, для служебного пользования.",
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Дата последнего изменения, для служебного пользования.",
        verbose_name="Дата изменения",
    )
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)
        ],
        default=0
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)
        ],
        default=0
    )
    map_info = models.ForeignKey(
        MapCountry,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = "Точка на карте"
        verbose_name_plural = "Точки на карте"
        ordering = ("-id",)

    def __str__(self) -> str:
        return str(self.name)

