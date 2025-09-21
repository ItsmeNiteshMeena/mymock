from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        avg_rating = Feedback.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
        total_feedback = Feedback.objects.count()
        return Response({
            'total_feedback': total_feedback,
            'average_rating': avg_rating
        })
