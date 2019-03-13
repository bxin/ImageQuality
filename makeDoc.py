
# We want the list to be in particular order below.
pathlist = [
'./leafNodes/TLS/M1M3/fabrication/README.md',
'./leafNodes/TLS/M1M3/vibration/README.md',
'./leafNodes/TLS/M1M3/gravity/README.md',
'./leafNodes/TLS/M1M3/forceError/README.md',
'./leafNodes/TLS/M1M3/CTEhomogeneity/README.md',
'./leafNodes/TLS/M1M3/thermal/README.md',
'./leafNodes/TLS/M1M3/coating/README.md',
'./leafNodes/TLS/M1M3/M3vsM1/README.md',
'./leafNodes/TLS/M2/fabrication/README.md',
'./leafNodes/TLS/M2/forceError/README.md',
'./leafNodes/TLS/M2/gravity/README.md',
'./leafNodes/TLS/M2/thermal/README.md',
'./leafNodes/TLS/M2/CTEhomogeneity/README.md',
'./leafNodes/TLS/M2/coating/README.md',
'./leafNodes/TLS/TLSalignment/static/README.md',
'./leafNodes/TLS/TLSalignment/AOS/README.md',
'./leafNodes/TLS/TLSdynamic/windBuffeting/README.md',
'./leafNodes/TLS/TLSdynamic/trackingServo/README.md',
'./leafNodes/TLS/TLSdynamic/trackingVibration/README.md',
'./leafNodes/TLS/TLSdynamic/domeSeeing/README.md',
'./leafNodes/TLS/TLSdynamic/focusShift/README.md',
'./leafNodes/Cam/CamOptFab/ROC_TWE_CT_W/README.md',
'./leafNodes/Cam/CamOptFab/indexHomogeneity/README.md',
'./leafNodes/Cam/CamOptFab/asphereDecenter/README.md',
'./leafNodes/Cam/CamOptFab/nullSetup/README.md',
'./leafNodes/Cam/CamAlignment/alignL1L2/README.md',
'./leafNodes/Cam/CamAlignment/align2BFOA/README.md',
'./leafNodes/Cam/FPflatness/README.md',
'./leafNodes/Cam/CamChargeDif/README.md',
'./leafNodes/Cam/CamGravity/correlated/README.md',
'./leafNodes/Cam/CamGravity/uncorrelated/README.md',
'./leafNodes/Cam/CamGravity/stress/README.md',
'./leafNodes/Cam/CamThermal/README.md',
'./leafNodes/Cam/CamPressure/README.md',
'./leafNodes/Cam/CamVibration/README.md']

fid = open('inputDataSummary.md', 'w')
icount = 0
for path_in_str in pathlist:
    # because path is object not string
    # path_in_str = str(path)
    fid.write('--------------%s------------\n' % path_in_str)

    fidr = open(path_in_str)
    isinput = False
    for line in fidr:
        #line = line.strip()
        if isinput:
            fid.write(line)
        if (line.startswith('Input data')):
            isinput = True
    fidr.close()
    icount += 1
    
    #if icount>3:
    #    break

fid.close()

