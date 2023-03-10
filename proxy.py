import stem
import time
import os
from stem import Signal
from stem.control import Controller
from stem.util import system

# Connect to the Tor control port
try:
    with Controller.from_port(port = 9051) as controller:
        # Authenticate to the Tor control port
        controller.authenticate()

        # Signal tor to change identity
        controller.signal(Signal.NEWNYM)

        # Start a new SOCKS listener on port 1080
        controller.set_conf('SocksPort', '1080')

        while True:
            # Get the current IP address
            ip_address = system.get_ip()
            print("VPN IP address: " + ip_address)
            # Sleep for 10 seconds
            time.sleep(10)

            # Check if the 'q' key is pressed
            if os.system("read -t 0.1 -n 1 -s key") == ord("q"):
                print("Disconnecting from VPN")
                controller.close()
                break

except Exception as e:
    print("An error occurred: ", e)
    print("Reconnecting to VPN...")
    os.execv(__file__, sys.argv)


# MIT License

# Copyright (c) 2023 Leah

"""Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
