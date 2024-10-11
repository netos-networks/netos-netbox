DEFAULT_USER_PREFERENCES = {
    "ui": {
        "colormode": "light"
    },
    "tables": {
        "ASNTable": {
            "columns": [
                "asn",
                "rir",
                "site_count",
                "provider_count",
                "sites",
                "description"
            ]
        },
        "VRFTable": {
            "columns": [
                "name",
                "rd",
                "description",
                "export_targets",
                "import_targets"
            ]
        },
        "RackTable": {
            "columns": [
                "name",
                "site",
                "location",
                "status",
                "facility_id",
                "role",
                "u_height",
                "device_count",
                "get_utilization"
            ]
        },
        "SiteTable": {
            "columns": [
                "name",
                "status",
                "facility",
                "region",
                "group",
                "description"
            ]
        },
        "VLANTable": {
            "columns": [
                "vid",
                "name",
                "description",
                "site",
                "group",
                "prefixes",
                "status",
                "role",
                "last_updated"
            ]
        },
        "CableTable": {
            "columns": [
                "id",
                "status",
                "type",
                "a_terminations",
                "site_a",
                "device_a",
                "b_terminations",
                "site_b",
                "device_b",
                "cf_Netos_Connection_B_Domain",
                "cf_Netos_Connection_B_Neighbor_Capabilities",
                "cf_Netos_Connection_B_Neighbor_Hostname",
                "last_updated"
            ]
        },
        "DeviceTable": {
            "columns": [
                "name",
                "status",
                "site",
                "location",
                "role",
                "manufacturer",
                "device_type",
                "primary_ip",
                "cf_Netos_Mgmt_IP",
                "tags"
            ]
        },
        "PrefixTable": {
            "columns": [
                "prefix",
                "status",
                "children",
                "vrf",
                "utilization",
                "site",
                "vlan",
                "role",
                "description"
            ]
        },
        "CircuitTable": {
            "columns": [
                "cid",
                "provider",
                "type",
                "status",
                "termination_a",
                "termination_z",
                "description",
                "last_updated",
                "tags"
            ]
        },
        "IPRangeTable": {
            "columns": [
                "start_address",
                "end_address",
                "size",
                "vrf",
                "status",
                "role",
                "description"
            ]
        },
        "ASNRangeTable": {
            "columns": [
                "name",
                "rir",
                "start",
                "end",
                "asn_count",
                "description"
            ]
        },
        "LocationTable": {
            "columns": [
                "name",
                "site",
                "status",
                "rack_count",
                "device_count",
                "description"
            ]
        },
        "AggregateTable": {
            "columns": [
                "prefix",
                "rir",
                "child_count",
                "utilization",
                "date_added",
                "description"
            ]
        },
        "FHRPGroupTable": {
            "columns": [
                "group_id",
                "protocol",
                "name",
                "auth_type",
                "description",
                "ip_addresses",
                "member_count",
                "last_updated"
            ]
        },
        "IPAddressTable": {
            "columns": [
                "address",
                "assigned_object",
                "vrf",
                "status",
                "role",
                "assigned",
                "description",
                "last_updated"
            ]
        },
        "InterfaceTable": {
            "columns": [
                "name",
                "device",
                "enabled",
                "type",
                "description",
                "cf_Netos_Interface_Status",
                "cable",
                "duplex",
                "speed"
            ]
        },
        "DeviceTypeTable": {
            "columns": [
                "model",
                "description",
                "manufacturer",
                "part_number",
                "instance_count",
                "cf_Netos_Standard_Software_Version",
                "tags"
            ]
        },
        "RouteTargetTable": {
            "columns": [
                "name",
                "description"
            ]
        },
        "ManufacturerTable": {
            "columns": [
                "name",
                "devicetype_count",
                "moduletype_count",
                "inventoryitem_count",
                "platform_count",
                "description",
                "tags"
            ]
        },
        "InventoryItemTable": {
            "columns": [
                "name",
                "description",
                "device",
                "role",
                "manufacturer",
                "part_id",
                "serial",
                "tags"
            ]
        }
    },
    "pagination": {
        "per_page": 25,
        "placement": "bottom"
    },
    "data_format": "json"
}