# Weekly Challenge: 4th week
# https://programmers.co.kr/learn/courses/30/lessons/84325
def solution(table, languages, preference):
    answer = ''
    map_score = make_map(table)
    top = 0
    for kind in map_score.keys():
        score = map_score[kind]
        current = 0
        for lan, pre in zip(languages, preference):
            current += score.get(lan, 0) * pre
        if top < current:
            answer = kind
            top = current
        elif top == current:
            answer = min(answer, kind)
    return answer


def make_map(table):
    scores = {}
    for line in table:
        row = line.split(" ")
        sco = {}
        for i in range(1, len(row)):
            sco[row[i]] = len(row) - i
        scores[row[0]] = sco
    return scores


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]
    print(solution(table, languages, preference), "HARDWARE")

    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    print(solution(table, languages, preference), "PORTAL")