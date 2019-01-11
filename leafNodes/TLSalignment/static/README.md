Verification Method:
---
LTS-206 has requirements on the hexapod positioning resolutions and repeating and non-repeating errors (3.5.16 - 3.5.24 for M2, 3.3.5-3.3.13 for Camera).
After these requirements are verified, further analysis will be done in two ways (1) scale the image quality estimates by the ratio of measured resolution to required resolution (2) multiply optical sensitivity matrix with the measured resolutions. Results from the first test will be used as sanity check. Results from second test will be used as final as-built FWHM.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T327

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-3905/

Input data:
---
o. (T&S) M2 hexapod positioning resolutions and repeating and non-repeating errors
        status: 
o. (T&S) Camera hexapod positioning resolutions and repeating and non-repeating errors
        status: 
