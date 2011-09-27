#SFX Object


class SfxObject:
    """A line of input data from SFX input file, exploded on \t"""
    def __init__(self,d_in):
        self.data = d_in
    def getFillingTitle(self):
        return self.data[0]
    def getFullTitle(self):
        return self.data[1]
    def getIssn(self):
        return self.data[3]
    def getObjId(self):
        return self.data[4]
    def getTargetString(self):
        return self.data[5]
    def getAvailString(self):
        return self.data[6]
    def getEIssn(self):
        return self.data[7]
    def getThreshLocal(self):
        return self.data[16]
    def getThreshGlobal(self):
        return self.data[17]
    def getTargetObjId(self):
        return self.data[19]
    def hasIssn(self):
        if (self.getIssn() != ""):
            return True
        else:
            return False
    def getThresh(self):
        if (self.getThreshLocal() == ""):
            return self.getThreshGlobal()
        else:
            return self.getThreshLocal()
        

    
    def print_all(self):
        print "Filling Title: ",self.getFillingTitle()
        print "Full Title: ",self.getFullTitle()
        print "Availability Text: ",self.getAvailString()
        print "Issn: ",self.getIssn()
        print "ObjectId: ",self.getObjId()
        print "Target String: ",self.getTargetString()
        print "Thresholds (Local):  ",self.getThreshLocal()
        print "Thresholds (Global): ",self.getThreshGlobal()
        print "Target Service Object ID: ",self.getTargetObjId()
        return

#Test

if __name__ == '__main__':
    sto = SfxObject([
            'JOURNAL OF POPULAR CULTURE', #0
            'Journal of Popular Culture', #1
            '', #2
            '0022-3840', #3
            '954925417990', #4
            'EBSCOhost Academic Search Premier', #5
            'Available from 1990. ', #6
            '1540-5931', #7
            'J POP CULT', #8
            'getFullTxt', #9
            '80000702', #10
            '110975953941252', #11
            '', #12
            '', #13
            '', #14
            '', #15
            '', #16
            '$obj->parsedDate(">=",1990,undef,undef)', #17
            '110975947325575', #18
            '110975947325577', #19
            '110975953941252', #20
            'Arts and Humanities - General and Others | Arts and Humanities - Society and Culture', #21
            '', #22
            '', #23
            '', #24
            'Bowling Green State University', #25
            'Bowling Green, Ohio', #26
            '', #27
            'JOURNAL', #28
            'ACTIVE', #29
            '', #30
            '', #31
            '', #32
            'eng', #33
            'Journal of Popular Culture', #34
            '\n' #35
            ])

    sto.print_all()
    if sto.hasIssn():
        print "Has an ISSN!"
    print "Has thresh params: ", sto.getThresh()
