from django.shortcuts import render
from . models import Author, Category, Journal
from django.db.models import Q


def is_valid_query(param):
    return param != '' and param is not None


def bootstrap_form_filter(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()

    # title and author
    title_contains_query = request.GET.get('title_contains')
    id_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')

    # views
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')

    # published_date
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    # category
    category = request.GET.get('category')

    # reviewed and not reviewed
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')


    # title and author
    if is_valid_query(title_contains_query):
        qs = qs.filter(title__contains=title_contains_query)

    elif is_valid_query(id_query):
        qs = qs.filter(id=id_query)

    elif is_valid_query(title_or_author_query):
        qs = qs.filter(
            Q(title__icontains=title_or_author_query) | Q(author__name__icontains=title_or_author_query)
        ).distinct()

    # views
    if is_valid_query(view_count_min):
        qs = qs.filter(views__gte=view_count_min) # gte stands for "greater than or equal to" if we type 90 it is only gets journals with the minimum views of 95 (95 is included)

    if is_valid_query(view_count_max):
        qs = qs.filter(views__lt=view_count_max)  # lt stands for "less than" if we type 90 it gets all journals with the views less that 90 (90 is not included)

    # published_date
    if is_valid_query(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_query(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_query(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)

    elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        'categories': categories,
    }

    return render(request, 'core/bootstrap_form.html', context=context)
