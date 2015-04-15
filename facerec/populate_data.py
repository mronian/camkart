import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facerec.settings')

import django
django.setup()

from jobs.models import Camera


def populate():

def add_cam(link, color, url, pri, tit, nr, nrat, avg, ctype, senti, stype):
    j=Camera.objects.get_or_create(link=link, color=color, img_url=url, price=pri, title=tit, number_of_reviews=nr, number_of_ratings=nrat, avg_rating=avg, cameratype=ctype, sentiment_score=senti, sensor_type=stype)[0]
    return j
# Start execution here!
if __name__ == '__main__':
    print "Starting Our population script..."
    populate()