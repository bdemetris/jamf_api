__author__ = 'brett_demetris'

import requests
import xml.etree.ElementTree as ET

jssURL = 'https://jssurl.com:8443/JSSResource/computers/id/'

jssAuth = 'username', 'password'

# Create a List of IDs That Need to be Unmanaged
xmlFile = 'PATH TO XML EXPORT.xml'
tree = ET.parse(xmlFile)

ids = []
for id in tree.iter('JSS_Computer_ID'):
    ids.append(id.text)

print ids

xmlTemplate = """<?xml version="1.0" encoding="ISO-8859-1"?>
<computer>
  <general>
    <remote_management>
      <managed>false</managed>
    </remote_management>
  </general>
</computer>
"""

for id in ids:
    r = requests.put(jssURL + id, auth=jssAuth, data=xmlTemplate)
    print r.content
