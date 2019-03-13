Verification Method:
---
Run end-to-end simulations of the AOS. For each visit, this includes the processing of the intra and extra focal half-chip images, extracting the image stamps with the wavefront sensing stars, running the wavefront sensing software, the state estimator and optical controller, applying the AOS control commands to the system, so that we can run raytracing to create wavefront images and evaluate image quality for the next visit. 

So far the only missing component here is the wavefront sensor image processing pipeline.

Note that with the real system, there is no way to determine contribution to the image quality from the AOS separately.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T328

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-7762/
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-9231/
Proc. SPIE 8444, 84444P (2012)
Proc. SPIE 9150, 91500H(2014)
Proc. SPIE 9911, 991118(2016)
Proc. of SPIE 10705, 107050P (2018)

Input data:
---
* (T&S) Poining history from the Operations Simulator, including summit temperature profile

status |
-|
received|

* (T&S) M1M3 and M2 printthroughs as functions of zenith angle

status |
-|
|

* (T&S) M1M3 and M2 deformations as functions of bulk temperatures and thermal gradients

status |
-|
received|

* (Cam) Camera optics deformations as functions of zenith angle, camera bulk temperature, and camera rotation angle.


status |
-|
received (updates needed if available) |


