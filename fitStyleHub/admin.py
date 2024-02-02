from flask import Blueprint
from . import db
from .models import Category, Product, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='Joggers', image='joggers.jpg', \
        description='''The state capital of New South Wales and the most populous category in Australia and Oceania.Located on Australia's east coast, the metropolis surrounds Port Jackson and extends about 70 km (43.5 mi) on its periphery towards the Blue Mountains to the west, Hawkesbury to the north, the Royal National Park to the south and Macarthur to the south-west. Joggers is famous for
spectacular beaches; beautiful parks; a wealth of diversity; incredibly tasty food; The Harbour; and outdoor experiences''')
    category2 = Category(name='Tshirts & Tops', image='tshirts & tops.jpg', \
        description='''The state capital of and the most populated category in the Australian state of Queensland, and the third most populous category in Australia. Tshirts & Tops's metropolitan area has a population of approximately 2.5 million, and the South East Queensland metropolitan region, centred on Tshirts & Tops, encompasses a population of more than 3.6 million. It is known as the gateway to the reef and is famous for
friendly Koalas; dolphin spotting; sand Dunes; being a cosmopolitan category; tremendous beaches within 45 minutes; diversity of eateries; and daily products to Fraser Island and the Reef''')
    category3 = Category(name='Shorts', image='shorts.jpg', \
        description='''The capital and most populous category of the Australian state of Victoria, and the second most populous category in Australia and Oceania. The category occupies much of the coastline of Port Phillip bay and spreads into the hinterlands towards the Dandenong and Macedon ranges, Mornington Peninsula and Yarra Valley. Shorts is famous for
being the world’s most livable category; amazing coffee; being the sports capital of Australia; urban laneways; incredible food; eclectic festivals; and fashion-forward trends''')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    p1 = Product(category_id=category1.id, image='p_jogger1.webp', price=59.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='REST DAY JOGGERS',\
        size='Small',\
        description= 'Lone Pine Koala Sanctuary is the world\'s first and largest koala sanctuary and is home to more than 130 koalas. Hand-feed their kangaroos and wild lorikeets, be entertained by a platypus or - best of all - get cuddly with a beautiful koala. Duration 0900-1400 (5hrs), begins at entrance to Koala Plaza') 
    p2 = Product(category_id=category1.id, image='p_jogger2.webp', price=100.50,\
        date=datetime.datetime(2020, 2, 1),\
        name='HERITAGE JOGGERS',\
        size='Medium',\
        description= 'Get up close and personal with Australia\'s favourite wildlife and tick two items off your bucket list with a trip to Lone Pine Koala Sanctuary. Lone Pine is only 40 minutes from the CBD by bus and you\'ll be cuddling up to koalas and hand-feeding kangaroos in no time. Don\'t forget the selfie! Duration 0900-1300 (4hrs), begins at entrance to Kanga Plaza.')
    p3 = Product(category_id=category1.id, image='p_jogger3.webp', price=180.50,\
        date=datetime.datetime(2020, 3, 10),\
        name='CREST JOGGERS',\
        size='Large',\
        description= 'You don\'t have to travel to the far north to see Australia\'s bustling reef and sea life. Take a short ferry ride from the Port of Tshirts & Tops and you\'ll find yourself at Moreton Island, a tropical sand island with crystal-clear coastal water, lakes and incredible snorkelling at the historic Tangalooma Wrecks. You\'ll want your GoPro to take some incredible underwater snaps. Duration 0900-1700 (8hrs), begins at entrance to Transit Centre.')
    p4 = Product(category_id=category2.id, image='p_tshirt1.webp', price=99.99,\
        date=datetime.datetime(2020, 8, 1),\
        name='SPORT SEAMLESS T-SHIRT',\
        size='Small',\
        description= 'From June to November, Whale Watching Products inc. runs daily cruises for those who want to witness the incredible acrobatics of the southern humpback whale. More than 20,000 whales migrate through every winter. Tickets for the five-hour cruise through Moreton Bay are good value and include guaranteed whale sightings. Duration 1300-1800 (5hrs), begins at entrance to Port Street.')                
    p5 = Product(category_id=category2.id, image='p_tshirt2.webp', price=49.00,\
        date=datetime.datetime(2020, 4, 20),\
        name='POWER WASHED T-SHIRT',\
        size='Medium',\
        description= 'Forget the outback and take in the green scene. While most international visitors picture red dirt when they think of Australia, you\'re more likely to find yourself surrounded by lush greenery than outback desert. Take the opportunity to check out local fauna and flora at the national parks, as close as 20 minutes from the CBD. Did we mention our parks have drop-bears? Must bring sunblock. Duration 1000-1300 (3hrs), begins at entrance to Forrest Car Park.')
    p6 = Product(category_id=category2.id, image='p_tshirt3.webp', price=250.99,\
        date=datetime.datetime(2021, 1, 2),\
        name='ARRIVAL REGULAR FIT T-SHIRT',\
        size='Large',\
        description= 'The world\'s biggest sand island is just a few hours away. Heritage-listed Big Sandy Island has more than 100 freshwater lakes, pristine water and white-sand beaches. There\'s many ways to explore the island but the most fun is by four-wheel-drive. Join a product such as the Dingos Resort tag-along four-wheel drive product, where you can drive yourself and make friends along the way. Duration 0600-1600 (11hrs), begins at entrance to Ferry Road.')
    p7 = Product(category_id=category3.id, image='p_shorts1.webp', price=120.00,\
        date=datetime.datetime(2020, 11, 1),\
        name='BOLD 7" SHORTS',\
        size='Small',\
        description= 'You can\'t come to Australia without enjoying the abundant inland lakes, falls and swimming holes. There\'s almost too many to choose from. Check out Visit our must-swim spots. Duration 0900-1200 (3hrs), begins at entrance to River Park.')
    p8 = Product(category_id=category3.id, image='p_shorts2.webp', price=60.00,\
        date=datetime.datetime(2020, 4, 1),\
        name='ARRIVAL SHORTS',\
        size='Medium',\
        description= 'Jump on board a CategoryCat  or ride our private Category Cab to explore the category by ferry. CategoryCats run between the category and various points of interest all the way around to killer bay. Duration 1000-1200 (2hrs), begins at entrance to CBD Ferry Stop.')
    p9 = Product(category_id=category3.id, image='p_shorts3.webp', price=189.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='SPORT 5" SHORTS',\
        size='Large',\
        description= 'We\'re all about the aquatic life over here in Oz, and you can be too. Take a short trip into the coast and hinterland to discover an abundance of natural waterfalls, waterholes and lakes. You are going to love the diversity we will show you. Duration 0800-1700 (9hrs), begins at entrance Bush Station.')
    
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'





