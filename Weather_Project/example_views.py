from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import generics
from .models import Creature, TradeOffer
from .forms import TradeOfferForm
from .serializers import TradeOfferSerializer
import json


@csrf_exempt  # For demo purposes only, remove in production
class TradeOfferCreateView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    def post(self, request, *args, **kwargs):
        form = TradeOfferForm(request.POST)
        if form.is_valid():
            # Get form data
            creature_to_trade = form.cleaned_data['creature_to_trade']
            desired_creature = form.cleaned_data['desired_creature']

            # Create a new trade offer
            trade_offer = TradeOffer(
                user=request.user,
                creature_to_trade=creature_to_trade,
                desired_creature=desired_creature
            )
            trade_offer.save()
            response_data = {'status': 'success',
                             'message': 'Trade offer created successfully.'}
            return JsonResponse(response_data)
        else:
            response_data = {'status': 'error',
                             'message': 'Form data is invalid.'}
            return JsonResponse(response_data, status=400)


@csrf_exempt  # For demo purposes only, remove in production
class TradeOfferListCreateView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    def get_queryset(self):
        return TradeOffer.objects.filter(user=self.request.user)


@csrf_exempt  # For demo purposes only, remove in production
class TradeOfferRetrieveDestroyView(LoginRequiredMixin, generics.RetrieveDestroyAPIView):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    def get_object(self):
        obj = get_object_or_404(TradeOffer, id=self.kwargs['trade_offer_id'])
        if obj.user != self.request.user:
            raise PermissionDenied("Unauthorized access.")
        return obj


@csrf_exempt  # For demo purposes only, remove in production
class TradeOfferAcceptView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    def patch(self, request, *args, **kwargs):
        trade_offer = get_object_or_404(
            TradeOffer, id=self.kwargs['trade_offer_id'], user=request.user)
        # Perform trade logic here
        # Update creature ownership and inventory for both users involved in the trade
        # ...
        trade_offer.delete()
        response_data = {'status': 'success',
                         'message': 'Trade offer accepted and processed successfully.'}
        return JsonResponse(response_data)


@csrf_exempt  # For demo purposes only, remove in production
class TradeOfferRejectView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    def delete(self, request, *args, **kwargs):
        trade_offer = get_object_or_404(
            TradeOffer, id=self.kwargs['trade_offer_id'], user=request.user)
        trade_offer.delete()
        response_data = {'status': 'success',
                         'message': 'Trade offer rejected and deleted successfully.'}
        return JsonResponse(response_data)
