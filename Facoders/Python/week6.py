s='More'
def students_names(Class_name):
    if Class_name == 'grade_one':
        return list(grade_one.keys())
    if Class_name == 'grade_two':
        return list(grade_two.keys())
    if Class_name =='grade_three':
        return list(grade_three.key())
def student_score(Class_name,student_name):
    if Class_name == 'grade_one':
        if student_name=='Sami':
            return grade_one.get('Sami')
        if student_name=='Ahmad':
            return grade_one.get('Ahmad')
        if student_name=='Faris':
            return grade_one.get('Faris')
        if student_name=='Salem':
            return grade_one.get('Salem')
        if student_name=='Mahmoud':
            return grade_one.get('Mahmoud')
    if Class_name == 'grade_two':
        if student_name=='Lana':
            return grade_two.get('Lana')
        if student_name=='Dina':
            return grade_two.get('Dina')
        if student_name=='Maha':
            return grade_two.get('Maha')
        if student_name=='Abeer':
            return grade_two.get('Abeer')
    if Class_name == 'grade_three':
        if student_name=='Rima':
            return grade_three.get('Rima')
        if student_name=='Tala':
            return grade_three.get('Tala')
        if student_name=='Lamar':
            return grade_three.get('Lamar')
        if student_name=='Rola':
            return grade_three.get('Rola')
        if student_name=='Naya':
            return grade_three.get('Naya')
        if student_name=='Dalal':
            return grade_three.get('Dalal')
        if student_name=='Ola':
            return grade_three.get('Ola')
def students_count(Class_name):
    if Class_name == 'grade_one':
        return len(list(grade_one.keys()))
    if Class_name == 'grade_two':
        return len(list(grade_two.keys()))
    if Class_name == 'grade_three':
        return len(list(grade_three.keys()))
while s=='More':
    n=input("Choose one: students_names, student_score, students_count: ")
    grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
    grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10],'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
    grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10],'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7],'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
    if n=='students_names':
        a=input('Class_name: ')
        print(students_names(a))
        s=input('More or Done: ')
    if n=='student_score':
        a=input('Class_name: ')
        b=input('student_name: ')
        print(student_score(a,b))
        s=input('More or Done: ')
    if n=='students_count':
        a=input('Class_name: ')
        print(students_count(a))
        s=input('More or Done: ')
