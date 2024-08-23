from django.shortcuts import render, redirect
from .models import Villa, Category, Lead
from .forms import VillaCreateForm, VillaUpdateForm

def index_view(request):

    villa = Villa.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        lead = Lead(
            full_name=name,
            email=email,
            subject=subject,
            message=message
        )
        lead.save()

    return render(request,'app/index.html', context={'villas': villa})

def villa_detail(request, pk):
    villa = Villa.objects.get(id=pk)

    if request.method == 'POST':
        form = VillaUpdateForm(request.POST, request.FILES, instance=villa)

        if form.is_valid():
            form.save()
    form = VillaUpdateForm(instance=villa)

    return render(request, 'app/villa_detail.html', context={'villa': villa, 'form': form})
def villa_create(request):
    if request.method == 'POST':
        address = request.POST['address']
        category_title = request.POST['category']
        description = request.POST['description']
        logo = request.FILES['logo']
        price = request.POST['price']
        bedroom = request.POST['bedroom']
        bathroom = request.POST['bathroom']
        floor = request.POST['floor']
        area = request.POST['area']
        parking = request.POST['parking']
        room_count = request.POST['room_count']

        category = Category.objects.get(title=category_title)

        villa = Villa(
            address=address,
            category=category,
            logo=logo,
            price=price,
            description=description,
            bedroom=bedroom,
            bathroom=bathroom,
            area=area,
            parking=parking,
            floor=floor,
            room_count=room_count
        )
        villa.save()
        return redirect('index')

    print(request.POST)
    categories = Category.objects.all()

    return render(request, 'app/villa_create.html', {'categories': categories})

def villa_create2(request):
    if request.method == 'POST':
        form = VillaCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = VillaCreateForm()

    return render(request, 'app/villa_create2.html', context={'form': form})

def villa_delete(request, pk):
    villa = Villa.objects.get(id=pk)
    villa.delete()

    return redirect('index')

