import re

def python_count(string):
    line_count = 0
    pattern_1 = r"\bpython\b"
    pattern_2 = r"\bPython\b"
    if re.search(pattern_1, string) or re.search(pattern_2, string):
        line_count += 1
    return line_count

def javascript_count(string):
    line_count = 0
    pattern_3 = r"\bjavascript\b"
    pattern_4 = r"\bJavascript\b"
    pattern_5 = r"\bJavaScript\b"
    if re.search(pattern_3, string) or re.search(pattern_4, string) or re.search(pattern_5, string):
        line_count += 1
    return line_count

def java_count(string):
    line_count = 0
    pattern_6 = r"\bJava\b"
    if re.search(pattern_6, string):
        line_count += 1
    return line_count


def main():
    total_java_count = 0
    total_python_count = 0
    total_javascript_count = 0
    try:
        with open("hacker_news.csv", "r") as file:
            line = file.readline()
            
            for line in file:
                total_python_count = python_count(line)
                total_javascript_count += javascript_count(line)
                total_java_count += java_count(line)
    except FileNotFoundError:
        raise TypeError("Could not open file")
    
    print(f"↓↓Results↓↓")
    print(f"Python: {total_python_count}\nJava:{total_java_count}\nJavascript:{total_javascript_count}")
    
    

if __name__ == "__main__":
    main()