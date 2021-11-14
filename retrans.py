def Retrans(packet):
    if (packet["TCP"]["seq"]< packet["TCP"]["ack"]):
        print("Retransmisión detectada")
    return packet
    
