import re

from django.db import models

MAX_NAME_LENGTH = 255

class NamedSetlistObject(models.Model):

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name

class Artist(NamedSetlistObject):

    # data
    name = models.CharField(max_length=MAX_NAME_LENGTH, blank=False, null=False, unique=True)

class Song(NamedSetlistObject):

    class Meta:
        ordering        = ('artist__name', )
        unique_together = ('name', 'artist')

    # data
    name   = models.CharField(max_length=MAX_NAME_LENGTH, blank=False, null=False, unique=False)
    played = models.BooleanField(default=False, unique=False)

    # relationships
    artist = models.ForeignKey(Artist, related_name='songs', blank=False, null=True, unique=False)

    def has_youtube(self):
        return self.has_link('YouTube')

    def has_lyrics(self):
        return self.has_link('Lyrics')

    def has_tab(self):
        return self.has_link('Guitar Tab')

    def sheet_links(self):
        return self.links.exclude(name='Lyrics').exclude(name='YouTube')

    def has_link(self, name):
        return self.links.filter(name=name).exists()

class Link(NamedSetlistObject):

    class Meta:
        unique_together = ('song', 'url')
        ordering        = ('name', )

    # data
    name = models.CharField(max_length=MAX_NAME_LENGTH, blank=False, null=False, unique=False)
    url  = models.URLField(blank=False, null=False, unique=False)

    # relationships
    song = models.ForeignKey(Song, related_name='links', blank=False, null=True, unique=False)

    def youtube_id(self):
        return re.match(r'.*v=(.*)', self.url).group(1)

    def __unicode__(self):
        return '{my.name} for {my.song} - {my.url}'.format(my=self)
