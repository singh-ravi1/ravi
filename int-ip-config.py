from ncclient import manager
m = manager.connect(host="10.0.0.1", port="830", username="cisco", password="cisco", hostkey_verify=False)



Interface_template = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
	  <name>{int_name}</name>
	  <description>{int_desc}</description>
	  <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
	  <enabled>true</enabled>
	  <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
		<address>
		  <ip>{ip_address}</ip>
		  <netmask>{subnet_mask}</netmask>
		</address>
	  </ipv4>
	</interface>
  </interfaces>
</config>
"""

# Build the XML Configuration to Send
netconf_payload = Interface_template.format(int_name="GigabitEthernet2",
                                          int_desc="NETCONF Script",
                                          ip_address="10.255.255.1",
                                          subnet_mask="255.255.255.0"
                                          )


print("Configuration Parameters:")
print("----------------------")
print(netconf_payload)

# Send NETCONF <edit-config>
netconf_reply = m.edit_config(netconf_payload, target="running")

# Print the NETCONF Reply
print(netconf_reply)


