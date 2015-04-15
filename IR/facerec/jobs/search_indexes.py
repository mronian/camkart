import datetime
from haystack import indexes
from .models import Camera

class CamIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
                             
    def get_model(self):
        return Camera
    
    def index_queryset(self):
        return self.get_model().objects.all()