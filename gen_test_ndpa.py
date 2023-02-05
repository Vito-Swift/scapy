from scapy.all import Dot11NDPA, Dot11, RadioTap, bytes_hex, raw

ndpa_packet = RadioTap() / \
              Dot11(addr1="e8:4e:06:95:29:24",
                    addr2="e8:4e:06:95:28:cd") / \
              Dot11NDPA(Sounding_Dialog_Token_Number=1)
print(ndpa_packet)
with open("/home/vitowu/Downloads/libroad/libroad/test_ndpa/pkt.bin", 'wb+') as f:
    f.write(raw(ndpa_packet))
