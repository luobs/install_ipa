from appium import webdriver
import time,os,datetime
import argparse

PATH = os.path.expanduser('~/Desktop/IPA/')

Filelist = os.listdir(PATH)
dateIntlist = []
#new ipa
for list in Filelist:
    if len(list)>20:
        dateIntlist.append(int(list.replace('EClite','').replace('-','').replace('_','')))
index = [i for i in range(len(dateIntlist)) if dateIntlist[i] == max(dateIntlist)]
ipaPath = PATH + Filelist[index[0]] +'/EClite.ipa'
print ipaPath

def run_app(udid,port):
    Desired_Capabilities = {
        'platformName':'ios',
        'automationName':'XCUITest',
        'deviceName':'iphone',
        'app':ipaPath,
        'Reset':'True',
        'udid':udid,
        'BundleID':'com.ec.ECLite'
    }
    driver  = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%port,Desired_Capabilities)
    time.sleep(5)
    print 'Install success...'

def xcbuild(options):
    udid = options.udid
    port = options.port

    if udid is None and port is None:
        print 'please input UDID! help="-u xxxxxxx or --udid xxxxxxxx"'
        pass
    elif udid is not None and port is None:
        port = '4723'
        run_app(udid,port)
    elif udid is not None and port is not None:
        run_app(udid,port)
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--udid", help="Build the UDID")
    parser.add_argument("-p", "--port", help="Build the port")
    options = parser.parse_args()
    print "Install App: %s" % (options)
    xcbuild(options)

if __name__ == '__main__':
    main()
