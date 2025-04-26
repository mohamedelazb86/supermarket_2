import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from faker import Faker
from blog.models import Post,Category
from django.contrib.auth.models import User


def seed_category(n):
    fake=Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.name()
        )

def seed_post(n):
    fake=Faker()
    category=Category.objects.all()
    images=('1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg')
    user=User.objects.all()

    for _ in range(n):
        Post.objects.create(
            title=fake.name(),
            content=fake.text(max_nb_chars=2000),
            category=category[random.randint(0,len(category)-1)],
            image=f'photo_post/{images[random.randint(0,8)]}',
            user=user[random.randint(0,len(user)-1)]


        )
# seed_category(50)

seed_post(200)


