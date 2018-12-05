#!/usr/bin/env python3

import socket
import ctypes
import fcntl
import pdb

class FLAGS:
    """封装开启混杂模式需要的数值"""

    # linux/if_ether.h
    ETH_P_ALL = 0x0003  # 所有协议
    ETH_P_IP = 0x0800  # 只处理IP层

    # linux/if.h，混杂模式
    IFF_PROMISC = 0x100
    
    # linux/sockios.h
    SIOCGIFFLAGS = 0x8913  # 获取标记值
    SIOCSIFFLAGS = 0x8914  # 设置标记值

class ifreq(ctypes.Structure):
    """C语言结构体类型"""

    _fields_ = [("ifr_ifrn", ctypes.c_char * 16),
                ("ifr_flags", ctypes.c_short)]

class PromiscuousSocket:
    """核心类

    负责创建一个绑定到当前主机名绑定的网卡上的
    raw socket对象，并设置启动混杂模式。
    """

    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname()) 
        s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,
                          socket.htons(FLAGS.ETH_P_ALL))

        ifr = ifreq()
        # 绑定网卡
        ifr.ifr_ifrn = b"eth0"
        # 获取标记字段的名称
        fcntl.ioctl(s, FLAGS.SIOCGIFFLAGS, ifr)
        # 添加混杂模式的值
        ifr.ifr_flags |= FLAGS.IFF_PROMISC
        # 更新
        fcntl.ioctl(s, FLAGS.SIOCSIFFLAGS, ifr)
        self.ifr = ifr

        # 设置socket的补充选项，使多个socket对象能绑定到相同的地址端口
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("eth0", 0))
        # 设置数据保护IP头部
        # s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # 设置混杂模式
        # s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        self.s = s

    def __enter__(self):
        return self.s

    def __exit__(self, *args, **kwargs):
        # 关闭混杂模式
        self.ifr.ifr_flags ^= FLAGS.IFF_PROMISC
        fcntl.ioctl(self.s, FLAGS.SIOCSIFFLAGS, self.ifr)

def sniffer(count, bufferSize=65565, showPort=False, showRawData=False):
    """使用PromiscuousSocket实例接收数据包，并打印基本信息"""

    with PromiscuousSocket() as s:
        for i in range(count):
            package = s.recvfrom(bufferSize)
            printPacket(package, showPort, showRawData)

def printPacket(package, showPort, showRawData):
    """打印数据包的基本信息"""

    dataIndex = 0
    headerIndex = 1
    ipAddressIndex = 0
    portIndex = 1

    pdb.set_trace()

    print("IP:", package[headerIndex][ipAddressIndex], end=" ")
    if(showPort):
        print("Port:", package[headerIndex][portIndex], end=" ")
    print("")  #换行
    if(showRawData):
        print("Data:", str(package[dataIndex]))

if __name__ == "__main__":
    sniffer(100, showPort=True, showRawData=True)
