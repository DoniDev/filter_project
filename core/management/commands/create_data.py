from django.core.management.base import BaseCommand
from core.models import Category, Author, Journal
import random as rd
import datetime as dt




categories = [
    'Sport',
    'Lifestyle',
    'Music',
    'Coding',
    'Travelling'
]

authors = [
    'John', 'Michael', 'Luke', 'Sally', 'Joe', 'Dude', 'Guy', 'Barbara'
]

def generate_author_name():
    index = rd.randint(0, len(authors)-1)

    return authors[index]


def generate_category_name():
    index = rd.randint(0, len(categories) - 1)

    return categories[index]


def generate_views_count():

    return rd.randint(1, 100)


def generate_is_reviewed():
    val = rd.randint(0, 1)
    if val == 0:
        return False
    return True


def generate_publish_data():
    year = rd.randint(2000, 2030)
    month = rd.randint(1, 12)
    day = rd.randint(1, 28)
    return dt.date(year, month, day)



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The txt file that contains the journal titles')


    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_publish_data()
                views = generate_views_count()
                reviewed = generate_is_reviewed()


                author = Author.objects.get_or_create(name=author_name)

                journal = Journal(
                    title=title,
                    author=Author.objects.get(name=author_name),
                    views=views,
                    publish_date=publish_date,
                    reviewed=reviewed,
                )

                journal.save()

                category = Category.objects.get_or_create(name=category_name)

                journal.categories.add(
                    Category.objects.get(name=category_name)
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))






