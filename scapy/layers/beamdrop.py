from scapy.packet import Packet, bind_layers, NoPayload, Raw
from scapy.fields import (
    BitField, ByteField, ShortField, ByteEnumField, XShortField
)

BDP_TYPE = {0: "beacon",
            1: "service_desc",
            2: "point_cloud_meta",
            3: "point_cloud_seg",
            4: "point_cloud_eof",
            5: "speedtest_meta",
            6: "speedtest_seg",
            7: "speedtest_eof"}


class BDP(Packet):
    # BeamDrop Packet definition
    name = 'BDP'
    file_desc = [
        ShortField("seq", 0),
        ByteEnumField("type", 0, BDP_TYPE),
        ShortField("len", None),
        XShortField("checksum", None),
    ]


class BDPBeacon(Packet):
    name = "BDP Beacon"


class BDPServiceDesc(Packet):
    name = "BDP Service Description"


class BDPPCMeta(Packet):
    name = "BDP Point Cloud Meta-data"


class BDPPCSegment(Packet):
    name = "BDP Point Cloud Segment"


class BDPPCEOF(Packet):
    name = "BDP Point Cloud End-of-file"


class BDPSpeedtestMeta(Packet):
    name = "BDP Speedtest Metadata"


class BDPSpeedtestSegment(Packet):
    name = "BDP Speedtest Segment"


class BDPSpeedtestEOF(Packet):
    name = "BDP Speedtest End-of-file"


bind_layers(BDP, BDPBeacon, type=0)
bind_layers(BDP, BDPServiceDesc, type=1)
bind_layers(BDP, BDPPCMeta, type=2)
bind_layers(BDP, BDPPCSegment, type=3)
bind_layers(BDP, BDPPCEOF, type=4)
bind_layers(BDP, BDPSpeedtestMeta, type=5)
bind_layers(BDP, BDPSpeedtestSegment, type=6)
bind_layers(BDP, BDPSpeedtestEOF, type=7)
