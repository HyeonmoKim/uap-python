#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ua_parser import user_agent_parser
import pprint
import csv


file_path = '/home/henry/workspace/python/ua-parser/data/sampledata.txt'
ua =[]
os_device =[]

def list_append(list,element):
	list.append(element)

def ua_part_filter(col11):
	c

def import_data(file_name):
    with open(file_name,'r') as f:
        temp_reader = csv.reader(f,delimiter='\t')
        ret_list = list(temp_reader)
        return ret_list

#UA정보 입력시 parsed된 정보를 return.
#return 된 정보는 list화.
def ua_parser() :
	pp = pprint.PrettyPrinter(indent=4)
	ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
	parsed_string = user_agent_parser.Parse(ua_string)
	pp.pprint(parsed_string)

def main():
	data = import_data(file_path)
	for i in range(0,len(data)):
		if(data[i][3]=='PV'):
			list_append(ua,data[i][12])
	print(ua)
	print(len(ua))

main()
