Verification Method:
---
Need actuator non-repeating force error measurements (LTS-146, 3.3.2.3, 3.3.2.4, 3.3.2.5). We can have some random realizations of the force error map. Multiplying these with mirror influence matrix gives the mirror shapes. Inserting the mirror shapes into the Zemax model gives estimated of IQ at GQ fields.

JIRA test case:
---
https://jira.lsstcorp.org/secure/Tests.jspa#/testCase/LVV-T322

Technical Notes:
---
https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-10847/ (initial analysis)

Input data:
---
o. (T&S) M2 single actuator repeating and non-repeating errors
        status: pending
o. (T&S) M2 commanded forces and applied forces during on-summit testing
        status:

