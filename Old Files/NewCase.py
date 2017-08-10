

class project_based:

    header = '! editor_text !! project_edits !! wp_edits !! last_edit !! regstr_time \n'
    table_str = '' #where the table is being built

    file_start = '{| class="wikitable sortable"\n |-\n' + header#begining of the table
    file_end = '|}' #end of the table, to be added after table is finished

    line_end = '\n'  #end of each row
    line_start = '|-\n | ' #start of each row

    delimiter = '**' #what the csv is seperated by

    name_end = '.csv'
    file = 'recommendations_newcomers.csv'

    delimiter = '**'

    projects = dict()
    users = dict()

    def __init__(self):
        f = open(self.file, 'r')
        titles = f.readline()
        lst = [str(x) for x in titles.split(self.delimiter)]

        for line in f.readlines():
            lst = [str(x) for x in line.split(self.delimiter)]
            project = lst[0]
            max = True

            project_file_name ='Projects/' + project + self.name_end
            project_file = open(project_file_name, 'a')

            if project not in self.projects:
                self.projects[project] = 0 #gets added to projects file
                project_file.write(project + '\n' + self.file_start) #first line gets added to file

            if self.projects[project] < 8:  #only adds a new line if there are less than 8 editors already added
                name = lst[1]
                if name not in self.users: #only adds if this user hasnt been used yet
                    talkname = name.replace(' ', '_')
                    user_id = lst[2]
                    first_article = lst[3]
                    project_edits = lst[4]
                    wp_edits = lst[5]
                    last_edit = lst[6]
                    regstr_time = lst[7]
                    regstr_time = regstr_time.strip('\n')
                    rec_type = ''

                    talk_page = '([https://en.wikipedia.org/wiki/User_talk:' + talkname + ' Talk Page])'

                    editor_text = name + ' ' + talk_page

                    new_line = self.line_start + editor_text + ' || ' + project_edits + ' || ' + wp_edits + ' || ' + last_edit + ' || ' + regstr_time + self.line_end

                    project_file.write(new_line)
                    self.users[name] = 1
                    self.projects[project] += 1
                else:
                    print ('multiple ' + name)
            project_file.close()



        for key in self.projects:
            project_file_name ='Projects/' +  key + self.name_end
            project_file = open(project_file_name, 'a')
            project_file.write(self.file_end)
            project_file.close()



        f.close()

x = project_based()
