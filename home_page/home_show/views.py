from django.shortcuts import render
from home_show.models import Person
from django.http import HttpResponse
import json

def home(request):
    #list = Person.objects.all()
    q = Person.objects.filter(name='online')
    #print (list[1].number)
    #print (q[0].number)
    print (q,len(q))
    if len(q)!=0:  #query success.
      context = {'number':q[0].number}
    else:  #result queried is null.
      context = {'number':'result queried is null, maybe table no item.',}
    return render(request, 'home.html', context)

def query(request):
    q_online = Person.objects.filter(name='online')
    print (q_online,len(q_online))
    if len(q_online)!=0:  #query success.
      data_online = q_online[0].number
    else:  #result queried is null.
      data_online = 'result queried is null, maybe table no item.'

    q_sent = Person.objects.filter(name='sent')
    print (q_sent,len(q_sent))
    if len(q_sent)!=0:  #query success.
      data_sent = q_sent[0].number
    else:  #result queried is null.
      data_sent = 'result queried is null, maybe table no item.'

    q_read = Person.objects.filter(name='read')
    print (q_read,len(q_read))
    if len(q_read)!=0:  #query success.
      data_read = q_read[0].number
    else:  #result queried is null.
      data_read = 'result queried is null, maybe table no item.'
    '''
    result_queried = str(data_online)+':' +str(data_sent)+ ':' +str(data_read)
    return HttpResponse(result_queried)
    '''
    result_queried = {'online':data_online,'sent':data_sent,'read':data_read}
    encodedjson = json.dumps(result_queried, sort_keys=True, indent=4) #transform string into object:encodedjson.
    print (repr(result_queried))
    print (encodedjson)

    return HttpResponse(encodedjson)
   

# Create your views here.
