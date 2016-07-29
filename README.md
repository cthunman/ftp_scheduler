# ftp_scheduler
simple tool for easy ftp batch scheduling

```
Args:
Arg1: 'FTP' or 'SFTP'
Arg2: host
Arg3: username
Arg4: password
Arg5: port (default is 22)
Arg6: mapping file (for details, open README.md)
```

Sample mapping file:

mappings.py
--
```python
'mapping' : {
	'remote_folder' : '/home/username/data_folder/',
	'local_folder' : '/home/username/target_folder/',
	'file_patterns' : ['*.csv', '*.xlsx'],
	'file_list' : ['file1.txt', 'something.pdf'],
}
```