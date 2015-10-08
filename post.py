#!/usr/bin/python

import xmlrpclib

serverUrl='http://<wp_ip>/xmlrpc.php'
userName='<wp_login>'
password='<wp_password>'

fileName="./post_content.txt"

# Create an object to represent our server.;
server = xmlrpclib.Server(serverUrl);

#Get file contents
f = open(fileName)
lines = f.readlines()
f.close()


#set blog entry content
title="<Entry title>"
content=''.join(lines)
publish=True

postData={'title':title,'description': content }

result = server.metaWeblog.newPost(1, userName,password,postData,publish)
f = open('result.log','a')
f.writelines(lines)
f.close()

