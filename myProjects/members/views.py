from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Members


# Create your views here.
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

# def index(request):
#   myMembers = Members.objects.all().values()
#   output = ""
#   for x in myMembers:
#     output += " ---- " + x["firstname"]
#   return HttpResponse(output)

def index(request):
    myMembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myMembers': myMembers,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))


def store(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def edit(request, id):
    myMember = Members.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        'myMember': myMember,
    }
    return HttpResponse(template.render(context, request))


def update(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))


def test(request):
    template = loader.get_template('test/variable.html')
    members = Members.objects.all().values()
    context = {
        'firstname': 'Duc Dv',
        'members': members,
        'greeting': 1,
        'x': '',
        'y': 'Ford',
        'z': 'BMW',
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Sierra',
                'year': '1981',
            },
            {
                'brand': 'Volvo',
                'model': 'XC90',
                'year': '2016',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }]
    }
    return HttpResponse(template.render(context, request))
