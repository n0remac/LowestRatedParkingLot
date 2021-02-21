import requests
import json

'''
ddress, an image if available, star rating, review count, and link to the Yelp page.

'''

def search(location):
    api_key='mi5qSSqdhmrNXBjLq5MBMwuqcS0q8aE4u52fwqrG8CkrBjjksgdV8ZblHdh4ThtDqQVFapfOwrCqadcTH4sJIMhQgEcWpc0bK_9ms_rJ1H-xMT1Amp4tmH_PhAg3X3Yx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url='https://api.yelp.com/v3/businesses/search'

    params = {'term':'parking','location': location}
    req = requests.get(url, params=params, headers=headers)

    # printing the text from the response
    results = json.loads(req.text)
    businesses = results['businesses']
    businesses = sorted(businesses, key = lambda i:i['rating'])
    ret = []
    for b in businesses:
        id = b['id']
        address = b['location']
        image = b['image_url']
        rating = b['rating']
        reviews = b['review_count']
        yelp_link = b['url']
        #score = ( number of reviews * rating ) / (number of reviews + 1)
        score = (int(reviews) * int(rating)) / (reviews + 1)
        ret.append({'score':score, 'address':address, 'image':image, 'rating': rating, 'reviews':reviews, 'yelp_link':yelp_link})

    return ret

search('Los Angeles')