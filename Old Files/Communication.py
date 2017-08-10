# messing around with stuff for WikiProject Research

import csv

#################################################
# Global Variables:
topicFile = 'topic_based.csv'  # file to open data from
bondsFile = 'bonds_based.csv'
ruleFile = 'rule_based.csv'
userCfFile = 'user_cf.csv'
messagesFile = 'messages.csv'
leaderFile = 'leaders.csv'
finalFile = 'final2.csv'

link = '[[https://docs.google.com/forms/d/e/1FAIpQLSelCKeHVbwJTupkELLLVOsiyX8rbKn3YuTYI6eBYt6cSC2xIw/viewform?usp=pp_url&entry.808388777='

delimiter = ','

projectsNew = dict()
projectsLead = dict()


#######################################################







class newcomer:
    @staticmethod
    def topic(infile):
        fil = open(infile, 'r')

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]

            rec_type = 'topic'
            user_text = lst[0]
            user_id = lst[1]
            project = lst[2]
            cos_sim = lst[3]
            pos = lst[4]

            found = project in projectsNew  # if there is already an instance of this project in the dictionary
            if found:
                (total, num_topic, b, c, d) = projectsNew[project]
                num_topic += 1
                total += 1
                projectsNew[project] = (total, num_topic, b, c, d)
            else:
                projectsNew[project] = (1, 1, 0, 0, 0)  # otherwise add to dictionary

            user_name = user_text.replace(' ', '_')
            talk_page = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + user_name + '&action=edit&redlink=1| User Talk Page]];'

            link_end = '&entry.2036239070=' + user_name + '&entry.1509434662| Survey]]'

            new_line = project + delimiter + rec_type + delimiter + user_text + delimiter + user_id + delimiter + talk_page + delimiter + link_end + delimiter + '0' + '\n'

            output.write(new_line)

        fil.close()

    def bonds(self, infile):
        f = open(infile, 'r')

        rec_type = 'bonds'

        titles = f.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        for line in list(f):
            lst = [str(x) for x in line.split(delimiter)]

            user_text = lst[0]
            project = lst[1]
            talks_members = lst[2]
            total_talks = lst[3]
            pos = lst[4]

            found = project in projectsNew
            if found:
                (t, a, b, c, d) = projectsNew[project]
                b += 1
                t += 1
                projectsNew[project] = (t, a, b, c, d)
            else:
                projectsNew[project] = (1, 0, 1, 0, 0)

            user_name = user_text.replace(' ', '_')
            talk_page = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + user_name + '&action=edit&redlink=1| User Talk Page]];'

            link_end = '&entry.2036239070=' + user_name + '&entry.1509434662| Survey]]'

            new_line = project + delimiter + rec_type + delimiter + user_text + delimiter + 'null' + delimiter + talk_page + delimiter + link_end + delimiter + '0' + '\n'

            output.write(new_line)

        f.close()

    @staticmethod
    def rule(infile):
        fil = open(infile, 'r')
        rec_type = 'rule'

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        # will change based on vals in inFile
        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            user_text = lst[0]
            user_id = lst[1]
            project = lst[2]
            total_edits = lst[3]
            pos = lst[4]

            found = project in projectsNew
            if found:
                (t, a, b, c, d) = projectsNew[project]
                c += 1
                t += 1
                projectsNew[project] = (t, a, b, c, d)
            else:
                projectsNew[project] = (1, 0, 0, 1, 0)

            user_name = user_text.replace(' ', '_')

            talk_page = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + user_name + '&action=edit&redlink=1| User Talk Page]];'

            link_end = '&entry.2036239070=' + user_name + '&entry.1509434662| Survey]]'

            new_line = project + delimiter + rec_type + delimiter + user_text + delimiter + user_id + delimiter + talk_page + delimiter + link_end + delimiter + '0' + '\n'

            output.write(new_line)

        fil.close()

    def member(self, infile):
        fil = open(infile, 'r')
        recType = 'userCF'

        titles = fil.readline()
        lst = [str(x) for x in titles.split(delimiter)]

        for line in fil.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            user_text = lst[0]
            user_ID = lst[1]
            project = lst[2]
            sum_score = lst[3]
            pos = lst[4]

            found = project in projectsNew
            if found:
                (t, a, b, c, d) = projectsNew[project]
                d += 1
                t += 1
                projectsNew[project] = (t, a, b, c, d)
            else:
                projectsNew[project] = (1, 0, 0, 0, 1)

            userName = user_text.replace(' ', '_')
            talkPage = '[[https://en.wikipedia.org/w/index.php?title=User_talk:' + userName + '&action=edit&redlink=1| User Talk Page]];'

            linkEnd = '&entry.2036239070=' + userName + '&entry.1509434662| Survey]]'

            newLine = project + delimiter + recType + delimiter + user_text + delimiter + user_ID + delimiter + talkPage + delimiter + linkEnd + delimiter + '0' + '\n'

            output.write(newLine)

        fil.close()


class Leader():
    def expEditor(self, outfile, infile):
        base = open(infile, 'r')
        output = open(outfile, 'a')

        titles = base.readline()
        lst = [str(x) for x in titles.split(',')]

        for line in base.readlines():
            lst = [str(x) for x in line.split(',')]

            project = lst[0]
            n = lst[1]
            name = n.strip('\n')

            found = project in projectsLead
            if found:
                v = projectsLead[project]
                v2 = v + 1
                projectsLead[project] = v2
            else:
                projectsLead[project] = 1

            rec = 'Hello ' + name + 'with the project ' + project + 'Here are some new editors for you to recruit'
            new_line = project + delimiter + name + delimiter + rec + '\n'

            output.write(new_line)

        base.close()
        output.close()


class Final():
    def final(self, mFile, lFile):

        # its gunna be a hot mess, inefficient, and take up a lot of space, but Im putting the whole messages and leaders files in lists, for right now

        messages = []
        mess_file = open(mFile, 'r')
        for line in mess_file.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            messages.append(lst)
        mess_file.close()

        leaders = []
        lead = open(lFile, 'r')
        for line in lead.readlines():
            lst = [str(x) for x in line.split(delimiter)]
            leaders.append(lst)
        lead.close()

        loc = 0
        table_start = '{| class="wikitable sortable"\n |-\n !Name !! Recommendation !! Talk Page !! Survey \n'
        table_end = '|}'

        proj_lst = sorted(projectsLead.keys())
        while loc < len(proj_lst):

            proj = proj_lst[loc]

            if proj in projectsNew:  # if there are newcomers for the curret leader's project
                (total, topic, bond, rule, member) = projectsNew[proj]  # number of newcomers for this project found through each algorithm
                num_leaders = projectsLead[proj]

                # number of newcomers each project lead will get from each algorithm
                num_topic = topic / num_leaders
                if num_topic > 3:
                    num_topic = 3
                num_bond = bond / num_leaders
                if num_bond > 3:
                    num_bond = 3
                num_rule = rule / num_leaders
                if num_rule > 3:
                    num_rule = 3
                num_member = member / num_leaders
                if num_member > 3:
                    num_member = 3

                count1 = 0
                count2 = 0
                count3 = 0
                count4 = 0

                type1 = ''
                type2 = ''
                type3 = ''
                type4 = ''

                i = 0
                j = -1

                while i < len(leaders):
                    lst_line = leaders[i]
                    project = lst_line[0]
                    new_line = ''

                    if project == proj:
                        lead_name = lst_line[1]
                        lead_name = lead_name.replace(' ', '_')
                        while j < len(messages):
                            mess = messages[j]
                            n = mess[6]
                            n = n.strip('\n')
                            j += 1

                            if n == '0' and mess[
                                0] == proj:  # checks if the line has been used, and if the projects match
                                if mess[1] == 'topic' and count1 < num_topic:
                                    survey = link + lead_name + mess[5]  # survey link
                                    survey = survey.strip(' ')
                                    survey = survey.strip('\n')
                                    new_message = '|-\n | ' + mess[2] + ' || ' + mess[1] + ' || ' + mess[
                                        4] + ' || ' + survey + '\n'
                                    count1 += 1
                                    type1 += new_message
                                    mess[6] = '1'
                                    messages[j] = mess
                            elif mess[1] == 'bonds' and count2 < num_bond:
                                survey = link + lead_name + mess[5]  # survey link
                                new_message = '|-\n | ' + mess[2] + ' || ' + mess[1] + ' || ' + mess[
                                    4] + ' || ' + survey + '\n'
                                count2 += 1
                                type2 += new_message
                                mess[6] = '1'
                                messages[j] = mess
                            elif mess[1] == 'rule' and count3 < num_rule:
                                survey = link + lead_name + mess[5]  # survey link
                                new_message = '|-\n | ' + mess[2] + ' || ' + mess[1] + ' || ' + mess[
                                    4] + ' || ' + survey + '\n'
                                count3 += 1
                                type3 += new_message
                                mess[6] = '1'
                                messages[j] = mess
                            elif mess[1] == 'member' and count4 < num_member:
                                survey = link + lead_name + mess[5]  # survey link
                                new_message = '|-\n | ' + mess[2] + ' || ' + mess[1] + ' || ' + mess[
                                    4] + ' || ' + survey + '\n'
                                count4 += 1
                                type4 += new_message
                                mess[6] = '1'
                                messages[j] = mess

                        types = type1 + type2 + type3 + type4
                        table = table_start + types + table_end
                        new_message = lst_line[2] + '\n' + table
                        new_line = lst_line[0] + delimiter + lst_line[1] + delimiter + new_message + delimiter + '\n'
                    final.write(new_line)
                    i += 1
            loc += 1


output = open(messagesFile, 'a')
x = newcomer()
x.topic(topicFile)
#x.bonds(bondsFile)
x.rule(ruleFile)
x.member(userCfFile)
output.close()

y = Leader()
y.expEditor(leaderFile, 'project_leaders.csv')

final = open(finalFile, 'w')
z = Final()
z.final(messagesFile, leaderFile)
final.close()
