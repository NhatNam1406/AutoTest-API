# Authority
username='raizo'
password='PassW0rd!$'

# Host
hostlocal='http://localhost:8081/ws/rest/'
host=hostlocal
# Endpoint
endpoint_token='get-token?username={{username}}&password={{password}}'
endpoint_token= endpoint_token.replace('{{username}}', username).replace('{{password}}', password)

endpoint_servicerequest='service-requests'


endpoint=endpoint_token





