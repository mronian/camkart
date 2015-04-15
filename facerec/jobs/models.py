from django.db import models

class Camera(models.Model):
    # id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=512)
    color = models.CharField(max_length=64, blank=True)
    img_url = models.CharField(max_length=128, blank=True)
    price = models.IntegerField(blank=True)
    title = models.CharField(max_length=128, blank=True)
    number_of_reviews = models.IntegerField(blank=True)
    number_of_ratings = models.IntegerField(blank=True)
    avg_rating = models.FloatField(blank=True)
    cameratype = models.CharField(max_length=64, blank=True)
    sentiment_score = models.FloatField(blank=True)
    sensor_type = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.link