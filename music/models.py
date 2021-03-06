from django.db import models

# Create your models here.


# Red pk 1
class Database(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title+'-'+self.artist


class Song(models.Model):
    album = models.ForeignKey(Database, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)


