class Admin:

    def __init__(self, karmandan_ghatar):
        self.list_karmandan = karmandan_ghatar
    def panel_modiriat(self):
        print('1. ezafe kardan karmand ghatar')
        print('2. hazf karmnd ghatar')
        print('3. moshahede list karmandan')
        print('4.khorooj az panel modiriat')
        entekhab_admin = input('lotfa gozine mored nazaretan ra vared konid: ')

        if entekhab_admin == '1':
            self.ezafe_kardan_karmand_ghatar()
            self.panel_modiriat()
        elif entekhab_admin == '2':
            self.hazf_karmand_ghatar()
            self.panel_modiriat()
        elif entekhab_admin == '3':
            self.moshahede_list_karmandan()
            self.panel_modiriat()
        elif entekhab_admin == '4':
            print('as panel modiriat kharej shodid!')
            main.panel_karbar()
        else:
            print('lotfa gozine sahih ra vared konid')
            self.panel_modiriat()

    def ezafe_kardan_karmand_ghatar(self):
        x1 = input("lotfa esme khod ra vared konid: ")
        x2 = input('lotfa famili khod ra vared konid: ')
        x3 = input('lotfa email khod ra vared konid: ')
        x4 = input('lotfa username khod ra vared konid: ')
        x5 = input('lotfa password khod ra vared konid: ')
        m = {'name' : x1, 'family' : x2, 'email' : x3, 'username' : x4, "password" : x5}
        if len(self.list_karmandan == 0):
            self.list_karmandan.append(m)
        else:
            k = True
            for i in self.list_karmandan:
                if i['username'] == x4 or i['email'] == x3:
                    k = False
                    break
            if k == True:
                self.list_karmandan.append(m)
            else:
                print('moshakhasat shoma tekrari ast, lotfa moshakhasat jadid vared konid!')
            self.ezafe_kardan_karmand_ghatar()
    def hazf_karmand_ghatar(self):
        z1 = input('lotfa username ra vared konid: ')
        m = True
        for i in self.list_karmandan:
            if i['username'] == z1:
                self.list_karmandan.drop(i)
                m = False
                break
        if m == True:
            print('lotfa username sahih vared konid')
            self.hazf_karmand_ghatar()
        else:
            print('ba movafaghiat hazf shod')
            self.panel_modiriat()
    def moshahede_list_karmandan(self):
        print(self.list_karmandan)
        self.panel_modiriat()


mohamadreza = Admin([])