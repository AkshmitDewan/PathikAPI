import http.client

conn = http.client.HTTPSConnection("pathik.guru")
payload = 'email=info%40sgsrgroup.com&password=Unread%232022%24'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/login/validate_login", payload, headers)
response = conn.getresponse()
cookie_header = response.getheader('Set-Cookie')
conn = http.client.HTTPSConnection("pathik.guru")
payload = ''
headers = {
  'Cookie': cookie_header
}
conn.request("POST", "/dashboard/validate_guest", payload, headers)
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()

# print(data.decode("utf-8"))
