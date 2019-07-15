def fullJustify(words, maxWidth):
    curr_line = []
    curr_line_width = 0
    lines = []

    for word in words:
        if len(word) + curr_line_width + len(curr_line) > maxWidth:
            # Need to add justified line
            if len(curr_line) - 1 > 0:
                nspaces = len(curr_line) - 1
            else:
                nspaces = 1

            for i in range(maxWidth - curr_line_width):
                curr_line[i % nspaces] += " "

            lines.append("".join(curr_line))

            curr_line = []
            curr_line_width = 0

        curr_line.append(word)
        curr_line_width += len(word)

    last_line = " ".join(curr_line)
    last_line = last_line.strip()
    last_line = last_line + " " * (maxWidth - len(last_line))
    lines.append(last_line)

    return lines

print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
print(fullJustify(words, 20))
