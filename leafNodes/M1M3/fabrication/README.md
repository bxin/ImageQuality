Verification Method:
---
(1) model M1M3 as-built surface (including interferometrically measured surface and crows' feet), insert into Zemax model to evaluate FWHM at GQ fields 
(2) During M1M3 optical testing, use the active support to apply low order bending modes to optimize the mirror shape. Compare this optimized surface with previous measured surface, and use Zemax to evaluate final image quality impact.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T313

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-17171/

Input data:
---
o. (T&S) M1 polished surface at acceptance: 
	status: received
	M1_finalSurface_2015.fits
o. (T&S) M3 polished surface at acceptance
	status: received
	M3_finalSurface_2015.fits
o. (T&S) M1 as-built radius of curvature
	status: received
o. (T&S) M1 as-built conic constant
        status: received
o. (T&S) M3 as-built radius of curvature 
        status: received
o. (T&S) M3 as-built conic constant
        status: received
o. (T&S) M1 optimized surface as measured in the Mirror Lab
	status:
	
o. (T&S) M3 optimized surface as measured in the Mirror Lab
        status:

