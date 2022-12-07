"""
Advent of Code 2022
"""

with open("input7", "r") as f:
    input = f.read()

root = {}


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.dirs = {}
        self.size = 0
        self.parent = parent

    def add_file(self, file, size):
        self.files.append(file)
        self.size += size
        par = self.parent
        while par:
            par.size += size
            par = par.parent

    def add_dir(self, dir):
        self.dirs[dir] = Dir(dir, self)


root = Dir("/", None)
curr = root

for commands in input.split("$")[1:]:
    lines = commands.split("\n")
    com, *rest = lines[0].strip().split(" ")
    if com == "cd":
        if rest[0] == "/":
            curr = root
        elif rest[0] == "..":
            curr = curr.parent
        else:
            curr = curr.dirs[rest[0]]
    elif com == "ls":
        for line in lines[1:]:
            if line == "":
                continue
            size, file = line.split(" ")
            if size == "dir":
                curr.add_dir(file)
            else:
                curr.add_file(file, int(size))


total_space = 70000000
needed_space = 30000000
space_to_free = needed_space - (total_space - root.size)

sizes = 0
min_dir_size = root.size
q = [root]

while q:
    curr = q.pop(0)
    size = curr.size
    if space_to_free <= size < min_dir_size:
        min_dir_size = size
    if size <= 100000:
        sizes += size
    q = q + (list(curr.dirs.values()))

print("Part 1:", sizes)

print("Part 2:", min_dir_size)
