from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from jobs.models import Camera
from jobs.forms import CamSearchForm
from haystack.query import SearchQuerySet

def cameras(request):
    form = CamSearchForm(request.GET)
    results = form.search()

    context_dict={}
    filteredResults = []
    if request.GET:
    	priceLow = int(request.GET['varA'].split(',')[0][1:])
    	numratLow = int(request.GET['varC'].split(',')[0][1:])
    	sentiscoreLow = float(request.GET['varD'].split(',')[0][1:])
    	avg_ratingLow = float(request.GET['varB'].split(',')[0][1:])

    	priceHigh= int(request.GET['varA'].split(',')[1][:-1])
    	numratHigh= int(request.GET['varC'].split(',')[1][:-1])
    	sentiscoreHigh= float(request.GET['varD'].split(',')[1][:-1])
    	avg_ratingHigh= float(request.GET['varB'].split(',')[1][:-1])

    	sortType = int(request.GET['varE'])

    	for i in range(len(results)):
    		try:
    			if not ( results[i].price >= priceLow and results[i].price <= priceHigh ):
    				continue
    			if not ( results[i].numrat >= numratLow and results[i].numrat <= numratHigh ):
    				continue
    			if not ( results[i].sentiscore >= sentiscoreLow and results[i].sentiscore <= sentiscoreHigh ):
    				continue
    			if not ( results[i].avgrating >= avg_ratingLow and results[i].avgrating <= avg_ratingHigh ):
   					continue
    			filteredResults.append(results[i])
    		except Exception as e:
    			print str(results[i].numrat) +"LOL"

    	if sortType==1:
    		filteredResults=sorted(filteredResults, key=lambda r:r.price)
    	elif sortType==2:
    		filteredResults=sorted(filteredResults, key=lambda r:-r.price)
    	elif sortType==3:
    		filteredResults=sorted(filteredResults, key=lambda r:r.avgrating)
    	elif sortType==4:
    		filteredResults=sorted(filteredResults, key=lambda r:-r.avgrating)
    	elif sortType==5:
    		filteredResults=sorted(filteredResults, key=lambda r:r.sentiscore)
    	elif sortType==6:
    		filteredResults=sorted(filteredResults, key=lambda r:-r.sentiscore)


    	# print [r.price for r in filteredResults]

    else :
    	filteredResults=results
        priceLow=0
        sentiscoreLow=0.0
        numratLow=0
        avg_ratingLow=0.0
        priceHigh=500000
        numratHigh=1000
        avg_ratingHigh=5.0
        sentiscoreHigh=1.0

    context_dict['results']=filteredResults
    context_dict['pL']=priceLow
    context_dict['pH']=priceHigh
    context_dict['rL']=avg_ratingLow
    context_dict['rH']=avg_ratingHigh
    context_dict['sL']=sentiscoreLow
    context_dict['sH']=sentiscoreHigh
    context_dict['nL']=numratLow
    context_dict['nH']=numratHigh

    return render(request,'base.html', context_dict)

    # Create your views here.
