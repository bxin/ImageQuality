Verification Method:
---
use measured values in the Zemax model, reoptimize optical design. Then add one sigma measured uncertainty. Calculate resulting image quality. Subtract in quadrature original design image quality. The radius of curvature and conic errors should also be included in this analysis, since they are not in the "fabrication" part.


JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T319

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-3787/
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-18176/
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-19421/

Input data:
---
* (T&S) M3 position vs M3: vertex separation 

status |
-|
received|

* (T&S) M3 position vs M3: decenter

status |
-|
received|

* (T&S) M3 position vs M3: wedge total indicator run-out (TIR)

status |
-|
received|

