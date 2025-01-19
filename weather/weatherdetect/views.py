from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponse
# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            city=request.POST['city']
            url='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b484dd85ecb525b4fc568cc7e5b0ad6a'
            res=urllib.request.urlopen(url).read()
            jsondata=json.loads(res)
            data={
                'countrycode':str(jsondata['sys']['country']),
                'temp':str(jsondata['main']['temp']),
                'pressure':str(jsondata['main']['pressure']),
                "humidity":str(jsondata['main']["humidity"])
    }
        else:
            city=''
            data={}
        return render(request,'index.html',{'city':city,'data':data})
    except Exception:
        return render(request,'home.html')


