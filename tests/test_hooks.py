"""
@file test_hooks.py
@Description: This is a test script for using the SIYI SDK Python implementation to demonstrate hooks
@Author: Mohamed Abdelkader
@Contact: mohamedashraf123@gmail.com
All rights reserved 2022
"""

import sys
import os
from time import sleep
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from siyi_sdk import SIYISDK, HookType

def pre_send_hook(msg: str):
    print(f"pre_send_hook: Sending message: {msg}")

def post_send_hook(bytes_sent: int):
    print(f"post_send_hook: Sent {bytes_sent} bytes")

def pre_recv_hook():
    print("pre_recv_hook: fired")

def post_recv_hook(data: str, data_len: int, cmd_id: str, seq: int):
    print(f"post_recv_hook: Received message: {data}, data_len: {data_len}, cmd_id: {cmd_id}, seq: {seq}")

def test():
    cam = SIYISDK(server_ip="192.168.144.25", port=37260)
    cam.installHook(HookType.PRE_SEND, pre_send_hook,)
    cam.installHook(HookType.POST_SEND, post_send_hook,)
    cam.installHook(HookType.PRE_RECV, pre_recv_hook,)
    cam.installHook(HookType.POST_RECV, post_recv_hook,)

    if not cam.connect():
        print("No connection ")
        exit(1)

    cam.removeHook(HookType.PRE_SEND, pre_send_hook)
    val = cam.requestCameraEncodingParameters(0)
    sleep(1)
    cam.disconnect()

if __name__ == "__main__":
    test()