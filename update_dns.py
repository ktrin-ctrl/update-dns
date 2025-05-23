from libcloud.dns.types import Provider, RecordType
from libcloud.dns.providers import get_driver
import urllib.request
import os 
from secret_credentials import username, api_key


cls = get_driver(Provider.NFSN)
driver = cls(username, api_key)

zone = driver.get_zone('anymouse.org')
record = driver.ex_get_records_by(zone, name='local')
our_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')

if our_ip != record[0].data:
    delete_record = driver.delete_record(record[0])
    record = zone.create_record(name='local', type=RecordType.A, data=our_ip )
    print('Updated DNS, ip: {}'.format(our_ip))
else:
    print('DNS already accurate, ip: {}'.format(our_ip))