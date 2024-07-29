def panel_karbar():
    print('1. Admin')
    print('2. Karmand ghatar')
    print('3. karbar addi')
    print('4. khorooj as system')
    mogheiat_karbar = input('no karbari khod ra moshakhas konid: ')
    if mogheiat_karbar == '1':
        vorood_admin()
        panel_karbar()
    elif mogheiat_karbar == '2':
        vorood_karmand_ghatar()
        panel_karbar()
    elif mogheiat_karbar == '3':
        vorood_karbar_addi()
        panel_karbar()
    elif mogheiat_karbar not in ['1', '2', '3', '4']:
        print('lotfa gozine sahih ra vared konid')
        panel_karbar()
    else:
        print('as system kharej shodid, khoda negahdar')
def vorood_admin():
    user_name = input("lotfa name karbari khod ra vared namaeed: ")
    ramze_oboor = input("lotfa name ramze obore khod ra vared namaeed: ")
    if user_name == 'Mohamadreza' and ramze_oboor == 'Mizbani':
        mohamadreza.panel_modiriat()
    else:
        print('lotfa name karbari va ramze obor ra be tor sahih vared konid!')
        vorood_admin()


def vorood_karmand_ghatar():
    pass


def vorood_karbar_addi():
    pass


panel_karbar()