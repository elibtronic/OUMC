#SFX Resolved Object

class SfxResolvedObject:
    """A data object that has an SfxObject in it plus some other stuff\t"""
    def __init__(self,sfx_d_in,r_data_in,date_in):
        self.sfx_data = sfx_d_in
        self.resolved_data = r_data_in
        self.date_resolved = date_in
    def print_all(self):
        print "==== SFX Component: \n\n",self.sfx_data.print_all(),"\n\n"
        print "==== Resolved Data Component: \n\n",self.resolved_data,"\n\n"
        print "==== Date Resolved: \n\n",self.date_resolved,"\n\n"
    def set_resolved_data(self, r_data_in):
        self.resolved_data = r_data_in
    def get_resolved_data(self):
        return self.resolved_data
    def get_sfx_object(self):
        return self.sfx_data

#Test

if __name__ == '__main__':
    import sfx_object
    from datetime import date
    sfxo = sfx_object.SfxObject([
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

    #sfxo.print_all()
    reso = SfxResolvedObject(sfxo,"test",date.today())
    reso.print_all()
    reso.set_resolved_data('Fart Face')
    reso.print_all()
    print "Resolved data: ",reso.get_resolved_data()
    print "SfxObject: ",reso.get_sfx_object()
