from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm  # ✅ Make sure this import is included


def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    form = ChaiVarityForm()  # ✅ Always initialize the form
    stores = []  # ✅ Default to empty list

    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varities=chai_varity)

    return render(request, 'chai/chai_stores.html', {
        'stores': stores,
        'form': form
    })
