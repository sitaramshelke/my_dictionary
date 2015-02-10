#!/usr/bin/env python
import urllib2
import sys
from PyQt4 import QtGui,QtCore
def getword():
    def find_start(h, sstring, estring):
        substr = sstring
        index_of_start = html.find(substr)
        newsubstr = html[index_of_start:index_of_start + 100]
        index_of_end = newsubstr.find(estring)
        substr = newsubstr[:index_of_end - 3]
        return substr

    request = urllib2.Request('http://www.merriam-webster.com/word-of-the-day/')
    response = urllib2.urlopen(request)
    html = response.read()
    # print html

    print find_start(html, "Word of the Day:", ">")
    word = find_start(html, "Word of the Day:", ">")

    substr = "Definition"
    index_of_start = html.find(substr)
    newsubstr = html[index_of_start:index_of_start + 400]
    index_of_start = newsubstr.find("</strong>")
    index_of_end = newsubstr.find("</span>")
    index_of_start += 8
    substr = newsubstr[index_of_start + 2:index_of_end]
    
    meaning = substr

    print "Definition: " + substr
    return word,meaning

def main():
    word,meaning = getword()
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(500, 200)
    w.move(400, 300)
    w.setWindowTitle('Word of the Day')
    w.show()
    
    label = QtGui.QLabel("<b><i><H1>Welcome Sitaram!!<H1></i></b>")
    label.setParent(w)
    label.move(120,20)
    label.show()
    
    
    label1 = QtGui.QLabel("<b>Today's "+word+"</b>")
    label1.setParent(w)
    label1.move(100,60)
    label1.show()
    
    label2 = QtGui.QLabel("Meaning: <i>"+meaning+"</i>")
    label2.setParent(w)
    label2.move(100,90)
    label2.show()
    
    bt = QtGui.QPushButton("Close")
    bt.setParent(w)
    bt.move(200,140)
    bt.show()
    bt.clicked.connect(QtCore.QCoreApplication.instance().quit)
    
    
    sys.exit(app.exec_())   
if __name__ == '__main__':
    main()
