import requests as req
import pandas as pd

res = req.get('https://restful-booker.herokuapp.com/booking')
response = res.json()

bookings = []
for item in response[:20]:
    booking_id = item['bookingid']
    detail = req.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}', timeout=10)
    if detail.status_code == 200:
        data = detail.json()
        bookings.append({
            'id': booking_id,
            'firstname': data.get('firstname'),
            'lastname': data.get('lastname'),
            'totalprice': data.get('totalprice'),
            'depositpaid': data.get('depositpaid'),
            'checkin': data.get('bookingdates', {}).get('checkin'),
            'checkout': data.get('bookingdates', {}).get('checkout'),
            'additionalneeds': data.get('additionalneeds')
        })

df = pd.DataFrame(bookings)
df.to_csv('bookings_data.csv', index=False)
print(df.to_string())