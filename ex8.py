# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter, formatter)
print formatter % (
	"line1",
	"line2",
	"line3",
	"line4"
)

print "%r ~ %s" % ("ÄãºÃ","ÄãºÃ")

