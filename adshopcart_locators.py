import datetime
from faker import Faker
fake = Faker(locale='en_CA')

app = 'Advantage Shopping Cart'
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_home_page_title = "\xa0Advantage Shopping"


username = fake.user_name()[5:14]
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


check_list1 = ["SPEAKERS", "TABLETS", "LAPTOPS", "MICE"]
check_list2 = ["SPECIAL OFFER", "POPULAR ITEMS", "CONTACT US"]
subject = f'Today is: {datetime.datetime.now()}. '

categories = ["Laptops", "Headphones", "Tablets", "Speakers", "Mice"]
