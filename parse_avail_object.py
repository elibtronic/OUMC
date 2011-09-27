#
# Data Structure that will when passed parse params returns neatly constructed 
# info that can be written directly to output file

import re
import datetime
import calendar
class ParseAvailObject:
    """figures out the appropriate data from Avail text"""


    
    def __init__(self,raw_avail_in):

        self.avail_in = self.strip_punc(raw_avail_in)
        self.enumcaption1 = "Volume"
        self.enumcaption2 = "Issue"
        self.start_date = ""
        self.end_date = ""
        self.embargo = 0
        self.enumstart1 = ""
        self.enumend1 = ""
        self.enumstart2 = ""
        self.enumend2 = ""


        #I'm hoping date is YYYYMMDD
        reso = re.split(" && ",self.avail_in)
        for blob in reso:
            blob = re.sub("\(","",blob)
            blob = re.sub("\)","",blob)
            #print "b",blob
            level2 = re.split(",",blob)
            #print "    level2",level2
            if (level2[0] == '>='):
                self.start_date = level2[1]+"0101"
                self.enumstart1 = level2[2]
                self.enumstart2 = level2[3]
            if (level2[0] == '<='):
                current = datetime.datetime.now()
                if (int(level2[1]) == int(current.year)):
                    maxdays=calendar.monthrange(current.year,current.month)
                    self.end_date = current.strftime("%Y")+current.strftime("%m")+str(maxdays[1])
                else:
                    self.end_date = level2[1]+"1231"
                self.enumend1 = level2[2]
                self.enumend2 = level2[3]
            if (level2[0] == 'timediff>='):
                compo = re.split("(\d)",level2[1])
                if (compo[2] == 'Y') or (compo[2] == 'y'):
                    self.embargo = int(compo[1]) * 365
                if (compo[2] == 'M') or (compo[2] == 'm'):
                    self.embargo = int(compo[1]) * 30
        return

    def strip_punc(self, text_in):
        text_in = re.sub("\'","",text_in)
        text_in = re.sub("\"","",text_in)
        text_in = re.sub("\$obj->","",text_in)
        text_in = re.sub("parsedDate","",text_in)
        return text_in 
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        return self.end_date
    def get_embargo(self):
        return str(self.embargo)
    def get_enumcaption1(self):
        return self.enumcaption1
    def get_enumstart1(self):
        return self.enumstart1
    def get_enumend1(self):
        return self.enumend1
    def get_enumcaption2(self):
        return self.enumcaption2
    def get_enumstart2(self):
        return self.enumstart2
    def get_enumend2(self):
        return self.enumend2
    def get_avail_raw(self):
        return self.avail_in
    def print_all(self):
        print " Avail data in: \n",self.avail_in,"\n"
        print "    start_date: ",self.start_date
        print "      end_date: ",self.end_date
        print "       embargo: ",self.embargo
        print "    enumstart1: ",self.enumstart1
        print "      enumend1: ",self.enumend1
        print "    enumstart2: ",self.enumstart2
        print "      enumend2: ",self.enumend2,"\n"

#Test

if __name__ == '__main__':
    print "Testing Avail Object\n"

    pp_object = ParseAvailObject("$obj->parsedDate(\">=\",1990,undef,undef) && $obj->timediff('>=','1y')")
    pp_object.print_all()
    pp_object = ParseAvailObject("$obj->parsedDate('>=','1995','29','3') && $obj->parsedDate('<=','2005','38','6')")
    pp_object.print_all()
    pp_object = ParseAvailObject("$obj->parsedDate('>=','1967','undef','undef') && $obj->parsedDate('<=','2001','undef','undef')")
    pp_object.print_all()
    pp_object = ParseAvailObject("$obj->parsedDate('>=','1967','1','1') && $obj->parsedDate('<=','1996','30','3')")
    pp_object.print_all()
    pp_object = ParseAvailObject("$obj->parsedDate('>=','1997','30','4')")
    pp_object.print_all()
    pp_object = ParseAvailObject("$obj->parsedDate('<=','2011','30','4')")
    pp_object.print_all()



