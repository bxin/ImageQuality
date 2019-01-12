Verification Method:
---
Mount: Gemini wind pressure measurements were applied to FE model of the telescope structure. Wind was assumed to be perpendicular to the telescope pointing. Both wind vibration and instance response analyses were performed. Assumed the displacements of all the optical elements to be in phase.

M1M3: Wind PSD was calculated based on the assumptions that wind speed will be controlled below 6m/s, and the M1M3 outer loop being closed at 1Hz. Applying the PSD to FE model of the mirror gives an estimate of the distorted mirror shape. The impact on image quality can then be estimated.

M2: Gemini wind pressure measurements were applied to FE model of M2 to estimated distorted mirror shape. Zemax model was then used to estimate image quality.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T329

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-2424/
SPIE7012, 70120W(2008)
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-2758/
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-10495/
SPIE8449, 844905(2012)

Input data:
---
o. (T&S) Measurements of wind speed, pressure, and structure response at various locations on the mount, M1M3, and M2.
        status: 
o. (T&S) Displacements and shape distortions of M1M3 and M2 due to wind buffeting, derived from instant response analysis using Finite Element Model.
	status:

