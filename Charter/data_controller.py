"""
This file is for manipulating datasets and rest apis. Once it gets a bit bigger, this will get split into multiple file
TODO feed this data into Charter
"""
import requests
import json
from django.core.cache import cache
from datetime import datetime


def get_diameters_for_date(date, max=True, unit='meters'):
    """
    Gets the estimated diameter of projectiles
    :param date:  list of dict. dict should have info about projectiles
    :param max: bool, if false, will get min estimated diameter
    :param unit: str, valid choices: kilometers, meters, miles, feet
    :return: list of ints
    """
    if max:
        value = 'estimated_diameter_max'
    else:
        value = 'estimated_diameter_min'
    return [x['estimated_diameter'][unit][value] for x in date]


def get_neo_max_estimated_diameter(data, max=True, unit='meters'):
    """
    Gets the max estimated diameter of neo objects in the last week
    :return: dict of list: {date:[diam1, diam2,...],...}
    """
    max_estimated_diameter = {}
    for k,v in data.items():
        max_estimated_diameter[k] = get_diameters_for_date(v, max, unit)

    return max_estimated_diameter


def get_nasa_neo():
    """
    Returns Nasa's Near Earth Object data from cache or REST API
    :return: error code 500 or dict
    """
    cache_key = datetime.now().strftime('%Y-%m-%d')
    data = cache.get(cache_key)
    if data is None:
        r = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params={
            'start_date': '2019-07-14',
            'end_date': '2019-07-21',
            'api_key': 'DEMO_KEY'  # Rate limited, so must use cache
        })

        if r.status_code != 200:
            return 500
        data = json.loads(r.text)

        data = data['near_earth_objects']
        seralized_data = json.dumps(data)
        cache.set(cache_key, seralized_data)
    return data


if __name__ == '__main__':
    data = get_nasa_neo()
    data = json.loads(data)
    print(get_neo_max_estimated_diameter(data))
