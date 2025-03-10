with open("../Resources/animals.txt", "r") as read_file:
    all_lines = read_file.read().split("\n")
    preserved_names = []
    for index in range(0, len(all_lines)):
        if not len(all_lines[index].split(" ")) > 1 and not len(all_lines[index]) > 5:
            preserved_names.append(all_lines[index])
    output_string = "\n".join(preserved_names)
    with open("../Resources/animals_short.txt", "w") as write_file:
        print(output_string, file=write_file)