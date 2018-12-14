# ImageQuality

LSST SysEng-approved image quality estimates for the as-built system.

The image quality contribution from each leaf node as in the LSST image quality error budget tree can be found in ./data/*yaml.
These can be looked at using the Notebook iq.ipynb

Detailed information on each leaf node, including how they are estimated, the as-built data that have been used as input, etc., can be found in ./leafNodes/. The README files in the subfolders describe the methodology each leaf node is estimated.

The LSST Project uses JIRA to track the verification activities. If you have an LSST JIRA account, these are the OSS-level Verification Elements:
https://jira.lsstcorp.org/browse/LVV-1537
https://jira.lsstcorp.org/browse/LVV-1538
By following the traceability, you can look at the test scripts for each test case and the execution staus etc.

Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](https://developer.lsst.io/tools/git_lfs.html)
explains how to set up Git LFS for LSST development.
