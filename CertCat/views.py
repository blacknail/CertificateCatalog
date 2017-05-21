from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from .forms import *
from CertCat.helpers import get_cert_dataOpenSSL, row_to_dict
from CertCat.helpersdb import DataOps as DO
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, "index.html", {'time': now()})


def cert_read(request):
    if request.method == 'POST':
        form = ReadCertForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file'].read()
            j_obj = get_cert_dataOpenSSL(file)
            DO().insert_subject(j_obj)
            return redirect('cert_list')
    else:
        form = ReadCertForm()
    return render(request, 'cert_read.html', {'form': form})


def cert_list(request):
    page = request.GET.get('page', 1)
    cert_list = cert_subj.objects.all()

    paginator = Paginator(cert_list, 5)
    try:
        certs = paginator.page(page)
    except PageNotAnInteger:
        certs = paginator.page(1)
    except EmptyPage:
        certs = paginator.page(paginator.num_pages)

    return render(request, "cert_list.html", {'certs': certs})


def edit_orm(request):
    try:
        cert_id = int(request.GET.get('id'))
    except Exception as ex:
        raise Http404

    certsubj = cert_subj.objects.get(id=cert_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CertSubjORMForm(request.POST, instance=certsubj)
        if form.is_valid():
            form.save()
            return redirect('cert_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CertSubjORMForm(instance=certsubj)

    return render(request, "edit_orm.html", {'form': form, 'cert_id': cert_id})


def edit_raw(request):
    try:
        cert_id = int(request.GET.get('id'))
    except Exception as ex:
        raise Http404

    row = DO().get_subject(cert_id)
    dict = row_to_dict(row)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        res = DO().update_subject(request.POST, cert_id)

        return redirect('cert_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CertSubjRawForm(initial=dict)

    return render(request, "edit_raw.html", {'form': form, 'cert_id': cert_id})
