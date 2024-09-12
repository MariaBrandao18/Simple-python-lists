# Given a list of student grades = [6.3, 7.5, 9.2, 5.1, 6.8], calculate and display the average grade. Also, display the number of above-average grades (6).

notas = [6.3, 7.5, 9.2, 5.1, 6.8]
media = sum(notas) / len(notas)
print('{:.2f}'.format(media))


contador = 0
for notas in notas:
   if notas >= 6:
       contador += 1
print(contador, 'alunos acima da média')
