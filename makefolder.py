import os

subdirlist = ['smov4/', 'cycle17/', 'cycle18/', 'cycle19/', 'cycle20/', 'cycle21/', 'cycle22/', 'cycle23/']

nums = ['7','13','17','23','27','33','37','43','47','53','57']

#for sub in subdirlist:
#    for num in nums:
#        os.system('mkdir /user/esnyder/'+ sub + num)

for sub in subdirlist:
    #if sub != 'cycle23/':
    #    os.system('mkdir /user/esnyder/' + sub + 'cals')
    os.system('mv /user/esnyder/' + sub + '*_corrtag*.fits /user/esnyder/' + sub + 'cals/')
    os.system('mv /user/esnyder/' + sub + '*_lampflash*.fits /user/esnyder/' + sub + 'cals/')
    os.system('mv /user/esnyder/' + sub + '*_flt*.fits /user/esnyder/' + sub + 'cals/')
