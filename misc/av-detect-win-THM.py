#!/usr/bin/env python3

import os

def main():

    open_processes = os.popen("""wmic process get name | findstr /v "Name 'System Idle Process' System""").read().strip().replace(" ", "")
    open_processes = open_processes.split("\n")
    status = False
    print("[+] Antivirus check is running...")
    av_check = ["MsMpEng.exe", "AdAwareService.exe", "afwServ.exe", "avguard.exe", "AVGSvc.exe", "bdagent.exe", "BullGuardCore.exe", "ekrn.exe", "fshoster32.exe", "GDScan.exe", 
            "avp.exe", "K7CrvSvc.exe", "McAPExe.exe", "NortonSecurity.exe", "PavFnSvr.exe", "SavService.exe", "EnterpriseService.exe", "WRSA.exe", "ZAPrivacyService.exe"] 
    for process in av_check:
        if process in open_processes:
            print(f"--AV Found: {process}")
            status = True
            break
    if not status:
        print("--AV software is not found!")

if __name__ == "__main__":
    main()
