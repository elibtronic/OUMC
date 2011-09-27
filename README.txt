OUMC
Open
URL
MetaData
Converter
v.0.9

This utility will take an export file from the SFX OpenURL resolver and create an input file
suitable for ingestion into a III ERM product.  This product will work with SFX V.3

Step 1.
  Unpack all files in a directory
  
Step 2.
  Edit settings.py to reflect your SFX settings
  

Step 3.
  Login to SFX Admin
  KBTools -> Export Tool
  Advanced Export Queries
  Select Output Format: TXT
  Submit
  
  It will take a while for the export file to build.  When completed download and copy to the 'data_in' directory of
  OUMC and rename to 'sfx_export.txt'
  
  
Step 4.
   Run resolve.py
   Depending on the amount of data this might take a really long time. For about 50,000 lines of input data this will take about
   3-4 hours to run

Step 5.
   Run finalize.py
   Your final file, ready to loading into the ERM catalogue using the ERM 'Coverage Load' feature will be in the data_done directory
   typically called finished_data.txt
   
   
The software makes uses of a caching mechanism so it will be kinder on your SFX server as it will only make 1 unique SFX request per
title. If you have trouble or suggestions please contact me: tim (dot) ribaric (at) gmail (dot) com
Next version will have a web interface based on webpy and will export MARCXML