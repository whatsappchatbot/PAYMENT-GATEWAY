keyid = 'rzp_test_ixIzmpmVcqXV1J'
keySecret = 'fCwpPR7wrXeClCzZjA7adlKg'
import razorpay
client = razorpay.Client(auth=(keyid,keySecret))
data ={
    'amount' : 100*100,
    "currency": "INR",
    "receipt" : "TSC",
    "notes":{

       "name": "TEJAS",
       "Payment_for" : "IOT"
    }

}
order = client.order.create(data=data)
print(order)


#client.utility.verify_payment_signature(params_dict)