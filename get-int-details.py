from ncclient import manager
import xml.dom.minidom

m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco")
Interface_filter = '''
 <filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
   <interface>
    <GigabitEthernet>
     <name>2</name>
    </GigabitEthernet>
   </interface>
  </native>
 </filter>
'''

print("Configuration Parameters:")
print("----------------------")
result = m.get_config('running', Interface_filter)
print(xml.dom.minidom.parseString(str(result)).toprettyxml())

print("----------------------")
