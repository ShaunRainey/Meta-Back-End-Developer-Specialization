from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    #print(dir(request))
    #print(request)
    #print(request.content_params)
    #print("status code: ", HttpResponse.status_code)
    #print(dir(HttpResponse.content))
    return HttpResponse('<h1>Welcome to Little Lemon Restaurant</h1>')

def testTemplate(request, name): 
    template = loader.get_template('hello.html') 
    context={"name":name, "species": "human"} 
    #print('TEMPLATE TEST', dir(request))
    return render(request, 'hello.html', context)  

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    htmlPage = '''
    <form action="/myapp/getform/" method="POST"> 
    {% csrf_token %} 
    <p>Name: <input type="text" name="id"></p> 
    <p>UserID :<input type="name" name="name"></p> 
    <input type="submit"> 
    </form> 
    '''

    #In the example this should be a render, figure out how to get that to work!
    return HttpResponse(htmlPage)

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def getTemplate(request):
    pass