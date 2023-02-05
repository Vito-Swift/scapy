from scapy.all import sniff, Dot11NDPA, Dot11ActionNoAck, Dot11, raw, bytes_hex, SniffSource, QueueSink, TransformDrain, PipeEngine
from scapy.all import ConsoleSink, sendp, RadioTap, Dot11Beacon, Dot11Elt
from threading import Thread, Timer, Event
import time

IFACE = "wlan0"


def sniff_handler(pkt):
    # if pkt.haslayer(Dot11NDPA):
    #     print(f"name: {pkt[Dot11NDPA].name}"
    #           f"\t addr1: {pkt[Dot11].addr1}\t addr2: {pkt[Dot11].addr2}\t addr3: {pkt[Dot11].addr3}")
    #     print(bytes_hex(pkt))
    # /scapy/layers/dot11.py - Dot11ActionNoACK
    if pkt.haslayer(Dot11ActionNoAck):
        print(pkt[Dot11ActionNoAck].CBRF_Mat_Hex)
    return pkt


source = SniffSource(iface=IFACE)
console_sink = ConsoleSink()
source > TransformDrain(sniff_handler) > console_sink
p = PipeEngine(source)
p.start()
p.wait_and_stop()
