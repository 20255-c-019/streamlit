
import time
import requests
import json
def serverrequest(data):


    url = "https://apiv2.sonyliv.com/AGL/1.7/SR/ENG/WEB/IN/SUBSCRIPTION/PRODUCTSBYCOUPON"

    payload = {'voucherCode': data,
    'channelPartnerID': 'MSMIND'}
    files=[

    ]
    headers = {
      'Security_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTg3NjkxNDQsImV4cCI6MTcyMDA2NTE0NCwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.RvvjGhYZ64QOSLSTcvjrakL-Wifp2uqzpxAa6HP0gXI5GQu8qhpu6MY81I4MnSNdzGJrOM0ADFThszdhncxmwtWsXms5_pEHZrfZs4z2OZglQlXlXUf51NzYB6Udqwashm7-l0Un0ZrAIAvhJVGwocWl8-6JBLbwzuFwzyei3X2mgkoZYnFpYTO7hJmCCMIq-2wa8pZ0GueTo9OnLh8rU850N9ZF9r_HxPlhk0Yd72oT1Ic5T_8gjXBtZLVvX0feFgBB_YNNoE42zTqY0tRBuiWP5PBxZFVrVQ7Fxlcn0Z25xKwjV3RnGb8sBvpy0g6Tx0XhnqZCPHiss6HFFeXqLPawiJwyPXWMHO653OWznNPeHeeGMSK_ecRdy6NfqzqGQrj3UNbWr7yejO1NF504CEiIEPiNbcCR4SEBoPJ3JEOSdjPWDIs0UZHQgrQ0iy7AJ8bw_aslytfSJz1qNobxjKsY8hpwvDSaxkGv-jgPznuuraHmTZ-ADfDprSltuZWQxv6Ip2M9Pi74OSc6Lrsb9zr0TQhUJyjUOTTqjhrUFdYY3CFBZatUIUCjh29yXvuWDAHl3PTR0mLblrwChrwR8UB4CNCJ9aiViCxOZNhAPyAYybC1s21VlDd_NOd_KHcMwgq60Qd4dNPDHO1y8VgQZ7NYs64TnFDl8m54JqtGYCY',
      'Cookie': '_abck=95D5F09874ACFA7EA58FE6FFC917A8C8~-1~YAAQis5JF8KwyvCPAQAATL/YOgzP/nndOFM/GSlf15GGi7hv28tJM7oj3k15ePm4Xece3d4Tahj0p3s3wRAFQ4DsbWggqvai7weuc6TweDT7Qht3Y0PT4MOZUctM5R4KReTWwTgsSzlK+b2x6bSSEcoOrYqhoWbdnusQCRH67kMxqJK315gnLFJrdLSPRp2oVquZP82NoTfQy85/iyu0ZfDzT1RiBIVYgqBBOOSd9eOw+y2smpFktXAta9AjFkuO6/ej/RsVclxexR2kIs5+Ts5gciKWiqT1Obw8J8q0mzkHDaJTQvG7skXHGZhHE97JscUK5ppEIyNIJAqowTIcHxvlKI4b1pKOTH1bK59Rr45hEW8zQcwjpbfzLV71oL1/gz2tzzifCZK73mtFW5FDjEilL47zicmwzm/TeRAc35zaN2VgqMjSS3cefuQlD8qeW71MvKF/~-1~-1~-1; bm_sz=AEF82DC650BFC6E850719E9851C0E038~YAAQis5JF8OwyvCPAQAATL/YOhh6IHefTYN+LM3Uyh86UZ1wcOZiHk3A0Ef4IYLBivdae4s8Enghy8qvW/j+0ldUsA8h6e+eM44ywt8l/hCQHhiPxjbi7fUdDLrImNaAIxEz1m+NQV7eLJF6VREce0XYswAhoTz9bI4YC3YMyhiq4DTQU8w2245RjOimMIfgbi77Z6JvEYHpdkI0Gu3QDQ1yGpluVC9d48whTTgv8xpB+xMRt70OGftM9bPoscab1AaIs5swiElrBl7eNcSsrMUtTvGJX/HQbPKn8TFTzOQd2OEC+ZDqhCa+WP1QFZMKZ0EUd6Inw/d4sdXX/nxsWwm+D+EqYJ4x4/0qOdlj~3683653~4536645'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    return response.text



def checkcode(codes_array):
    check_response=[]
    for code in codes_array:
        time.sleep(1)
        api=json.loads(serverrequest(code))
        response=""
        if(api["message"]==""):
            response= "successful coupon appiled "
        else:
            response=api["message"]


        check_response.append(code+"       "+response)
    return check_response


import streamlit as st

codes_txt = st.text_area("sonyliv codes")


if st.button("submit"):
   codes_array = codes_txt.splitlines()
   print(codes_array)
   data =checkcode(codes_array)
   for code in data:
       st.write(code)

