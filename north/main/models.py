from django.db import models


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

    def __str__(self) -> str:
        return self.weight


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

    class Meta:
        verbose_name = "Табак"
        verbose_name_plural = "Табаки"
        ordering = ("name",)

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

