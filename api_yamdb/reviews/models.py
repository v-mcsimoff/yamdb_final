from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()
# from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='name'
    )
    year = models.IntegerField(
        verbose_name='Release year',
    )
    description = models.TextField(
        verbose_name='Description'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genre',
        related_name='titles',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Work',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Text',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Score',
        validators=[
            MinValueValidator(1, 'Enter an integer from 1 to 10'),
            MaxValueValidator(10, 'Enter an integer from 1 to 10')
        ],
    )
    pub_date = models.DateTimeField(
        verbose_name='Publication date',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Review',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Text',
    )
    author = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Publication date',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
