import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  


#1. Чтение данных из файлов data.txt и settings.txt
with open('settings.txt', "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype = float)

fig, ax = plt.subplots()

sample_rate = float(tmp[0])
step = float(tmp[1])
n = len(data_array)
duration = n / sample_rate 
T = duration / n #период одного измерения


#2. Данные показаний АЦП уже в вольтах, номера отсчётов переведём в секунды
time = []
for i in range(n):
    time.append(i * T)
time = np.array(time)


#4. Настройки цвета и формы линии, размера и цвета маркеров, частоты отображений маркеров и легенды
ax.plot(time, data_array, color='grey', marker='o', linestyle='solid', linewidth=2, markersize=3, markevery=5, markerfacecolor='green', markeredgecolor='magenta', label='V(t)')
ax.legend()

#5. Задание максимальных и минимальных значений для шкалы
ax.set_xlim(0, n * T + 0.2)
ax.set_ylim(np.min(data_array), np.max(data_array) + 0.1)

#6. Подписи осей
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

#7. Название графика, с настройками его месторасположения и переносом текста на следующую строку, если текст слишком длинный
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", pad=20, wrap=True, loc='center')

#8. Наличие сетки (главной и дополнительной), настройка ее цвета и стиля
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.125))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.grid(which='major', color='grey', linestyle='-', alpha=0.7)
ax.grid(which='minor', color='grey', linestyle='--', alpha=0.4)

#9. Текст с временем зарядки и разрядки
t1 = round(np.argmax(data_array) * T, 2)
t2 = round(n * T - t1, 2)
x1 = np.percentile(time, 60)
y1 = np.percentile(data_array, 30)
x2 = np.percentile(time, 60)
y2 = np.percentile(data_array, 20)
plt.text(x1, y1, "Время заряда = " + str(t1) + " с", fontsize=8, color='black', fontfamily='serif', fontweight='bold')
plt.text(x2, y2, "Время разряда = " + str(t2) + " с", fontsize=8, color='black', fontfamily='serif',  fontweight='bold')

#3. Сохранение графика в файл в формате .svg.
plt.savefig("plot.svg")
