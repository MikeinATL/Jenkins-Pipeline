
#! /usr/bin/env python
#portable os shebang 


import os
import logging
import platform
import sys 
import errno
from time import gmtime, strftime

###################################
# Testing: 
spin_path = '/folk/releng/new_drive/users/mglickma/testing/vxworks/vxworks7/spin/vx20170809170702_vx7-integration'
prod_name = 'vxworks-7'
rel_name = 'vxworks-7-CR0471'
###############################################


# if  len(sys.argv) < 4:
# 	sys.exit(-1)

# else:
# 	# These are the command line arguements
# 	# spin_path -> The path to the blessed release
# 	# prod_name -> Name of the product to be released
# 	# rel_name -> Releases name.
	
	
# 	spin_path = str(sys.argv[1])
print('Spin Path: ', spin_path)
	
# 	prod_name = str(sys.argv[2])
# 	print('Product Name:', prod_name)
	
# 	rel_name = str(sys.argv[3])
# 	print('Release Name: ', rel_name)



print ('The arguments are: ' , str(sys.argv))



#########################################################
# #TESTING
# Pointing to my home directory, will be moved to 
# on the machine this is running on and then copied into the 
# archive directory
#########################################################

# Generate time stamp for log files.
time_stamp = strftime("%Y-%m-%d-%H.%M.%S", gmtime())

#logging_path = releng_archive_path +'/log/'
logging_path = '/Users/melissa/log/'
logging_file = logging_path + time_stamp +'.log'

try:
    os.makedirs(logging_path)
except OSError as e:
    if e.errno is errno.EEXIST:
    	pass
    else:
    	raise
    	sys.exit(-1)


#####################################################
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename=logging_file,
#     filemode='w',
# )
# logging.debug('Start of the program')
# logging.info('Platform: ', platform.platform())
# logging.info('Program is terminating now')
#######################################################


#######################################################
# Verify that the spin directory exists
#######################################################
# if not os.path.isdir(spin_path):
# 	print('Path to spin directory incorrect' , spin_path)
# 	sys.exit(-1)



#######################################################
# Call script to pull location of current
# archive directory from DB and pass it back 
# The path will include up to product name
# Ex: /net/arles2/arles16/released-build-store/vxworks/vxworks-7
# append the <rel_name> and this becomes fully qualified
# path to releng archive location.
#
# #TESTING: this is temp hard coded location 8/15/2017
#######################################################
releng_archive_path = '/folk/releng/new_drive/users/mglickma/testing/archive/vxworks-7/'
releng_archive_path = releng_archive_path + rel_name

print('Archive path: ',releng_archive_path)


#######################################################
# Create the spin/
# rsync the files in spin_path to a local spin/ on 
# releng archive drive
# #TESTING: this is temp hard coded paths
#######################################################
cmd = 'mkdir -p ' + releng_archive_path + '/spin'
print('\nCMD1: ', cmd)


cmd = 'rsync -raLpEt ' + spin_path + ' ' + releng_archive_path + '/spin'
print('\nCMD2: ', cmd)
#os.system(cmd)





#######################################################
# Create the pr/ and release_media/ directories 
#######################################################

cmd = 'mkdir -p ' + releng_archive_path + '/pr'
print('\nCMD3: ', cmd)
#os.system(cmd)

cmd = 'mkdir -p ' + releng_archive_path + '/released_media'
print('\nCMD4: ', cmd)
#os.system(cmd)

#######################################################
# create symbolic links to /pr and released_media
#######################################################
handOff_name = os.listdir(releng_archive_path + '/spin')


cmd = 'ln -s ' + releng_archive_path + '/spin/' + handOff_name[0] + '/* ' + releng_archive_path + '/pr'
print('\nCMD4: ', cmd)
#os.system(cmd)


cmd = 'ln -s ' + releng_archive_path + '/spin/' + handOff_name[0] + '/* ' + releng_archive_path + '/released_media'
print('\nCMD4: ', cmd)
#os.system(cmd)


#######################################################
# Each release can have a list of specific folderes to exclude 
# from various directories.  Ben is creating a script to grab
# these from DB and pass them on to this script.
# this is for testing purposes only 8/15/2017
#######################################################

prod_list_to_exclude = ['VxWorks_NotShipped', 'OEM_workbench']
for item in prod_list_to_exclude:
	cmd = 'rm -rf ' + releng_archive_path + '/pr' + '/' + item
	print('\nCMD5: ', cmd)
	#os.system(cmd)


#######################################################
# Each product has a known list of directories to 
# exclude from pr/ released_media 
# Loop through and remove them from the linked copies 
# from the parent directories.
#######################################################


installer_items = ['installer_profiles', 'bootstrap_installer_core_platform', ]
for item in installer_items:
	cmd = 'rm -rf ' + releng_archive_path + '/released_media' +'/' + item
	print('\nCMD6: ', cmd)
	#os.system(cmd)







