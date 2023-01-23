# TorProxy
A simple Tor proxy that uses the stem library for routing traffic through Tor nodes.

The process of configuring your system to use a proxy will vary depending on the operating system you are using. Here are a few examples of how you can configure your system to use a SOCKS proxy on localhost port 1080 on different operating systems:

Windows:

Open Internet Options from the Control Panel or by typing "inetcpl.cpl" in the Run dialog.
Go to the Connections tab and click the LAN settings button.
Check the "Use a proxy server for your LAN" option and enter "127.0.0.1" for the address and "1080" for the port.
MacOS/Linux:

Open the terminal
export all_proxy="socks5://127.0.0.1:1080"
Firefox:

Open Firefox
Go to Preferences > Network Settings
Select "Manual proxy configuration"
Enter "127.0.0.1" for the SOCKS Host and "1080" for the Port.
Chrome:

Open Chrome
Go to Settings > Advanced > System
Click on "Open proxy settings"
Go to the "Connection" tab and click on "LAN settings"
Check the "Use a proxy server for your LAN" option and enter "127.0.0.1" for the address and "1080" for the port.
