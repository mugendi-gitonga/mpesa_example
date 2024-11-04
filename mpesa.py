
import base64
import datetime
import os
from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth


def get_mpesa_token(consumerKey=None, consumerSecret=None):
    url = f"{settings.MPESA_BASE_API_URL}/oauth/v1/generate?grant_type=client_credentials"
    resp = requests.get(url, auth=HTTPBasicAuth(
        consumerKey, consumerSecret), timeout=60)
    if not resp.status_code == 200:
        raise Exception(resp.text)

    access_token = resp.json().get('access_token')
    expires_in = resp.json().get('expires_in')
    return access_token


def send_stk_push(phone_number, amount, trans_ref, description=None):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode('utf-8')).decode('utf-8')

    token = get_mpesa_token(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": settings.MPESA_TRANS_TYPE,
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_PARTY_B,
        "PhoneNumber": phone_number,
        "CallBackURL": f'{settings.HOSTING_DOMAIN}/payment/confirmation/',
        "AccountReference": trans_ref,
        "TransactionDesc": description
    }

    url = f"{settings.MPESA_BASE_API_URL}/mpesa/stkpush/v1/processrequest"
    resp = requests.post(url, json=payload, headers=headers)
    json_resp = resp.json()
    print(json_resp)
    return json_resp


def query_status(CheckoutRequestID):
    
    url = f"{settings.MPESA_BASE_API_URL}/mpesa/stkpushquery/v1/query"
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode('utf-8')).decode('utf-8')

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "CheckoutRequestID": CheckoutRequestID #STK_PUSH request ID from response
    }

    token = get_mpesa_token(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
    headers = {
        "Authorization": f"Bearer {token}"
    }

    resp = requests.post(url, json=payload, headers=headers)
    json_resp = resp.json()
    print(json_resp)
    return json_resp


