Verification Method:
---

Measure the temperature of the camera body and various optics as much
as we can, using thermal sensors and IR camera. There are some
temperature sensors within the purge system but nothing directly on
any of the optics or optics mount. Detector plane T distribution can
be measured with RTD sensors, assisted by FEA-based intepolation, and
known thermal dependence of the throughput. These knowledge can be
used in two ways (1) scale up IQ estimates based on earlier FEA
analysis and its inputs (2) redo the FEA analysis with updated
model. AOS optimization should be taken into account either by
optimizing camera hexapod only, or optimizing two mirrors and two
hexapods. The latter requires the FEA output to be used as AOS
simulation input.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T345

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/LCA-17/
https://docushare.lsstcorp.org/docushare/dsweb/Get/LCA-283/ (sec. 11.7.9)
https://docushare.lsstcorp.org/docushare/dsweb/Get/LCA-283/ (sec. 11.6.1)
Vincent's email on 8/17/2018

Input data:
---
* (Cam) image quality degradation due to camera thermal effects

status |
-|
| 

