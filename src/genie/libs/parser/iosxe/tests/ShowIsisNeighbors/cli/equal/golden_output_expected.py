expected_output = {
    "isis": {
        "null":{
            "neighbors": {
                "2222.22ff.4444": {
                    "type": {
                        "L1": {
                            "interface": "Gi2.415",
                            "ip_address": "10.12.115.2",
                            "state": "INIT",
                            "holdtime": "21",
                            "circuit_id": "2222.22ff.4444.01",
                        },
                        "L2": {
                            "interface": "Gi2.415",
                            "ip_address": "10.12.115.2",
                            "state": "INIT",
                            "holdtime": "20",
                            "circuit_id": "2222.22ff.4444.01",
                        },
                    }
                },
                "R3_nx": {
                    "type": {
                        "L1": {
                            "interface": "Gi3.415",
                            "ip_address": "10.13.115.3",
                            "state": "UP",
                            "holdtime": "21",
                            "circuit_id": "R1_xe.02",
                        },
                        "L2": {
                            "interface": "Gi3.415",
                            "ip_address": "10.13.115.3",
                            "state": "UP",
                            "holdtime": "27",
                            "circuit_id": "R1_xe.02",
                        },
                    }
                },
            }
        }
    }
}
