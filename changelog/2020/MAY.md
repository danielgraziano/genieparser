| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |       20.5    |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* IOSXE
    * Updated ShowMacAddressTable for new commnad:
        * show mac address-table vlan {vlan}
    * Added ShowSdwanBfdSessions for:
        * show sdwan bfd sessions
    * Added ShowSdwanBfdSummary for:
        * show sdwan bfd summary
    * Added ShowSdwanControlConnections for:
        * show sdwan control connections
    * Added ShowSdwanControlLocalProperties for:
        * show sdwan control local-properties

* IOS
    * Updated ShowMacAddressTable for new commnad:
        * show mac address-table vlan {vlan}

* LINUX
    * Added route
    * Added netstat -rn

* JUNOS
    * Added ShowOspfNeighborDetail for:
        * show ospf neighbor {neighbor} detail
    * Added ShowLogFilename for:
        * show log {filename}
    * Added ShowVersionDetail for:
        * show version detail
    * Added ShowVersionInvokeOnAllRoutingEngines for:
        * show version invoke-on all-routing-engines
    * Added ShowVersionDetailNoForarding for:
        * show version detail no-forwarding
    * Added ShowInterfacesDescriptions for:
        * show interfaces descriptions
    * Added ShowPfeRouteSummary for:
        * show pfe route summary
    * Added ShowInterfaces for:
        * show interfaces
    * Added ShowInterfacesExtensive for:
        * show interfaces extensive
        * show interfaces extensive {interface}
    * Added ShowInterfacesExtensiveNoForwarding for:
        * show interfaces extensive no-forwarding
    * Added ShowOspfDatabaseLsaidDetail for:
        * show ospf database lsa-id {ipaddress} detail
    * Added ShowOspfDatabaseNetworkLsaidDetail for:
        * show ospf database network lsa-id {ipaddress} detail
    * Added ShowOspf3DatabaseLinkAdvertisingRouter for:
        * show ospf3 database link advertising-router {ipaddress} detail
    * Added ShowOspf3DatabaseNetworkDetail for:
        * show ospf3 database network detail

* VIPTELA
    * Added ShowBfdSessions for:
        * show bfd sessions
    * Added ShowBfdSummary for:
        * show bfd summary
    * Added ShowControlConnections for:
        * show control connections
    * Added ShowControlLocalProperties for:
        * show control local-properties

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOS
    * Updated ShowIpArp
        * Added argument 'output' into super().cli()

* IOSXE
    * Fixed ShowBootvar to support more outputs
    * Removed duplicate ShowBoot parser & fixed existing ShowBoot parser
    * Fixed ShowDmvpn not executing the command properly on device
    * Update ShowIpRoute:
        * Fixed regex for VRF name, now supports the '-' character in name.
    * Update ShowCdpNeighborsDetail:
        * Modified regex to parse interface and port_id like FastEthernet0/0.1 and Serial0/0/0:1
    * Updated ShowInterfacesSwitchport:
        * Fixed the order of conditional statements, now the parser can parse the device output correctly
    * Updated ShowAccessLists:
        * Fixed a typo in code.
    * Updated ShowIpCefInternal:
        * Change some keys to Optional.
    * Updated ShowIpRouteWord:
        * Fixed a typo in code
    * Update ShowVtpStatus:
        * Changed the following keys into Optional: 'maximum_vlans' and 'md5_digest'.
    * Update ShowLldpEntry:
        * Fixed regex for chassis id, now also supports ':' and '-'.
        * Fixed regex for description, now also supports messages like '{"SN":"SN-NR","Owner":"OWNER"}'.
        * Fixed regex for management addresses, now also supports IPv6 addresses.
        * Changed the following keys into Optional for 'med_information': 'f/w_revision', 'power_source', 'power_priority', 'wattage' and 'capabilities'.
    * Update ShowCdpNeighborsDetail:
        * Fixed regex for platform, now also supports ':'.
    * Update ShowVlan:
        * Fixed regex for vlan name, now also supports multiple white spaces.
        * Added regex for toking ring table.
        * Added the following keys: 'token_ring', 'are_hops', 'ste_hops' and 'backup_crf'.
    * Update ShowSwitchDetail
        * Changed the following keys into Optional: 'mac_persistency_wait_time' and 'hw_ver'.
    * Update ShowVersion:
        * Fixed regex for interface and ethernet_type, now also supports 'FastEthernet'.
        * Changed the key 'virtual_ethernet' value to optional.
        * Added the following keys 'fastethernet', 'power_supply_part_nr', 'power_supply_sn', 'db_assembly_num', 'db_sn', 'top_assembly_part_num', 'top_assembly_rev_num', 'version_id', 'clei_code_num', 'db_rev_num' and 'hb_rev_num'
        * Added regex for swith table without 'Mode' column.
    * Renamed ShowPowerInlineInterface to ShowPowerInline
        * Added 'watts' information the schema, containing available, used and remaining watts.
        * Added regex to parse watts information
        * Changed the regex to also support white spaces in device names

* IOSXR
    * Updated ShowBgpSessions:
        * Added regex to support various outputs
    * Updated ShowBgpInstanceNeighborsDetail:
        * Updated regex to support various outputs
    * Updated ShowLldpNeighborsDetail:
        * Updated regex to support various outputs
    * Updated Dir
        * Fixed regex to support various outputs

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional
    * Updated ShowRunInterface:
        * Add regex to support various sample outputs
    * Updated ShowInterfaceStatus:
        * Fix a regex pattern to support various outputs
    * Updated ShowInterface
        * Added regex to support interfaces down for SFP Not Inserted
        * Added regex to support interfaces down for ErrDisabled
        * Added regex to support interfaces down due to being suspended (LACP)

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.
    * Updated ShowRouteProtocolExtensive:
        * Update key 'validation-state' as Optional
    * Update ShowRouteProtocolExtensive for:
        * show route {route} extensive
        * show route extensive
        * show route extensive {destination}

* ASA
    * Updated ShowRoute:
        * Fixed the logic for overlapping prefixes.
        * Fixed the OSPF protocol mappings.
        * Parser optimization for dynamic routing protocols (EIGRP, OSPF, BGP, etc)

* LINUX
    * Fixed Ifconfig parser issues.