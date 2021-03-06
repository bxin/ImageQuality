Verification Method:
---

point camera at zenith angle 75 deg, and set rotator angle to zero, measure the change in alignment for each optic as compared to zenith pointing. Put this change into Zemax model, then optimize the model by moving camera hexapod. The difference between the resulting image quality and the optical design is the contribution of correlated part of the gravity induced error.

75 deg actually can be any angle between 0 and 90 deg. Alignment-induced errors can be left out of this analysis, assuming system linearity.
Note this is different from the way T&S budget handles off-zenith errors. T&S budget is for zenith, with requirement on off-zenith degradation to be less than 1/sec^0.6. According to LCA-283, LCA-17 used 60 deg zenith angle for requirements on gravity-induced errors (according to LCA-283).
Horizon pointing alignment will also be measured by camera I&T.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T342

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/LCA-283/ (sec. 11.3.3.2)

Input data:
---
* (Cam) change in alignment for each optic at an intermediate zenith angle (nominally 75 deg, but may lie anywhere between 0 and 90 degrees)

status |
-|
|


