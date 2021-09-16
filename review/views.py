from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from review.models import Review
from review.serializers import ReviewListSerializer


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class CreateReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class UpdateReviewView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class DeleteReviewView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        elif self.action == 'retrieve':
            return ReviewListSerializer
        return ReviewListSerializer
