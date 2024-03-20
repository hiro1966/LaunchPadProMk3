import rtmidi
import time
midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
# Print the available ports
port_number = 0
for i, port in enumerate(available_ports):
    print(f"Port {i}: {port}")
    if "LPProMK3" in port:
        print(f"Launchpad found at port {i}")
        port_number=i
        break
# Select the desired port
#port_number = 3  # Replace with the desired port number
midi_out.open_port(port_number)
sysex_message = [240,0,32,41,2,14,14,1,247]  # set Programmer mode
#sysex_message = [240,0,32,41,2,14,14,0,247]  # set Daw mode
midi_out.send_message(sysex_message)


# Send a Control Change message
channel = 0  # Replace with the desired channel number (0-15)
for controller_number in range(110):  # Replace with the desired controller number (0-127)
    value = 1  # Replace with the desired value (0-127)
    cc_message = [176 + channel, controller_number, value]
    midi_out.send_message(cc_message)

# waku1 = list(range(81,88))+ list(range(88,18,-10)) + list(range(18,11,-1)) + list(range(11,81,10))
# waku2 = list(range(72,77))+ list(range(77,27,-10)) + list(range(27,22,-1)) + list(range(22,72,10))
# waku3 = list(range(63,66))+ list(range(66,36,-10)) + list(range(36,33,-1)) + list(range(33,63,10))
# waku4 = [54,55,45,44]
# #waku1 = range(81,88)
# while True:
#     for color in range(0,127,10):
#         t = (127-color) /127 *0.1
#         for pos in waku1:
#             cc_message = [176 + channel, pos, color]
#             midi_out.send_message(cc_message)
#             time.sleep(t)
#         for pos in waku2:
#             cc_message = [176 + channel, pos, color]
#             midi_out.send_message(cc_message)
#             time.sleep(t)
#         for pos in waku3:
#             cc_message = [176 + channel, pos, color]
#             midi_out.send_message(cc_message)
#             time.sleep(t)
#         for pos in waku4:
#             cc_message = [176 + channel, pos, color]
#             midi_out.send_message(cc_message)
#             time.sleep(t)
waku1=[55]
waku2=[45]
waku3=[44]
waku4=[54]
for i in range(7):
    for r in range(i+1):
        p = i+r*10-r
        if p % 10 < 4 and p / 10 <4 :
            #print(p)
            waku1 += [waku1[0]+p]
            waku3 += [waku3[0]-p]
            print (p)
            d =divmod(p,10)
            p = -d[0]*10 + d[1]
            print (p)
            waku2 += [waku2[0]+p]
            waku4 += [waku4[0]-p]
while True:
    for color in range(0,127,10):
        t = (127-color) /127 *0.1
        for i in range(len(waku1)):
            cc_message = [176 + channel, waku1[i], color]
            midi_out.send_message(cc_message)
            cc_message = [176 + channel, waku2[i], color]
            midi_out.send_message(cc_message)
            cc_message = [176 + channel, waku3[i], color]
            midi_out.send_message(cc_message)
            cc_message = [176 + channel, waku4[i], color]
            midi_out.send_message(cc_message)
            time.sleep(t)
