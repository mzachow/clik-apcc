#!/usr/bin/env python
import apccapi

c = apccapi.Client()
c.retrieve(
	{
		'jobtype': 'MODEL',
		'dataset': 'MODEL',
		'type': 'HINDCAST',
		'institute': 'BCC',
		'model': 'CSM1.1M',
		'variable': ['prec', 't2m'],
		'yearmonth': ['201909']
	},
	'bcc.zip'
)