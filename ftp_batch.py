import sys, datetime

def arg_help():
	print 'Missing arguments.'
	print 'Arg1: \'FTP\' or \'SFTP\''
	print 'Arg2: host'
	print 'Arg3: username'
	print 'Arg4: password'
	print 'Arg5: port (default is 22)'
	print 'Arg6: mapping file (for details, open README.md)'

num_args = len(sys.argv)

if num_args == 1:
	arg_help()

elif num_args != 7:
	print 'Check number of arguments.'
	arg_help()


