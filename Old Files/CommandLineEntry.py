import os
import random


class project_based:

    def __init__(self):
        self.table_str = ''  # where the table is being built

        self.header = '! editor_text !! project_edits !! wp_edits !! last_edit !! regstr_time \n'
        self.file_start = '{| class="wikitable sortable"\n |-\n' + header  # begining of the table

        self.delimiter = '**'  # what the csv is seperated by

        self.projects = dict()  # keeps record of all projects
        self.users = dict()  # keeps record of all users that have been recommended, prevents duplicates

        self.total_per_project = 8

        self.file_data = []
        self.files = []

    def input_filename(self):
        from sys import argv
        param1 = argv[0]
        argv.remove(param1)
        self.files = argv


    def input_files(self):
        print('Enter the name(s) of newcomer files')
        something = True
        while something:
            file_name = input('File: ')
            if file_name == '':
                something = False
            else:
                self.files.append(file_name)  # files is a list of all the newcomer files

    def finish(self):
        for key in self.projects:
            project_file_name = key + '.csv'
            project_file = open(project_file_name, 'a')
            project_file.write('|}')
            project_file.close()

    def files_table(self):
        files_lst = self.files
        for file in files_lst:
            f = open(file, 'r')
            f.readline()  # removes titles
            self.file_data += list(f)  # still in string format
            f.close()
        #self.file_data = random.shuffle(self.file_data)  # mixes together all file data points


    def execute(self):


        file_lst = self.file_data
        for line in file_lst:
            lst = [str(x) for x in line.split(self.delimiter)]
            project = lst[0]

            project_file_name = project + '.csv'
            project_file = open(project_file_name, 'a+')

            if project not in self.projects:
                self.projects[project] = 0  # gets added to projects file
                project_file.write(project + '\n' + self.file_start)  # first line gets added to file

            if self.projects[project] < self.total_per_project:  # only adds a new line if there are less than 8 editors already added
                name = lst[1]
                if name not in self.users:  # only adds if this user hasnt been used yet
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

                    new_line = '|-\n | ' + editor_text + ' || ' + project_edits + ' || ' + wp_edits + ' || ' + last_edit + ' || ' + regstr_time + '\n'

                    project_file.write(new_line)
                    self.users[name] = 1
                    self.projects[project] += 1
            project_file.close()


def main():

    table_generator = project_based()
    table_generator.input_filename() #gets files from command line
    table_generator.files_table() #puts data from all tables into one table
    table_generator.execute() #creates the table
    table_generator.finish() #adds table ends and closes files


main()


