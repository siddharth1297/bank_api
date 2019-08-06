export jwt="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY1NTM2OTk1LCJlbWFpbCI6ImFkbWluQGJhbmsuY29tIn0.HUyWPBGxfXEn_HV6igBJS_ac4xL7X6zTb-jZitz6qB0"



# Get all the bank details 

echo "------ All the banks details limit=5 and offset=8 ------"
echo

curl -X GET \
  'https://sidd-bank-api.herokuapp.com/api/bank/?limit=10&offset=8' \
  -H "Authorization: Bearer $jwt" \


# Get bank details with given ifsc
echo
echo
echo "------Bank details for ifsc=ABHY0065015------"
echo

curl -X GET \
  https://sidd-bank-api.herokuapp.com/api/bank/ABHY0065015/ \
  -H "Authorization: Bearer $jwt" \


# Get bank details with given name and city
echo
echo
echo "------ All the banks details for name='HDFC BNAK' and city='MUMBAI' with limit=5 and offset=2 ------"
echo

curl -X GET \
  'https://sidd-bank-api.herokuapp.com/api/search/HDFC%20BANK-MUMBAI/?limit=5&offset=2' \
  -H "Authorization: Bearer $jwt" \
  
echo
