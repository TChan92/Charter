from datetime import datetime

from django.core.cache import cache
from django.test import TestCase

from data.data_controller import get_neo_estimated_diameter


class TestDataController(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "2019-01-01": [
                {
                    "links": {
                        "self": "http://www.neowsapp.com/rest/v1/neo/3843317?api_key=DEMO_KEY"
                    },
                    "id": "1",
                    "neo_reference_id": "1",
                    "name": "Test Asteroid 1",
                    "nasa_jpl_url": "http://ssd.jpl.nasa.gov/",
                    "absolute_magnitude_h": 0,
                    "estimated_diameter": {
                        "kilometers": {
                            "estimated_diameter_min": 0.1,
                            "estimated_diameter_max": 1.1
                        },
                        "meters": {
                            "estimated_diameter_min": 0.2,
                            "estimated_diameter_max": 1.2
                        },
                        "miles": {
                            "estimated_diameter_min": 0.3,
                            "estimated_diameter_max": 1.3
                        },
                        "feet": {
                            "estimated_diameter_min": 0.4,
                            "estimated_diameter_max": 1.4
                        }
                    },
                    "is_potentially_hazardous_asteroid": False,
                    "close_approach_data": [
                        {
                            "close_approach_date": "2019-01-01",
                            "close_approach_date_full": "2019-Jan-01 00:00",
                            "epoch_date_close_approach": 1563154140000,
                            "relative_velocity": {
                                "kilometers_per_second": "1",
                                "kilometers_per_hour": "3600",
                                "miles_per_hour": "2"
                            },
                            "miss_distance": {
                                "astronomical": "3",
                                "lunar": "4",
                                "kilometers": "5",
                                "miles": "6"
                            },
                            "orbiting_body": "Earth"
                        }
                    ],
                    "is_sentry_object": False
                },
                {
                    "links": {
                        "self": "http://www.neowsapp.com/rest/v1/neo/3843317?api_key=DEMO_KEY"
                    },
                    "id": "2",
                    "neo_reference_id": "2",
                    "name": "Test Asteroid 2",
                    "nasa_jpl_url": "http://ssd.jpl.nasa.gov/",
                    "absolute_magnitude_h": 1,
                    "estimated_diameter": {
                        "kilometers": {
                            "estimated_diameter_min": 10.1,
                            "estimated_diameter_max": 11.1
                        },
                        "meters": {
                            "estimated_diameter_min": 10.2,
                            "estimated_diameter_max": 11.2
                        },
                        "miles": {
                            "estimated_diameter_min": 10.3,
                            "estimated_diameter_max": 11.3
                        },
                        "feet": {
                            "estimated_diameter_min": 10.4,
                            "estimated_diameter_max": 11.4
                        }
                    },
                    "is_potentially_hazardous_asteroid": False,
                    "close_approach_data": [
                        {
                            "close_approach_date": "2019-01-01",
                            "close_approach_date_full": "2019-Jan-01 00:00",
                            "epoch_date_close_approach": 1563154140000,
                            "relative_velocity": {
                                "kilometers_per_second": "2",
                                "kilometers_per_hour": "7200",
                                "miles_per_hour": "3"
                            },
                            "miss_distance": {
                                "astronomical": "4",
                                "lunar": "5",
                                "kilometers": "6",
                                "miles": "7"
                            },
                            "orbiting_body": "Earth"
                        }
                    ],
                    "is_sentry_object": False
                },
            ]
        }
        cache.delete(datetime.now().strftime('%Y-%m-%d'))

    def test_get_neo_max_estimated_diameter_default_params(self):
        data = get_neo_estimated_diameter(self.data)

        assert isinstance(data, dict)
        assert len(data.keys()) == 1
        assert data == {'2019-01-01': [1.2, 11.2]}

    def test_get_neo_min_estimated_diameter_default_params(self):
        data = get_neo_estimated_diameter(self.data, max=False)

        assert isinstance(data, dict)
        assert len(data.keys()) == 1
        assert data == {'2019-01-01': [0.2, 10.2]}
