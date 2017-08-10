#messing around with stuff for WikiProject Research

import csv


inF = 'topic_based.csv'  #file to open data from
delimiter = '**'
projectColumn = 0
outF = 'messages.csv'

tempNew = 'tempNew.csv'
tempLeader = 'tempLeader.csv'





class newComer:
        

    def topic(self, infile):
        fil = open(infile, 'r')

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]


        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            project = lst[projectColumn]
            recType = lst[projectColumn+1]
            editorText = lst[projectColumn +2]
            editorID = lst[projectColumn + 3]
            topN = lst[projectColumn + 4]
            att1 = lst[projectColumn + 5]
            attVal1 = lst[projectColumn + 6]

            talkPage = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + editorText + '&action=edit&redlink=1| User Talk Page]];'

            link = '[[https://docs.google.com/forms/d/e/1FAIpQLSelCKeHVbwJTupkELLLVOsiyX8rbKn3YuTYI6eBYt6cSC2xIw/viewform?usp=pp_url&entry.808388777='
            message = editorText + '; ' + talkPage + '; ' + link

            messageEnd = '&entry.2036239070=' + editorText + '&entry.1509434662| Survey]]'

            newLine = project + '**' + recType + '**' + topN + '**' + editorID + '**' + message + '**' + messageEnd + '\n'
            

            output.write(newLine)

        fil.close()

    def bonds(self, infile):
        fil = open(infile, 'r')

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]


        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            project = lst[projectColumn]
            recType = lst[projectColumn+1]
            editorText = lst[projectColumn +2]
            editorID = lst[projectColumn + 3]
            topN = lst[projectColumn + 4]
            att1 = lst[projectColumn + 5]
            attVal1 = lst[projectColumn + 6]

            talkPage = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + editorText + '&action=edit&redlink=1| User Talk Page]];'

            link = '[[https://docs.google.com/forms/d/e/1FAIpQLSelCKeHVbwJTupkELLLVOsiyX8rbKn3YuTYI6eBYt6cSC2xIw/viewform?usp=pp_url&entry.808388777='
            message = editorText + '; ' + talkPage + '; ' + link

            messageEnd = '&entry.2036239070=' + editorText + '&entry.1509434662| Survey]]'

            newLine = project + '**' + recType + '**' + topN + '**' + editorID + '**' + message + '**' + messageEnd + '\n'
            

            output.write(newLine)

        fil.close()

    def rule(self, infile):
        fil = open(infile, 'r')

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]
        

        #will change based on vals in inFile
        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            project = lst[projectColumn]
            recType = lst[projectColumn+1]
            editorText = lst[projectColumn +2]
            editorID = lst[projectColumn + 3]
            topN = lst[projectColumn + 4]
            att1 = lst[projectColumn + 5]
            attVal1 = lst[projectColumn + 6]

            talkPage = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + editorText + '&action=edit&redlink=1| User Talk Page]];'

            link = '[[https://docs.google.com/forms/d/e/1FAIpQLSelCKeHVbwJTupkELLLVOsiyX8rbKn3YuTYI6eBYt6cSC2xIw/viewform?usp=pp_url&entry.808388777='
            message = editorText + '; ' + talkPage + '; ' + link

            messageEnd = '&entry.2036239070=' + editorText + '&entry.1509434662| Survey]]'

            newLine = project + '**' + recType + '**' + topN + '**' + editorID + '**' + message + '**' + messageEnd + '\n'
            

            output.write(newLine)

        fil.close()
        
    def member(self, infile):
        fil = open(infile, 'r')

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        #the following values read from the infile with change depending on the recType
        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            project = lst[projectColumn]
            recType = lst[projectColumn+1]
            editorText = lst[projectColumn +2]
            editorID = lst[projectColumn + 3]
            topN = lst[projectColumn + 4]
            att1 = lst[projectColumn + 5]
            attVal1 = lst[projectColumn + 6]

            talkPage = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + editorText + '&action=edit&redlink=1| User Talk Page]];'

            link = '[[https://docs.google.com/forms/d/e/1FAIpQLSelCKeHVbwJTupkELLLVOsiyX8rbKn3YuTYI6eBYt6cSC2xIw/viewform?usp=pp_url&entry.808388777='
            message = editorText + '; ' + talkPage + '; ' + link

            messageEnd = '&entry.2036239070=' + editorText + '&entry.1509434662| Survey]]'

            newLine = project + '**' + recType + '**' + topN + '**' + editorID + '**' + message + '**' + messageEnd + '\n'
            

            output.write(newLine)

        fil.close()

class Leader():

    def expEditor(self, outfile, infile):
        base = open(infile, 'r')
        lead = open(outfile, 'a')

        titles = base.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        for line in base.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            project = lst[0]
            n = lst[1]
            name = n.strip('\n')

            rec = 'Hello ' + name + 'with the project ' + project + 'Here are some new editors for you to recruit'
            newLine = project + '**' + name + '**' + rec + '**' + '0' + '\n'

            

            lead.write(newLine)

        base.close()
        lead.close()

#class Final():

#    def final(self, messages, lead):
#        mess = open(messages, 'r')
#        leaders = open(lead, 'r+')
#
#        for line in mess.readlines():
#            lst = [str(x) for x in line.split(delimiter)]
#            project = lst[0]
            
#            leaders = open(lead, 'r+')
#            for leadLine in leaders.readlines():
#               leadLst = [str(x) for x in leadLine.split(delimiter)]
#                leadProject = leadLst[0]
#                if leadProject = project:
#                    st = lst[4] + leadLst[1] + lst[5]
                    
                

        


        
            

        


output = open(outF, 'a')
x = newComer();
x.topic(inF)
x.bonds('bonds_based.csv')
output.close()

y = Leader()
y.expEditor('leaders.csv', 'project_leaders.csv')


