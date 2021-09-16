import datetime
import pytz

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


# TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
# TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)
def set_bd(index):
    TEST_DATE = datetime.datetime(2017+index, 4, 10, 12, 00, tzinfo=pytz.utc)
    TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)

    user = CustomUser(id=110+index,
                      email=f'email{index}@mail.com',
                      password='1234',
                      first_name=f'fname{index}',
                      middle_name=f'mname{index}',
                      last_name=f'lname{index}'
                      )
    user.save()
    user_free = CustomUser(id=220 + index,
                           email=f'2email{index}@mail.com',
                           password='1234',
                           first_name=f'2fname{index}',
                           middle_name=f'2mname{index}',
                           last_name=f'2lname{index}'
                           )
    user_free.save()

    author1 = Author(id=100 + index,
                     name="AuthorName1",
                     surname="AuthorSurname1",
                     patronymic="Patronymic1"
                     )
    author1.save()

    author2 = Author(id=101 + index,
                     name="AuthorName2",
                     surname="AuthorSurname2",
                     patronymic="Patronymic2")
    author2.save()

    book1 = Book(id=100 + index,
                 name=f"book1_{index}",
                 description=f"description1_{index}",
                 count=index
                 )
    book1.save()
    book1.authors.add(author1)
    book1.save()

    book2 = Book(id=101 + index,
                 name=f"book2_{index}",
                 description=f"description2_{index}",
                 )
    book2.save()
    book2.authors.add(author2)
    book2.save()

    book3 = Book(id=102 + index,
                 name=f"book3_{index}",
                 description=f"description3_{index}",
                 )
    book3.save()
    book3.authors.add(author1)
    book3.authors.add(author2)
    book3.save()

    order1 = Order(id=100+index,
                   user=user,
                   book=book1,
                   plated_end_at=TEST_DATE
                   )
    order1.save()
    order2 = Order(id=101+index,
                   user=user,
                   book=book2,
                   plated_end_at=TEST_DATE
                   )
    order2.save()
    order3 = Order(id=102+index,
                   user=user,
                   book=book3,
                   end_at=TEST_DATE_END,
                   plated_end_at=TEST_DATE)
    order3.save()

