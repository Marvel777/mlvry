from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import UserProfile
from orders.models import Order, OrderDetails, Payment
from products.models import Product
from .serializers import UserProfileSerializer, OrderSerializer, OrderDetailsSerializer, PaymentSerializer, ProductSerializer

@api_view(['GET'])
def UserProfileData(request):
    userprofile = UserProfile.objects.all()
    serializer = UserProfileSerializer(userprofile, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def OrderData(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def OrderDetailsData(request):
    orderdetails = OrderDetails.objects.all()
    serializer = OrderDetailsSerializer(orderdetails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PaymentData(request):
    payment = Payment.objects.all()
    serializer = PaymentSerializer(payment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProductData(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


