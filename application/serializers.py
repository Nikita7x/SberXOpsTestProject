from datetime import datetime
from typing import List

from rest_framework import serializers
from urllib.parse import urlparse

from . import models


class Activity:

    class Create(serializers.Serializer):
        links = serializers.ListField(child=serializers.CharField(required=True), required=True)

        def create(self, validated_data) -> List[models.Activity]:
            visited_domains_activity = []
            now = datetime.now()

            for link in validated_data['links']:
                visited_domains_activity.append(
                    models.Activity(
                        domain=urlparse(link).netloc,
                        datetime=now
                    )
                )

            models.Activity.objects.bulk_create(
                visited_domains_activity
            )
            return visited_domains_activity

        def validate(self, data):
            for link in data['links']:
                if urlparse(link).netloc == '':
                    raise serializers.ValidationError(
                        detail={
                            'status': {
                                'link': link,
                                'message': 'Не удалось определить домен у ссылки. Проверьте данные'
                            },
                        }
                    )
            return data


    class List(serializers.ModelSerializer):
        class Meta:
            model = models.Activity
            fields = ('domain',)





