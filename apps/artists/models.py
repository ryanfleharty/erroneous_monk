# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ArtistManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("Name is too short!")
        return errors

class Artist(models.Model):
    name = models.CharField(max_length=255)


class AlbumManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['title']) < 2:
            errors.append("Title is too short")
        return errors

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name="albums")
    year = models.IntegerField()

    objects = AlbumManager()