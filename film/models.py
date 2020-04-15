from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
RESOLUTION = (
    ("720p", "720p"),
    ("1080p", "1080p"),
    ("4k", "4K")
)
GENRES= (
    ("Akcja", "Akcja"),
    ("Komedia", "Komedia"),
    ("Dramat", "Dramat"),
    ("Fantasy", "Fantasy"),
    ("Horro", "Horror"),
    ("Katastroficzny", "Katastroficzny"),
    ("Przygodowy", "Przygodowy"),
    ("Thriller", "Thriller"),
    ("Western,", "Western"),
    ("Wojenny", "Wojenny")   

)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    thumb = models.ImageField(default='default.png', blank=True)
    link = models.CharField(max_length=300, default='dash video link')
    content = models.TextField()
    resolution = models.CharField(max_length=32,choices=RESOLUTION, default="720p")
    genres = models.CharField(max_length=32,choices=GENRES, default="Akcja")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title