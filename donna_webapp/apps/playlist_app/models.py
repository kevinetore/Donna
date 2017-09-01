from django.db import models

class Playlist(models.Model):
    playlist_id = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
