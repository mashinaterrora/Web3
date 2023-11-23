from django.shortcuts import render
from entry.models import Entry
from rest_framework.decorators import api_view
import qrcode
from pathlib import Path

def index(request):
    printData()
    return render(request, 'frontend/index.html')
    
@api_view(['GET', 'POST', ])
def qrpage(request):
    if logIn(request.POST['login'], request.POST['password']) is not None:
        entry = Entry.objects.all()
        for j,i in enumerate(entry):
            arr = i.toArray()
            if request.POST['login'] in arr[0:2] and arr[2] == request.POST['password']:
                make_qr(j,abs(hash(arr[0])))
                break
        return render(request, 'frontend/qrpage.html',{"login":request.POST['login'],"otp":logIn(request.POST['login'], request.POST['password'])})
    return index(request)

def regpage(request):
    return render(request, 'frontend/reg.html')

#####
def logIn(login, password):
    entry = Entry.objects.all()
    for i in entry:
        arr = i.toArray()
        if login in arr[0:2] and arr[2] == password:
            return arr[5]
    return None

#self.login, self.email, self.password, self.creation_date, self.id, self.otp
def printData(): #debug function
    entry = Entry.objects.all()
    a = open('test.txt', mode = 'w')
    for i in entry:
        a.write(" ".join(list(map(str, i.toArray()))))
        a.write('\n')
    a.close()

def make_qr(testid,testopt):
    link=f"https://everspace.app/deeplink?type=auth&id={testid}&otp={testopt}&callbackUrl=      &warningText=Attention"
    img=qrcode.make(link)
    img.save(str(Path(__file__).resolve().parent.parent)+"\\static\\qr.png")

@api_view(['GET', 'POST', ])
def regcon(request):
    if "" in request.POST.values():
        return render(request, 'frontend/reg.html')
    else:
        for i in request.POST.values():
            if len(list(filter(lambda k: k in "@." or k.isalnum(), i))) != len(i):
                return render(request, 'frontend/reg.html')

    emailToCheck = request.POST['email']
    entry = Entry.objects.all()
    for i in entry:
        arr = i.toArray()
        if request.POST['login'] in arr[0:2]:
            return render(request, 'frontend/reg.html')
    
    element = Entry(login = request.POST['login'], email = request.POST['email'], password = request.POST['password'], id = str(len(entry)),otp="отсутствует")
    element.save()
    make_qr(len(entry),abs(hash(request.POST['login'])))
    return render(request, 'frontend/qrpage.html', {"login":request.POST['login'],"otp":"отсутствует"})

