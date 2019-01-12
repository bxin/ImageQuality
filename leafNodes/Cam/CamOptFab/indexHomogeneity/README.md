Verification Method:
---

For more details, see Document-16782.

To the first order, the glass index inhomogeneity doesn't matter much, because it shows up in the null test as a wavefront error, and therefore gets polished out on the convex surface.

Two analyses have been performed -
1. estimate OPD amplitude using glass specification and thickness. Approximate the spatial variation as a defocus shape, then assume polishing takes out half of the image blur. This gives 6 mas (RMS).
2. put a Zernike on S2 to simulate inhomogeneity, and the same Zernike on S1 to simulated the correction that would be polished into the lens. The two Zernikes have different normalizing radii, the ratio of which is equal to the ratio of the marginal ray heights on the two surfaces as in the testing configuration. In terms of simulating the index variation along the optical axis, this is the worst case, because the changes are localized to the two surfaces. The amplitude of the Zernikes is again estimated using glass specification and thickness. Analysis was repeated for Zernikes up to order 20. In all cases, the image blur in all cases is less than 4 mas (FWHM).

Results are also checked against a research paper on Corning 7980 and NIF blank specifications.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T335

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-16782/

Input data:
---
None

