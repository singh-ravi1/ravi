from ncclient import manager
import xml.dom.minidom

# IOS XE Settings
host_ip = "10.0.0.1"
port_no = 830
user = "cisco"
pass = "cisco"

m = manager.connect( host=host_ip, port=port_no, username=user, password=pass, hostkey_verify=False, look_for_keys=False )

netconf_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                        <name>Loopback1</name>
                </interface>
        </interfaces>
</config>
"""


print("Configuration Parameters:")

print(netconf_template)

netconf_reply = m.edit_config(netconf_template, target = "running")

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

m.close_session()

# Print the NETCONF Reply
print(netconf_reply)

