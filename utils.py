import markdown

# Turns contents of a file into string representation
def mdToStr(filename):
    temp = ""
    with open(filename, 'r') as f:
        for line in f:
            temp += str(line)
    return temp

def mdToHtml(filename):
    return markdown.markdown(mdToStr(filename))
