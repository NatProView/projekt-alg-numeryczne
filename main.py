def checkIfDuplicates(toCheck):
    if len(toCheck) == len(set(toCheck)):
        return False
    else:
        return True


print("Podaj liczbę naturalną n >= 0")
while(True):
    n = int(input())
    if n < 0:
        print("Liczba nie spełnia warunku, spróbuj jeszcze raz")
    else:
        m = (n + 1) * 2
        break

n_amount = n + 1
print(f"Podaj (oddzielając spacją) twoje x (powinno być ich {n_amount})")
while(True):
    x_list = input().split(" ")
    if len(x_list) != n_amount:
        print("Podano złą ilość argumentów, spróbuj jeszcze raz")
    elif checkIfDuplicates(x_list):
        print("Twoja lista argumentów zawiera duplikat, spróbuj ponownie")
    else:
        break
    
print(f"Podaj (oddzielając spacją) twoje y (powinno być ich {n_amount})")
while(True):
    y_list = input().split(" ")
    if len(y_list) != n_amount:
        print("Podano złą ilość argumentów, spróbuj jeszcze raz")
    else:
        break


print(f"Podaj (oddzielając spacją) twoje z (powinno być ich {n_amount})")
while(True):
    z_list = input().split(" ")
    if len(z_list) != n_amount:
        print("Podano złą ilość argumentów, spróbuj jeszcze raz")
    else:
        break

print(f"Podaj (oddzielając spacją) twoje t")
while(True):
    t_list = input().split(" ")
    break

x_list = [float(i) for i in x_list]
y_list = [float(i) for i in y_list]
z_list = [float(i) for i in z_list]
t_list = [float(i) for i in t_list]

print(f"Twoje x: {x_list}\nTwoje y: {y_list}\nTwoje z: {z_list}")

m_list = []     # listy pomocnicze
xx_list = []    # listy pomocnicze

for i in range (n_amount):
    m_list.append(y_list[i])
    m_list.append(z_list[i])

for x in x_list:
    xx_list.append(x) #xx_list to lista pomocnicza
    xx_list.append(x)

xx_list = [float(i) for i in xx_list]
m_list = [float(i) for i in m_list]

#iloraz rozniczkowy
def ilorazRoz(x1,x2,y1,y2):
    if x1 == x2:
        iloraz = z_list[x_list.index(x1)]
    else:
        iloraz = (y2-y1)/(x2-x1)
    return iloraz

def piramida(iteration, arguments, results):
    if iteration > m:
        return results
    newArguments = []
    i = 0
    print(f"m = {m}")
    while i < m - iteration -1:
        # print(f"Iteration: {iteration}, i + iteration + 1 = {i + iteration + 1}")
        newArguments.append(ilorazRoz(xx_list[i], \
                                      xx_list[i + iteration + 1], \
                                      arguments[i], \
                                      arguments[i + 1]))
        if i == 0:
            results.append(newArguments[0])
        i += 1
    return piramida(iteration + 1, newArguments, results)

b_list = piramida(0, m_list, [])

print(b_list)


# pierwsza wartosc b_list jest pominieta, poniewaz obliczylismy ją inaczej niz w piramidzie 
# TODO kod który ją dodaje
def wielomian(t):
    i = 0
    o = 0
    result = 0
    temp = 0
    while i < m - 1:
        o = 0
        temp = float(b_list[i])
        while o < i:
            temp *= (t - m_list[o])
            o += 1
        result += temp
        i += 1
    return result


print("Wyniki obliczen wielomianow na podstawie podanych t:")
for t in t_list:
    print(f"t = {t} | wielomian = {wielomian(t)}")