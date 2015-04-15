import datetime
from haystack import indexes
from .models import Camera

class CamIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    price=indexes.IntegerField(model_attr='price', faceted=True)
    avgrating=indexes.FloatField(model_attr='avg_rating', faceted=True)
    numrat=indexes.IntegerField(model_attr='number_of_ratings', faceted=True)
    sentiscore=indexes.FloatField(model_attr='sentiment_score', faceted=True)


    def get_model(self):
        return Camera
    
    def index_queryset(self):
        return self.get_model().objects.all()