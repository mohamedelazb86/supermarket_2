import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from faker import Faker
from blog.models import Post,Category
from django.contrib.auth.models import User
from product.models import Brand,Product


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
def seed_brand(n):
    fake=Faker()
    images=('1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg')
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_brand/{images[random.randint(0,8)]}'
        )

def seed_product(n):
    fake=Faker()
    flag_type=['New','Sale','Feature']
    images=('1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg')
    brands=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag_type[random.randint(0,2)],
            price=round(random.uniform(5.55,99.99),2),
            image=f'photo_product/{images[random.randint(0,8)]}',
            sku=random.randint(1000,100000000),
            subtitle=fake.text(max_nb_chars=1000),
            descriptions=fake.text(max_nb_chars=15000),
            brand=brands[random.randint(0,len(brands)-1)],
            quantity=random.randint(10,150)


        )

# seed_category(50)

# seed_post(200)
# seed_brand(150)
seed_product(1200)




