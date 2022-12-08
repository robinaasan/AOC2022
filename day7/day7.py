class Filesystem:
    def __init__(self):
        self.files = Dir("first_dir", 0)
        self.level = 1
        self.files.add_new_dir(Dir("/", self.level, self.files))
        self.curr_dir = self.files
        self.under_100000 = []
        self.answear = 0
        self.delete_candidates = []

    def read_input(self):
        with open('input.txt', 'r', encoding='UTF8') as files_input:
            for line in files_input:
                line = line.strip()
                line_array = line.split(" ")
                if line_array[0] == "$":
                    if line_array[1] == "ls":
                        continue
                    elif line_array[1] == "cd":
                        if line_array[2] == "..": #go back a step
                            self.level -= 1
                            if self.curr_dir.has_parent():
                                self.curr_dir = self.curr_dir.parent
                        else:
                            name_to_cd = line_array[2]
                            self.level += 1
                            if self.curr_dir.children[name_to_cd]:
                                self.curr_dir = self.curr_dir.children[name_to_cd]

                elif line_array[0] == "dir":
                    new_dir = Dir(line_array[1], self.level, self.curr_dir)
                    self.curr_dir.add_new_dir(new_dir)
                else:
                    try:

                        if type(int(line_array[0])) == int:
                            dot_index = line_array[1].find(".")

                            if dot_index != -1:
                                file_type = line_array[1][dot_index + 1: -1] + line_array[1][-1] #example .txt
                            else:
                                file_type = None
                            file_size = int(line_array[0])
                            file_name = line_array[1]

                            the_file = File(file_size, file_name, file_type, self.level, parent=self.curr_dir)
                            self.curr_dir.add_file(the_file)
                            self.curr_dir.sum += the_file.size
                            curr = self.curr_dir
                            while curr.parent is not None:
                                curr.parent.sum += the_file.size
                                curr = curr.parent

                    except ValueError:
                        print(f"The input is not valid!\n{ValueError}")

    def print_file_system(self):
        self.iterate_file_system(self.files)

    def iterate_file_system(self, curr_dict):
        for diir in curr_dict.children.values():
            print(diir)
            if type(diir) == Dir:
                self.iterate_file_system(diir)

    def find_under_value(self, curr_dict, sum=0):
        for diir in curr_dict.children.values():
            if type(diir) is Dir:
                if diir.sum <= 100000:
                    self.under_100000.append(diir)
                    sum += diir.sum
                    self.answear += diir.sum
                self.find_under_value(diir, sum)

    def find_needed_space(self, curr_dir, space_to_delete):
        for diir in curr_dir.children.values():
            if type(diir) is Dir:
                if diir.sum >= space_to_delete:
                    self.delete_candidates.append(diir)
                self.find_needed_space(diir, space_to_delete)


class File:
    def __init__(self, size: int, name: str, file_type: str, level: int, parent=None):
        self.size = size
        self.name = name
        self.file_type = file_type
        self.level = level
        self.parent = parent

    def __str__(self):
        space = '  ' * self.level
        return f"{space}- {self.name} (file, size={self.size})"


class Dir:
    def __init__(self, dir_name: str, level: int, parent=None):
        self.dir_name = dir_name
        self.parent = parent
        self.children = {}
        self.level = level
        self.sum = 0

    def add_new_dir(self, directory):
        self.children[directory.dir_name] = directory

    def add_file(self, file: File):
        self.children[file.name + 'file'] = file #needs + 'f' because the the directory and file cant have the same name

    def has_parent(self):
        return self.parent is not None

    def __str__(self):
        space = '  ' * self.level
        return f"{space}- {self.dir_name} (Dir) sum: {self.sum}"

    def __repr__(self):
        return f"Directory: {self.dir_name}"

if __name__ == '__main__':
    filesystem = Filesystem()
    filesystem.read_input()
    print("Filesystem:")
    filesystem.print_file_system()
    filesystem.find_under_value(filesystem.files)
    print()
    print(f"answear1: {filesystem.answear}")

    space_to_delete = 30000000 - (70000000 - filesystem.files.sum)
    filesystem.find_needed_space(filesystem.files, space_to_delete)

    filesystem.delete_candidates.sort(key=lambda x: x.sum)
    # print(filesystem.delete_candidates)
    print(f"Answear2: delete: {filesystem.delete_candidates[0]}")
