from datetime import datetime
from rest_framework import serializers


class DateRangeFilter:
    @staticmethod
    def filter_queryset(queryset, request):
        from_parameter = request.GET.get('from')
        to_parameter = request.GET.get('to')

        if from_parameter:
            try:
                dt = datetime.fromtimestamp(int(from_parameter))

            except ValueError:
                raise serializers.ValidationError(detail={"status": "Неправильный формат даты начала"})

            queryset = queryset.filter(datetime__gte=dt)

        if to_parameter:
            try:
                dt = datetime.fromtimestamp(int(to_parameter))
            except ValueError:
                raise serializers.ValidationError(detail={"status": "Неправильный формат даты конца"})

            queryset = queryset.filter(datetime__lte=dt)

        return queryset
