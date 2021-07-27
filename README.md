# pywebdriver

## Summary

Python Web Services to communicate wih Devices.

The aim of this project is to ease the communication between application and Devices,
providing light WebServices based on Python-Flask libraries. The software can be
installed on a computer or a Raspberry-like device. It is compatible with Linux
distribution.

## Table of Content

- [Features](#features)
  - [Web Page](#feature-a)
  - [Specific WebServices for Odoo](#feature-b)
  - [Generic WebServices using CUP](#feature-c)
- [End-Users / Customers Section](#customers)
- [Contributors](#contributors)
- [Developers Section](#developers)
  - [Installation on Debian/Ubuntu](#install-debian)
  - [Installation on Mac OS X](#install-osx)
  - [Installation on Windows 10](#install-windows)
  - [Browser settings](#browser-settings)
  - [Specific configuration](#specific-configuration)
  - [Development](#development)
  - [Contribute](#contribute)
  - [Localization](#localization)
  - [Other Projects](#other-projects)

# <a name="features"></a>Features

## <a name="feature-a"></a>Web Page

This apps provides a light flask app to:

- know the state of the devices;
- know informations about system;
- test communication with some devices (e.g. send a test message to the customer
  display, print a test ticket, etc...).

## <a name="feature-b"></a>Specific WebServices

The aim of this sub project is to provide WebServices and Web Page to simulate the
behaviour of Odoo Apps (hw_proxy applications & co) to allow Odoo users to use Odoo
Point of Sale with PyWebDriver as a Proxy.

- **Odoo8**:
  - **Printers** :
    - Epson TM-T20
  - **Credit Card Reader**:
    - Ingenico and Sagem credit card readers with Telium Manager version 37783600 or
      superior
    - Ingenico i2200 check reader and writer
  - **Customer Display**:
    - Bixolon BCD-1100
    - Bixolon BCD-1000
    - [Epson OCD300](http://www.aures-support.fr/NEWSITE/ocd300/)
  - **Scale**:
    - TODO : planned by GRAP (Any help welcome);
  - **Barcode Reader**, **Cash Box** :
    - Not Planned
