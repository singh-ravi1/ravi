from ncclient import manager
import xml.dom.minidom

m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco", device_params={"name":"csr"})

running_config = m.get_config('running')
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

