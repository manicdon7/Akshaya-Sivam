from django.shortcuts import render
from .models import UserInput

# Create your views here.
def home(request):
    items = UserInput.objects.all()
    return render(request,'index.html',{'items': items})
def base(request):
    items = UserInput.objects.all()
    return render(request,'base.html',{'items': items})
def aboutus(request):
    return render(request,'aboutus.html')
def aboutus1(request): 
    return render(request, 'aboutus1.html')
def aboutus2(request):
    return render(request, 'aboutus2.html')
def aboutus3(request):
    return render(request, 'aboutus3.html')
def aboutus4(request):
    return render(request, 'aboutus4.html')
def our_services(request):
    return render(request,'Our_Services.html')
def card(request):
    return render(request,'card.html')
def contactus(request):
    return render(request,'contactus.html')
def faq(request):
    return render(request,'FAQ.html')
def login(request):
    return render(request,'login.html')
def causes(request):
    items = UserInput.objects.all()
    return render ( request , "causes.html",{'items': items})
def Getinvolved(request):
    return render(request,'Get_invloved.html')  
def volunteer(request):
    return render(request,'get1.html')
def support(request):
    return render(request,'support.html')  
def foster(request):
    return render(request,'foster.html')
def impact(request):
    return render(request,'impact.html') 
def Donate(request):
    return render(request,'Donate.html')
def exception(request, exception):
    return render(request, '404.html')
def save_input(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal = request.POST.get('goal')

        UserInput.objects.create(
            image=image,
            name=name,
            title=title,
            description=description,
            goal=goal
        )

        return redirect('input_form')

    return render(request, 'test.html')