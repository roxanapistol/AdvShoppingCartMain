import datetime
from faker import Faker
fake = Faker(locale='en_CA')

app = 'Advantage Shopping Cart'
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_home_page_title = "\xa0Advantage Shopping"


username = fake.user_name()[0:15]
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'

email = fake.email()
city = fake.city()
phone = fake.phone_number()
address = fake.address().replace("\n", " ")[0: 50]
province = fake.province()[0: 10]
postal_code = fake.postcode()
country = fake.current_country()

subject = f'Today is: {datetime.datetime.now()}. '

