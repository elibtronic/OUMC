
import string
import urllib2
import xml.dom.minidom
import re
import pickle
from datetime import date
from datetime import timedelta
import time

import sfx_object
import resolved_sfx_object
from settings import *

sfx_lines = 0
xml_calls = 0

data_in = dict()
cache_urls = dict()
data_out = dict()

inFile = open(INPUT_FILE,'r')
outFile = open(OUTPUT_FILE, 'w')
       

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

start_time = time.localtime(time.time())

if(DEBUG >= 1):
    print "Starting OUMC! at:", time.asctime(start_time)

if(DEBUG >= 2):
    print "Building Input File"

#Build input file
for line in inFile:
        Sfx_data_raw = sfx_object.SfxObject(string.split(line, SEP_CHAR))
        if(MUST_ISSN):
            if(Sfx_data_raw.hasIssn()):
                comId = str(Sfx_data_raw.getTargetObjId()) + str(Sfx_data_raw.getObjId())
                data_in[comId] = Sfx_data_raw
                if(DEBUG >= 3):
                    print "."
        else:
            comId = str(Sfx_data_raw.getTargetObjId()) + str(Sfx_data_raw.getObjId())
            data_in[comId] = Sfx_data_raw
            if(DEBUG >= 3):
                print "."
inFile.close()

if(DEBUG >= 3):
    print "Input Data struture\n\n"
    for k in data_in.keys():
        print "key: ",k
        sPrint = data_in.get(k)
        sPrint.print_all()
        print "\n"

if (DEBUG >= 2):
    print "Now checking against cache and resolving"

#Resolve and Cache
#Check cache first, if not then resolve
#fill cache with remainder of stuff
for k in data_in.keys():


    sWorkingLine = data_in.get(k)
    sfx_lines += 1
    currentObjectId = sWorkingLine.getObjId()
    currentTargetService = sWorkingLine.getTargetObjId()
    comId = currentTargetService + currentObjectId
    workingResO = resolved_sfx_object.SfxResolvedObject(sWorkingLine,'no_data',date.today())
    if (DEBUG >= 3):
        print "."
    
    #This is in buffer, if matched remove from cache and build data
    if comId in cache_urls:
        workingResO.set_resolved_data(cache_urls[comId])
        data_out[comId] = workingResO
        del cache_urls[comId]
    else:
        #Not in buffer so write it to final output file
        #Put rest of resolved data into buffer
        dom = xml.dom.minidom.parse(urllib2.urlopen(BASE_URL + QUERY_STRING + currentObjectId))
        xml_calls += 1
        nodes = dom.getElementsByTagName("target")
        for n in range(nodes.length):
            tsi = remove_html_tags(nodes[n].getElementsByTagName("target_service_id").item(0).toxml())
            turl = remove_html_tags(nodes[n].getElementsByTagName("target_url").item(0).toxml())
            #print tsi
            cache_key =  tsi + currentObjectId
            cache_urls[cache_key] = turl
        if cache_key in cache_urls:
            workingResO.set_resolved_data(cache_urls[cache_key])
            del cache_urls[cache_key]
            data_out[comId] = workingResO
        else:
            if(DEBUG >=2):
                print "Unmatched item: ", currentObjectId

#The problem is getting the right object id into the cache and comparing it against the input line!!

if(DEBUG >= 3):
    print "===== Cache Contents ====="
    for k in cache_urls.keys():
        print "key: ",k
        print "url: ",cache_urls.get(k)
        print "\n"
    print "===== Output Dictionary ====="
    for k in data_out.keys():
        sPrint = data_out.get(k)
        sPrint.print_all()

#This is probably enough output about process but hey
if (DEBUG >= 1):
    print "Lines Processed: ",sfx_lines
    print " SFX calls made: ",xml_calls
    print "  Size of cache: ",len(cache_urls)


#Build Output file
pickle.dump(data_out,open(OUTPUT_FILE,"wb"))


if(DEBUG >= 1):
    finish_time = time.localtime(time.time())
    print "OUMC Completed at:",time.asctime(finish_time)

