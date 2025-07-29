from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service
from .request_service import RequestService
from .forms import RequestServiceForm

def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.service = service
            service_request.save()
            return redirect('services:my_requests')
    else:
        form = RequestServiceForm()
    return render(request, 'services/request_service.html', {
        'form': form,
        'service': service
    })

@login_required
def my_requests(request):
    requests = RequestService.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'services/my_requests.html', {'requests': requests})
