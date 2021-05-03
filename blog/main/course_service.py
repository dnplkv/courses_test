from .models import Course


def course_all():
    return Course.objects.all()


def course_find(course_id: int) -> Course:
    return Course.objects.get(id=course_id)
