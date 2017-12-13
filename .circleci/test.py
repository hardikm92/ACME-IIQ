from StringIO import StringIO

from lxml import etree

dtd = etree.DTD("sailpoint.dtd")
with open('application.xml', 'r') as myfile:
    data=myfile.read().replace('\n', '')
root = etree.XML(data)
print(dtd.validate(root))

print(dtd.error_log.filter_from_errors())
