
smartphone-movement
===
This demo lets you start recording live smartphone movements in just five minutes with a handful of scripts. Learn more at http://www.princeton.edu/~saha/smartphone-movement/. Extended from Peter Friese's mobile demo (http://www.peterfriese.de/how-to-use-the-gyroscope-of-your-iphone-in-a-mobile-web-app/).

Usage
---

Make the CGI script executable

    chmod +x cgi-bin/ear.py
    
Start the CGIHTTPServer

    python start.py

Open the specified address in your smartphone browser

In a new window, start the client

    python client.py
    
Smartphone movement readings will be printed. For a quick demo of an example interactive application, uncomment the following lines from client.py

    if int(ax) > 15:
        print "\a"
        
Re-running the script should generate a "bump" noise every time you swing your iPhone down like a hammer.