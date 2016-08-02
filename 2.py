import urllib2
response = urllib2.urlopen('http://db-sjc-tel-04.tktn.be:5799/hazelcast/rest/maps/pre_register/0B73AA5B-8A65-4608-AC3D-7955C18B23CA')
print response.read()