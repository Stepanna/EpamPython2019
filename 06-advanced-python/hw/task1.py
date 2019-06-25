"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной,
например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import shutil
import os


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.output = []

    def __str__(self, depth=0):
        for item in self.content:
            if os.path.isfile(self.name + '\\' + item):
                if depth-1:
                    self.output.append("| "*(depth-1) + "|-> " + item)
                else:
                    self.output.append("|-> " + item)
            if os.path.isdir(self.name + '\\' + item):
                if depth:
                    if depth-1:
                        self.output.append(
                            "|   "*(depth-1) + "|->" + ' V ' + item)
                    else:
                        self.output.append("|-> V " + item)
                else:
                    self.output.append("V " + item)
                depth += 1
                new_folder = PrintableFolder(self.name+'\\'+item,
                                             os.listdir(self.name+'\\'+item))
                self.output.append(new_folder.__str__(depth))
                depth -= 1
        return '\n'.join(self.output)

    def __contains__(self, item):
        for i in self.content:
            if os.path.isdir(self.name+'\\'+i):
                new_folder = PrintableFolder(
                    self.name+'\\'+i, os.listdir(self.name+'\\'+i))
                return item in new_folder
            if os.path.isfile(self.name+'\\'+i):
                if item.name == i:
                    return True


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '|-> '+self.name


folder1 = PrintableFolder(r'C:\Users\nyna-\Documents\Virtual Machines',
                          os.listdir
                          (r'C:\Users\nyna-\Documents\Virtual Machines'))
print(folder1)

file1 = PrintableFile('QNX-s001.vmdk')
print(file1 in folder1)
