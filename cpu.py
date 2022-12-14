#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import pardir, realpath
from sys import path
path.append(realpath(pardir))

from statux.battery import *
from examples._functions import print_txt


if is_present():

    for k, v in battery_info().items():  # Manufacturer, Model and S/N
        print_txt(k, v)

    print_txt("Supply type", supply_type())
    print_txt("Status", status())
    print_txt("Remaining Time", "%s (%s seconds)" % (remaining_time(True), remaining_time()))
    print_txt("Voltage", voltage(), "mV")
    print_txt("Current", current(), "mA")
    print_txt("Charge", charge(), "mAh")
    print_txt("Energy", energy(), "mWh")
    print_txt("Power", power(), "mW")
    print_txt("Capacity", capacity(), "%")
    print_txt("Capacity level", capacity_level())
    print_txt("Wear level", wear_level(), "%")
    print_txt("Chemistry", technology())
    print_txt("Low level", low_level())
    print_txt("Action level", action_level())
    print_txt("Power action", critical_power_action())
    print_txt("AC Adapter Online", ac_adapter_online())

lid = lid_state()
if lid is not None:
    print_txt("Lid state", lid)
