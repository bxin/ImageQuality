Verification Method:
---
According to Doug Neil (email on 12/17/2018). It is unlikely that we will update the M1M3 thermal FEA.

Need thermal gradient measurements (LTS-89 page 6), in Z, X, Y, and radial directions. 
We shall then reuse earlier FEA results, and scale up the resulting image size based on earlier analysis. 
These need to be used as input to AOS simulations, because the low order deformations will be taken out by the AOS. The difference in AOS output IQ with and without this input will be due to this source.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T317

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-4634/ (initial analysis on thickened back plate)

To help with the understanding of the above document.
page 11.
Initially, the CTE homogeneity was budgeted as 188cm for M1 and 300cm for M3.
There are r0 values, to convert to FWHM, use FWHM = 0.976*wavelength/r0. Wavelength = 500nm.
188cm -> ~51mas, 300cm -> ~19mas (for M3, multiply by 0.6, because the mirror D is smaller)

Adding the above with the initial allocation for thermal (not including CTE): 180cm and 107cm, 
by following (1/r0)^(5/3) = (1/r0_1)^(5/3) + (1/r0_2)^(5/3), we get total of 120cm and 97cm.

Then because the estimate for CTE homogeneity turned out to be smaller than initially budgeted, this made room for strengthening M1M3 back plate. How big is the room? we can have total thermal up to 140cm and 102cm. 

page 12.
According to page 8 and 9, thickening back plate to 1.75" would make the thermal total to be 137cm and 105cm. Right on!

Now, take 250cm from page 8, corresponding FWHM = 40 mas
take 750cm from page 9, corresponding FWHM = 19 mas

https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-6852/ (initial analysis on M1M3 thermal total)

page 22.
M1 estimate maintains 54mas
M3 estimate goes up to 84mas
Note that these are without AOS corrections.

Input data:
---
o. (T&S) M1M3 thermal gradient measurements (LTS-89 page 6), in Z, X, Y, and radial directions.
	status:
o. (T&S) M1M3 thermal FEA results (as presented in Document-6852
        status: pending
