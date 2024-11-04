import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import MpesaDepositTransaction
from core.serializers import STKPushSerializer
from mpesa import query_status, send_stk_push

# Create your views here.

# TRIGGER STK PUSH #
class STKPush(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def post(self, request):
        data=request.data
        serializer = STKPushSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        phone_number = data.get('phone_number')
        amount = data.get('amount')
        trans_ref = data.get('trans_ref')
        description = data.get('description')
        resp = send_stk_push(phone_number, amount, trans_ref, description=description)

        instance.stk_resp =resp
        instance.save()

        return Response(resp)
    
    def get(self, request):
        CheckoutRequestID = request.GET.get('CheckoutRequestID')
        if CheckoutRequestID:
            resp = query_status(CheckoutRequestID)
            return Response(resp)
        return Response({'detail':'CheckoutRequestID required'}, status=400)

# MPESA DEPOSIT VALIDAION IF VALIDATION URL IS SET #
class MpesaValidation(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def post(self, request):
        
        data = request.data
        print('validation data', data)
        
        edited_date = data['TransTime']
        edited_date = datetime.strptime(edited_date, '%Y%m%d%H%M%S')

        mpesa_trans, created  = MpesaDepositTransaction.objects.get_or_create(
            phone_number=data["MSISDN"], acc_number=data["BillRefNumber"], names=(data['FirstName']), transaction_id=data['TransID'], amount=int(float(data['TransAmount'])), trans_date=edited_date, trans_type='DEPOSIT', status='VALIDATING')

        return Response({"ResultCode": 0,"ResultDesc": "Accepted"})

# MPESA DEPOSIT CONFIRMATION AFTER VALIDAION / CALLBACK #
class MpesaConfirmation(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    
    def post(self, request):
        
        data = request.data
        print('confirmation data', data)

        edited_date = data['TransTime']
        edited_date = datetime.strptime(edited_date, '%Y%m%d%H%M%S')

        mpesa_trans, created  = MpesaDepositTransaction.objects.get_or_create(
            phone_number=data["MSISDN"], acc_number=data["BillRefNumber"], names=(data['FirstName']), transaction_id=data['TransID'], amount=int(float(data['TransAmount'])), trans_date=edited_date, trans_type='DEPOSIT', status='PENDING')

        mpesa_trans.status = "SUCCESS"
        mpesa_trans.save()
        
        return Response({"ResultCode": 0,"ResultDesc": "Accepted"})