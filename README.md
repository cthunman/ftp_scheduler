# ftp_scheduler
simple tool for easy ftp batch scheduling

```
Args:
1: 'FTP' or 'SFTP'
2: host
3: username
4: password
5: port (default is 22)
6: mapping file (for details, open README.md)
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