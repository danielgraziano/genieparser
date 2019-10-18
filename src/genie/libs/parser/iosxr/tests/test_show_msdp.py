# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show msdp
from genie.libs.parser.iosxr.show_msdp import ShowMsdpPeer, ShowMsdpContext, ShowMsdpSummary


class TestShowMsdpPeer(unittest.TestCase):
    """
        Commands:
        show msdp peer
        show msdp vrf <vrf> peer
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'default': {
                'peer': {
                    '202.202.33.3': {
                        'connect_source_address': '202.202.11.1',
                        'elapsed_time': '00:00:09',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'StopRead',
                            'up_down_time': '1d02h'},
                        'password': 'None',
                        'peer_as': 65109,
                        'reset': '999',
                        'sa_filter': {
                            'in': {
                                '(S,G)': {
                                    'filter': 'none'},
                                'RP': {
                                    'filter': 'none'}},
                            'out': {
                                '(S,G)': {
                                    'filter': 'none'},
                                'RP': {
                                    'filter': 'none'}}},
                        'sa_request': {
                            'input_filter': 'none',
                            'sa_request_to_peer': 'disabled'},
                        'session_state': 'Inactive',
                        'statistics': {
                            'conn_count_cleared': '00:01:25',
                            'output_message_discarded': 0,
                            'queue': {
                                'size_input': 0,
                                'size_output': 0},
                            'received': {
                                'sa_message': 0,
                                'tlv_message': 0},
                            'sent': {
                                'tlv_message': 3}},
                        'timer': {
                            'keepalive_interval': 30,
                            'peer_timeout_interval': 75},
                        'ttl_threshold': 2}}}}}

    device_output_1 = {
        'execute.return_value': '''
        Router# show msdp peer

        MSDP Peer 202.202.33.3 (?), AS 65109
        Description:
          Connection status:
            State: Inactive, Resets: 999, Connection Source: 202.202.11.1
            Uptime(Downtime): 00:00:09, SA messages received: 0
            TLV messages sent/received: 3/0
          Output messages discarded: 0
            Connection and counters cleared 00:01:25 ago
          SA Filtering:
            Input (S,G) filter: none
            Input RP filter: none
            Output (S,G) filter: none
            Output RP filter: none
          SA-Requests:
            Input filter: none
            Sending SA-Requests to peer: disabled
          Password: None
          Peer ttl threshold: 2
          Input queue size: 0, Output queue size: 0
          KeepAlive timer period: 30
          Peer Timeout timer period: 75
          NSR:
            State: StopRead, Oper-Downs: 0
            NSR-Uptime(NSR-Downtime): 1d02h
    '''}

    expected_output_2 = {
        'vrf': {
            'VRF1': {
                'peer': {
                    '1.1.1.1': {
                        'connect_source_address': '22.22.22.23',
                        'description': 'R1',
                        'elapsed_time': '18:19:47',
                        'nsr': {
                            'oper_downs': 0,
                            'state': 'Unknown',
                            'up_down_time': '22:46:31'},
                        'password': 'None',
                        'peer_as': 0,
                        'reset': '0',
                        'sa_filter': {
                            'in': {
                                '(S,G)': {
                                    'filter': 'safilin'},
                                'RP': {
                                    'filter': 'none'}},
                            'out': {
                                '(S,G)': {
                                    'filter': 'safilout'},
                                'RP': {
                                    'filter': 'none'}}},
                        'sa_request': {
                            'input_filter': 'none',
                            'sa_request_to_peer': 'disabled'},
                        'session_state': 'Listen',
                        'statistics': {
                            'conn_count_cleared': '22:46:31',
                            'output_message_discarded': 0,
                            'queue': {
                                'size_input': 0,
                                'size_output': 0},
                            'received': {
                                'sa_message': 0,
                                'tlv_message': 0},
                            'sent': {
                                'tlv_message': 0}},
                        'timer': {
                            'keepalive_interval': 30,
                            'peer_timeout_interval': 75},
                        'ttl_threshold': 222}}}}}

    device_output_2 = {'execute.return_value': '''
        Router# show msdp vrf VRF1 peer

        MSDP Peer 1.1.1.1 (?), AS 0
        Description: R1
          Connection status:
            State: Listen, Resets: 0, Connection Source: 22.22.22.23
            Uptime(Downtime): 18:19:47, SA messages received: 0
            TLV messages sent/received: 0/0
          Output messages discarded: 0
            Connection and counters cleared 22:46:31 ago
          SA Filtering:
            Input (S,G) filter: safilin
            Input RP filter: none
            Output (S,G) filter: safilout
            Output RP filter: none
          SA-Requests:
            Input filter: none
            Sending SA-Requests to peer: disabled
          Password: None 
          Peer ttl threshold: 222
          Input queue size: 0, Output queue size: 0
          KeepAlive timer period: 30
          Peer Timeout timer period: 75
          NSR:
            State: Unknown, Oper-Downs: 0
            NSR-Uptime(NSR-Downtime): 22:46:31
    '''}

    def test_show_msdp_peer_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpPeer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_peer_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_peer_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpPeer(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_2)


class TestShowMsdpContext(unittest.TestCase):
    """
        Commands:
        show msdp context
        show msdp vrf <vrf> context
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'default': {
                'config': {
                    'allow_encaps_count': 0,
                    'default_peer_address': '0.0.0.0',
                    'maximum_sa': 20000,
                    'originator_address': '150.150.1.1',
                    'originator_interface': 'Loopback150',
                    'sa_holdtime': 150},
                'context_info': {
                    'table_count': {
                        'active': 2,
                        'total': 2},
                    'table_id': '0xe0000000',
                    'vrf_id': '0x60000000'},
                'inheritable_config': {
                    'keepalive_period': 30,
                    'maximum_sa': 0,
                    'peer_timeout_period': 75,
                    'ttl': 2},
                'mrib_update_counts': {
                    'g_routes': 26,
                    'sg_routes': 447,
                    'total_updates': 473,
                    'with_no_changes': 0},
                'mrib_update_drops': {
                    'auto_rp_address': 2,
                    'invalid_group': 0,
                    'invalid_group_length': 0,
                    'invalid_source': 0},
                'sa_cache': {
                    'external_sas': {
                        'current': 3,
                        'high_water_mark': 3},
                    'groups': {
                        'current': 2,
                        'high_water_mark': 2},
                    'rps': {
                        'current': 3,
                        'high_water_mark': 0},
                    'sources': {
                        'current': 12,
                        'high_water_mark': 12}}}}}

    device_output_1 = {'execute.return_value': '''
        Router# show msdp context

        MSDP context information for default
          VRF ID                     : 0x60000000
          Table ID                   : 0xe0000000
          Table Count (Active/Total) : 2/2
        Inheritable Configuration
          TTL                 : 2
          Maximum SAs         : 0
          Keepalive Period    : 30
          Peer Timeout Period : 75
          Connect Source      : 
          SA Filter In        : 
          SA Filter Out       : 
          RP Filter In        : 
          RP Filter Out       : 
        Configuration
          Originator Address         : 150.150.1.1
          Originator Interface Name  : Loopback150
          Default Peer Address       : 0.0.0.0
          SA Holdtime                : 150
          Allow Encaps Count         : 0
          Context Maximum SAs        : 20000
        SA Cache Counts    (Current/High Water Mark)
          Groups       :          2/2         
          Sources      :         12/12        
          RPs          :          3/0         
          External SAs :          3/3         
        MRIB Update Counts
          Total updates        : 473
          With no changes      : 0
          (*,G) routes         : 26
          (S,G) routes         : 447
        MRIB Update Drops
          Invalid group        : 0
          Invalid group length : 0
          Invalid source       : 0
          Auto-RP Address      : 2
'''}

    expected_output_2 = {
        'vrf': {
            'VRF1': {
                'config': {
                    'allow_encaps_count': 0,
                    'default_peer_address': '0.0.0.0',
                    'maximum_sa': 22222,
                    'originator_address': '22.22.22.23',
                    'originator_interface': 'Loopback3',
                    'sa_holdtime': 150},
                'context_info': {
                    'table_count': {
                        'active': 1,
                        'total': 1},
                    'table_id': '0xe0000011',
                    'vrf_id': '0x60000002'},
                'inheritable_config': {
                    'connect_source': 'Loopback3',
                    'keepalive_period': 30,
                    'maximum_sa': 0,
                    'peer_timeout_period': 75,
                    'sa_filter': {
                        'in': 'safilin',
                        'out': 'safilout'},
                    'ttl': 222},
                'mrib_update_counts': {
                    'g_routes': 0,
                    'sg_routes': 0,
                    'total_updates': 0,
                    'with_no_changes': 0},
                'mrib_update_drops': {
                    'auto_rp_address': 0,
                    'invalid_group': 0,
                    'invalid_group_length': 0,
                    'invalid_source': 0},
                'sa_cache': {
                    'external_sas': {
                        'current': 0,
                        'high_water_mark': 0},
                    'groups': {
                        'current': 0,
                        'high_water_mark': 0},
                    'rps': {
                        'current': 0,
                        'high_water_mark': 0},
                    'sources': {
                        'current': 0,
                        'high_water_mark': 0}}}}}

    device_output_2 = {'execute.return_value': '''
    Router# show msdp vrf VRF1 context

    MSDP context information for VRF1
      VRF ID                     : 0x60000002
      Table ID                   : 0xe0000011
      Table Count (Active/Total) : 1/1
    Inheritable Configuration
      TTL                 : 222
      Maximum SAs         : 0
      Keepalive Period    : 30
      Peer Timeout Period : 75
      Connect Source      : Loopback3
      SA Filter In        : safilin
      SA Filter Out       : safilout
      RP Filter In        : 
      RP Filter Out       : 
    Configuration
      Originator Address         : 22.22.22.23
      Originator Interface Name  : Loopback3
      Default Peer Address       : 0.0.0.0
      SA Holdtime                : 150
      Allow Encaps Count         : 0
      Context Maximum SAs        : 22222
    SA Cache Counts    (Current/High Water Mark)
      Groups       :          0/0         
      Sources      :          0/0         
      RPs          :          0/0         
      External SAs :          0/0         
    MRIB Update Counts
      Total updates        : 0
      With no changes      : 0
      (*,G) routes         : 0
      (S,G) routes         : 0
    MRIB Update Drops
      Invalid group        : 0
      Invalid group length : 0
      Invalid source       : 0
      Auto-RP Address      : 0
    '''}

    def test_show_msdp_context_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpContext(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_context_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpContext(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_context_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpContext(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')

        self.assertEqual(parsed_output, self.expected_output_2)


class TestShowMsdpSummary(unittest.TestCase):
    """
        Commands:
        show msdp summary
        show msdp vrf <vrf> summary
    """
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    expected_output_1 = {
        'vrf': {
            'VRF1': {
                'current_external_active_sa': 0,
                'maximum_external_sa_global': 20000,
                'peer_status': {
                    'address': {
                        '1.1.1.1': {
                            'active_sa_cnt': 0,
                            'as': 0,
                            'cfg_max_ext_sas': 0,
                            'name': 'R1',
                            'reset_count': 0,
                            'state': 'Listen',
                            'tlv': {
                                'receive': 0,
                                'sent': 0,
                            },
                            'uptime_downtime': '18:25:02',
                        },
                        '11.11.11.11': {
                            'active_sa_cnt': 0,
                            'as': 0,
                            'cfg_max_ext_sas': 0,
                            'name': '?',
                            'reset_count': 0,
                            'state': 'Listen',
                            'tlv': {
                                'receive': 0,
                                'sent': 0,
                            },
                            'uptime_downtime': '18:14:53',
                        },
                    },
                },
            },
        },
    }

    device_output_1 = {'execute.return_value': '''
    Router# show msdp summary

    Maximum External SA's Global : 20000
    Current External Active SAs : 0

    MSDP Peer Status Summary
     Peer Address    AS           State    Uptime/   Reset Peer    Active Cfg.Max   TLV
                                           Downtime  Count Name    SA Cnt Ext.SAs recv/sent
     1.1.1.1         0            Listen   18:25:02  0     R1       0      0        0/0
     11.11.11.11     0            Listen   18:14:53  0     ?        0      0        0/0
    '''}

    expected_output_2 = {
        'vrf': {
            'default': {
                'current_external_active_sa': 0,
                'maximum_external_sa_global': 20000,
                'peer_status': {
                    'address': {
                        '4.4.4.4': {
                            'active_sa_cnt': 0,
                            'as': 200,
                            'cfg_max_ext_sas': 444,
                            'name': 'R4',
                            'reset_count': 0,
                            'state': 'Connect',
                            'tlv': {
                                'receive': 0,
                                'sent': 0,
                            },
                            'uptime_downtime': '20:35:48',
                        },
                    },
                },
            },
        },
    }

    device_output_2 = {'execute.return_value': '''
        Fri Jun 16 15:47:02.865 UTC
    Out of Resource Handling Enabled
    Maximum External SA's Global : 20000
    Current External Active SAs : 0
    
    MSDP Peer Status Summary
     Peer Address    AS           State    Uptime/   Reset Peer    Active Cfg.Max   TLV
                                           Downtime  Count Name    SA Cnt Ext.SAs recv/sent
     4.4.4.4         200          Connect  20:35:48  0     R4       0      444      0/0
    '''}
    def test_show_msdp_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMsdpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_msdp_summary_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowMsdpSummary(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.expected_output_1)

    def test_show_msdp_summary_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowMsdpSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_output_2)


if __name__ == '__main__':
    unittest.main()
