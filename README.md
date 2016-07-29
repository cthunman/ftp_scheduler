# ftp_scheduler
simple tool for easy ftp batch scheduling


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