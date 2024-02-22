from rest_framework.test import APIClient
from application import models
from application.tests import factories


class TestActivity:

    def get_client(self):
        client = APIClient()
        return client

    def test_create_activity(self, db):
        client = self.get_client()

        body = {
            "links": [
                "http://example.com",
                "http://example.com/hello_world/",
                "http://google.com/search?q=hello+world",
                "https://ya.ru",
            ]
        }

        expected_response_body = {
            "status": "ok"
        }

        response = client.post(path='/visited_links/', data=body)
        assert response.status_code == 200
        assert response.data == expected_response_body

        created_activities = models.Activity.objects.all()

        assert len(created_activities) == 4
        assert created_activities[0].domain == "example.com"
        assert created_activities[1].domain == "example.com"
        assert created_activities[2].domain == "google.com"
        assert created_activities[3].domain == "ya.ru"

    def test_get_activity(self, db):
        client = self.get_client()

        activities = factories.ActivityFactory.create_batch(3)
        activities__only_domains = [activity.domain for activity in activities]

        response = client.get('/visited_domains/')

        assert list(response.data['domains']) == activities__only_domains
        assert response.data['status'] == 'ok'
