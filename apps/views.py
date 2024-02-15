from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.models import Project
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
from .models import Project
class ProjectTemplateView(ListView):
    template_name = 'index.html'
    queryset = Project.objects.order_by('-id')
    context_object_name = 'projects'


def delete_project(request, pk):
    Project.objects.filter(id=pk).delete()
    return redirect('project-list')





def project_list(request):
    users = Project.objects.all()

    # Paginate the user list
    paginator = Paginator(users, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


