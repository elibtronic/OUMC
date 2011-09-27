import string
import pickle
import pprint
import time

import sfx_object
import resolved_sfx_object
import parse_avail_object
from settings import *

start_time = time.localtime(time.time())

if(DEBUG >= 1):
    print "Starting Final Output file build at:", time.asctime(start_time)

inData = dict()

buildFile = open(OUTPUT_FILE,'rb')
finalFile = open(FINAL_FILE,'w')

finalFile.write('TITLE|ISSN|ISBN|START_DATE|END_DATE|PROVIDER|URL|EMBARGO|ENUMCAPTION1|ENUMSTART1|ENUMEND1|ENUMCAPTION2|ENUMSTART2|ENUMEND2\n')
inData = pickle.load(buildFile)

if(DEBUG >= 2):
    print "Building Final Output file with",len(inData),"files"


#Translate into final output files
for i in inData.keys():
    l = ""
    rItem = inData.get(i)
    sItem = rItem.get_sfx_object()
    cItem = parse_avail_object.ParseAvailObject(sItem.getThresh())
    l += sItem.getFullTitle() #Title
    l += ERM_SEP_CHAR
    l += sItem.getIssn() #ISSN
    l += ERM_SEP_CHAR
    l += "" #ISBN
    l += ERM_SEP_CHAR
    l += cItem.get_start_date() #START_DATE
    l += ERM_SEP_CHAR
    l += cItem.get_end_date() #END_DATE
    l += ERM_SEP_CHAR
    l += sItem.getTargetString() #PROVIDER
    l += ERM_SEP_CHAR
    l += str(rItem.get_resolved_data()) #URL
    l += ERM_SEP_CHAR
    l += cItem.get_embargo() #EMBARGO
    l += ERM_SEP_CHAR
    l += cItem.get_enumcaption1() #ENUMCAPTION1
    l += ERM_SEP_CHAR
    l += cItem.get_enumstart1()#ENUMSTART1
    l += ERM_SEP_CHAR
    l += cItem.get_enumend1()#ENUMEND1
    l += ERM_SEP_CHAR
    l += cItem.get_enumcaption2()#ENUMCAP2
    l += ERM_SEP_CHAR
    l += cItem.get_enumstart2() #ENSUMSTART2
    l += ERM_SEP_CHAR
    l += cItem.get_enumend2()#ENUMEND2
    l += ERM_SEP_CHAR
    l += "\n"
    if (DEBUG >= 3):
        print "Writing to output file:\n",l,"\n"
    finalFile.write(l)
    
buildFile.close()
finalFile.close()

if(DEBUG >= 1):
    finish_time = time.localtime(time.time())
    print "OUMC Completed at:",time.asctime(finish_time)
