from django.shortcuts import render, HttpResponse, redirect
import time,os
# the index function is called when root is visited
os.environ['TZ']='US/Pacific'
time.tzset()
#tzname('EST', 'EDT')
def index(request):
    context={
        'date':time.strftime("%b %d, %Y", time.localtime()),
        'time':time.strftime("%H:%M %p", time.localtime())
    }
    #return HttpResponse(response)
    return render(request,'clock/index.html',context)