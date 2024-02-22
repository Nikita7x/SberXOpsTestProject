from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers, models
from .filters import DateRangeFilter


class Activity(
    viewsets.GenericViewSet
):
    serializer_class = serializers.Activity.Create

    @action(detail=False, methods=['post'])
    def visited_links(self, request):

        serializer = serializers.Activity.Create(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({"status": "ok"})

    @action(detail=False, methods=['get'])
    def visited_domains(self, request):
        queryset = models.Activity.objects.all().distinct()
        queryset = DateRangeFilter.filter_queryset(queryset, request)
        data = queryset.values_list('domain', flat=True)
        from rest_framework import status
        return Response(
            data={
                "domains": data,
                "status": "ok"
            },
            status=status.HTTP_200_OK
        )



