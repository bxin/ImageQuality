instring$="v3.9bd"

imageSize=2048
# play with this first in GUI, otherwise -3 code makes no sense
imagedelta= 0.10
nFieldEnd=31

nRing=5
nArm=6
nField=nRing*nArm+1
declare armlen, DOUBLE, 1, 5
armlen(1)=0.379
armlen(2)=0.841
armlen(3)=1.237
armlen(4)=1.535
armlen(5)=1.708
sampleAngle=6.283185/nArm   #or 2*ACOS(-1)/nArm
vec3(1)=0
vec4(1)=0
for i=1,nRing,1
    for j=1,nArm,1
    	 vec3(1+(i-1)*nArm+j)=armlen(i)*COSI((j-1)*sampleAngle)
    	 vec4(1+(i-1)*nArm+j)=armlen(i)*SINE((j-1)*sampleAngle)
	 FORMAT 2 INT
	 PRINT "vec3/4(",1+(i-1)*nArm+j,")= ",
	 FORMAT 8.3
	 PRINT vec3(1+(i-1)*nArm+j), " ",  vec4(1+(i-1)*nArm+j)
    NEXT j
    PRINT "-----------"
NEXT i

outputPath$ = $pathname()+"\images\"
nSamp=imageSize/2

   cfgFile$ = $pathname()+"\LSSTv33_1c1w_As_CornerNoComp_x3_gridSag.CFG"
   nSamp=2*nSamp
   nSampZ = INTE(LOGE(nSamp/16)/LOGE(2)+0.1)  #1 for 32, 2 for 64, 3 for 128 
   print "nSampZ = ", nSampZ
   print "using CFG file ", cfgFile$
   MODIFYSETTINGS cfgFile$, WFM_SAMP, nSampZ

for iField=1,nFieldEnd,1
   ! --- do not skip anything
   if 0
   ! --- skip #1,10,20,30
   ! if ((imageSize>2000) & ((iField ==1) | (iField ==10) | (iField ==20) | (iField ==30)))
   ! --- only run on #1,10,20,30
   ! if ((imageSize>2000) & (iField !=1) & (iField !=10) & (iField !=20) & (iField !=30))
      goto 998
   endif
   setsystemproperty 102, 1,vec3(iField)
   setsystemproperty 103, 1,vec4(iField)
   if (iField<10) then format 1 int
   if (iField>=10) & (iField<100) then format 2 int
   if (iField>=100) then format 3 int
   CALLSETSTR 1, outputPath$
   CALLSETDBL 1, nSamp
 
      imgFile$ = instring$+"_fld"+$str(iField)+"_wfm.txt"
      CALLSETSTR 2, imgFile$
      CALLSETSTR 4, cfgFile$
      CALLMACRO sub_create_wfm.ZPL
 
   LABEL 998
next iField
print
LABEL 999
PRINT "Calculations Completed"
