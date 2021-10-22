#package handler


#(REPLACEMENT FOR SUDO. SUDO DOES NOT WORK AS WELL. AND IS ABANDONED AND DEPRECATED)
 
import importlib
import os

import time

import requests

OFFICIAL = True # Here so you can't delete the thing that deletes things #

def install(url):
    c = requests.Request("GET", url)
    return c.data


def main(c, a):
    if c == 1:
        print("PKG for KTerminal.\nUse pkg install to begin.\n")
    elif c >= 1:
        if a[1] == "install":

            link_base = "http://github.com/thekaigonzalez/" + a[2]
            link_unixbinutils = "https://raw.githubusercontent.com/thekaigonzalez/KTerminal-PyKernel/master/download/unix-core/" + a[2] + ".py"
            link_base_rawcontentlink = "http://raw.githubusercontent.com/thekaigonzalez/" + a[2]
            link_external = "http://github.com/" + a[2]
            link_external_rawcontentlink = "http://raw.githubusercontent.com/" + a[2] + ""
            request = requests.get(link_base)

            print("Looking for package {}...\n".format(a[2]))
            time.sleep(1 )
            print("reading database for {}\n".format(a[2]))
            time.sleep(0.4)
            if requests.get(link_unixbinutils).status_code == 200:
                print("# installing module from unix-binutil\n")
                re = requests.request('GET', link_unixbinutils)
                u = open('usr/bin/' + link_unixbinutils[link_unixbinutils.rfind('/')+1:len(link_unixbinutils)], 'w')
                u.write(re.text)
                u.close()
            if request.status_code == 200:
                print("module found in verified area, checking for module's name ({}.py)\n ".format(a[2]))
                daak = requests.get(link_base_rawcontentlink + "/master/" + a[2] + ".py")
                if daak.status_code == 200:
                    print("Treating {} as an official module. downloading content. ..\n".format(a[2]))
                    time.sleep(2 )
                    c = requests.request('GET', link_base_rawcontentlink + "/master/" + a[2] + ".py")
                    d = open("usr/bin/" + a[2] + ".py", 'w')
                    d.write("#----------- BEGIN GENERATED LINE --------------#\nOFFICIAL=False\n#---------- END GENERATED LINE ----------#\n\n" + c.text)
                    d.close()
                    print("Success!\n")
                    time.sleep(1 )
                    daak = requests.get(link_base_rawcontentlink + "/master/" + "deps.txt")
                    if daak.status_code == 200:
                        print("installing dependencies for " + a[2] + "\n")
                        time.sleep(2)
                        dep = open('cache-deps.txt', 'w')
                        dep.write(daak.text)
                        dep.close()
                        deps = open('cache-deps.txt', 'r')
                        ar = deps.readlines()
                        for i in ar:
                            os.system('pip3 install ' + i)
                        deps.close()
                        os.rmdir('cache-deps.txt')
                    else:
                        print(a[1] + " does not require any more dependencies. install success\n")

            else:
                print("Failed to find the module in verified space. checking for module as a github repository.\n")
                req = requests.get(link_external)
                if req.status_code == 200:
                    print("Module found as GitHub repository. Installing. . .\n")
                    time.sleep(2 )
                    c = requests.request('GET', link_external_rawcontentlink + "/master/" + a[2] + ".py")
                    d = open("usr/bin/" + a[2] + ".py", 'w')
                    d.write(c.text)
                    d.close()
                    print("Success!\n")
                else:
                    print("module for {} not found.\n".format(a[2]))
        elif a[1] == "-u":
            try:
                if importlib.import_module("usr.bin." + a[2]).OFFICIAL == True:
                    print("get-apt: cannot delete system module\n")
                else:
                    try:
                        print("deleting " + a[2] + "...\n")
                        os.remove("usr/bin/" + a[2] + ".py")
                    except Exception:
                        print("")
            except Exception:
                print("apt-get: cannot delete system module\n")