# TODO: nothing

class Label:
    def labelFile(filename):
        ifCount = 0
        lines = open(filename, "r").readlines()
        lines = [line.replace("\n", "") for line in lines]
        labels = []
        for line in range(len(lines)):
            splits = lines[line].split()
            if splits[0] == "if":
                labels.append(["if", line, ifCount])
                ifCount += 1
            elif splits[0] == "endif":
                ifCount -= 1
                labels.append(["endif", line, ifCount])
        return labels
