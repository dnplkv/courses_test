from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .course_service import course_all, course_find
from .forms import CourseForm
from .models import Course


def index(request):
    return render(request, 'main/index.html')


def courses(request):
    courses = course_all()
    return render(request, 'main/courses_all.html', {"title": "Courses", "courses": courses})


def course_create(request):
    err_custom = ""
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_all')
        else:
            err_custom = "Error on save Course"
    else:
        form = CourseForm()
    context = {
        'form': form,
        'err_my': err_custom
    }
    return render(request, 'main/course_create.html', context=context)


def course_delete(request, course_id):
    obj = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        obj.delete()
        return redirect('courses_all')
    context = {
        "course": obj
    }
    return render(request, 'main/delete_course.html', context=context)


def course_update(request, course_id):
    err = ""
    crs = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        form = CourseForm(instance=crs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_all')
        else:
            err = "Error on update Course"
    else:
        form = CourseForm(instance=crs)
    context = {
        'form': form,
        'err_my': err
    }
    return render(request, 'main/course_update.html', context=context)


def courses_show(request, course_id):
    crs = course_find(course_id)
    return render(request, 'main/courses_show.html', {"title": crs.title,
                                                      "crs": crs,
                                                      "description": crs.description,
                                                      "start_date": crs.start_date,
                                                      "finish_date": crs.finish_date,
                                                      "amount": crs.amount})


def search_title(request):

    if request.method == "POST":
        searched = request.POST['searched']
        start_date = request.POST['start_date']
        finish_date = request.POST['finish_date']
        filter_obj = {"title__contains": searched}
        if start_date:
            filter_obj.update({"start_date__gte": start_date})
        if finish_date:
            filter_obj.update({"finish_date__lte": finish_date})
        titles = Course.objects.filter(**filter_obj)
        # titles = Course.objects.filter(title__contains=searched,
        #                                start_date__gte=start_date,
        #                                finish_date__lte=finish_date)
        return render(request, 'main/search_title.html', {'searched': searched,
                                                          'start_date': start_date,
                                                          'finish_date': finish_date,
                                                          'titles': titles})
    else:
        return render(request, 'main/search_title.html', {})


def json_courses(request):
    courses_cont = course_all().values('title', 'description', 'start_date', 'finish_date', 'amount')
    data = list(courses_cont)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_courses_show(request, course_id):
    pst = course_find(course_id)
    dict_obj = model_to_dict(pst)
    return JsonResponse(dict_obj, safe=False)
