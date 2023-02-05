from scapy.all import sniff, Dot11NDPA, Dot11, raw, bytes_hex, SniffSource, QueueSink, TransformDrain, PipeEngine
from scapy.all import ConsoleSink, sendp, RadioTap, Dot11Beacon, Dot11Elt
from threading import Thread, Timer, Event
import time

IFACE = "wlan0"

# def sniff_handler(pkt):
#     if pkt.haslayer(Dot11NDPA):
#         print(f"name: {pkt[Dot11NDPA].name}"
#               f"\t addr1: {pkt[Dot11].addr1}\t addr2: {pkt[Dot11].addr2}\t addr3: {pkt[Dot11].addr3}")
#         print(bytes_hex(pkt))
#     return pkt


# class TimerThread(Thread):
#     def __init__(self, interval, func, event):
#         Thread.__init__(self)
#         self.stopped = event
#         self.interval = interval
#         self.func = func
#
#     def run(self) -> None:
#         while not self.stopped.wait(self.interval):
#             self.func()
#
#
# def timer_function():
#     print("hello world")


# sniff(iface=IFACE, prn=sniff_handler, filter='type ctl')

# source = SniffSource(iface=IFACE, filter="type ctl")
# queue_sink = QueueSink()
# console_sink = ConsoleSink()
# source > TransformDrain(sniff_handler) > console_sink
# p = PipeEngine(source)
# p.start()
# p.wait_and_stop()

# stop_event = Event()
# t = TimerThread(interval=1, func=timer_function, event=stop_event)
# t.start()
# time.sleep(10)
# stop_event.set()

frame = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff",
                           addr2="00:01:02:03:04:05",
                           addr3="00:01:02:03:04:05") / \
        Dot11Beacon(cap="ESS", timestamp=1) / \
        Dot11Elt(ID="SSID", info="123123123")
sendp(frame, iface="wlan0", loop=1, inter=0.001)
