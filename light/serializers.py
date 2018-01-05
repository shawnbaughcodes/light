from django.core.serializers.json import DjangoJSONEncoder
from .models import *

class ReviewsEncoder(DjangoJSONEncoder):
    def default(self, obj):
        
