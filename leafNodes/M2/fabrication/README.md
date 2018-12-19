Verification Method:
---

(1) Take interferometrically measured M2 surface map, use it in the Zemax model, look at OPD/PSF/FWHM at GQ fields. 
(2) Synthesize M2 surface map with the swirl feature, use it in the Zemax model, look at OPD/PSF/FWHM at GQ fields.
(3) The IQ impact of the as-built radius of curvature and conic constant are studied with the integrated Zemax model. After system-wide optimization, these are seen to have negligible impact on the IQ. This is demonstrated with
the integrated Zemax model.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T321

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-25305/ (Swirl 1)
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-25347/ (Swirl 2)
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30767/ (interferometrically measured surface)

Test data:
---
Zemax grid file for M2 Swirl: M2_polishing_M2_161109_interp_gridSamp.DAT
Final interferometrically measured surface (from Harris, z in inch): M2_Harris.dat
