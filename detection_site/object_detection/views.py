from django.shortcuts import render
from .forms import TriangleForm
import math


def triangle_view(request):
    triangle_data = None
    solution_steps = ""


    if 'reset' in request.POST:
        return render(request, 'object_detection/home.html',
                      {'form': TriangleForm(), 'triangle_data': None, 'solution_steps': ""})

    if request.method == 'POST':
        form = TriangleForm(request.POST)

        if form.is_valid():
            cathetus_a = form.cleaned_data.get('cathetus_a')
            cathetus_b = form.cleaned_data.get('cathetus_b')
            hypotenuse = form.cleaned_data.get('hypotenuse')

            # Если оба катета введены
            if cathetus_a is not None and cathetus_b is not None:
                hypotenuse = math.sqrt(cathetus_a ** 2 + cathetus_b ** 2)
                triangle_data = {
                    'cathetus_a': cathetus_a,
                    'cathetus_b': cathetus_b,
                    'hypotenuse': hypotenuse,
                }
                solution_steps = (
                    f"1. Используем теорему Пифагора: c² = a² + b²<br>"
                    f"2. Подставляем значения: c² = {cathetus_a}² + {cathetus_b}²<br>"
                    f"3. Вычисляем: c² = {cathetus_a ** 2} + {cathetus_b ** 2} = {cathetus_a ** 2 + cathetus_b ** 2}<br>"
                    f"4. Находим гипотенузу: c = √({cathetus_a ** 2 + cathetus_b ** 2}) = {hypotenuse:.2f}"
                )


            elif cathetus_a is not None and hypotenuse is not None:
                if hypotenuse > cathetus_a:
                    cathetus_b = math.sqrt(hypotenuse ** 2 - cathetus_a ** 2)
                    triangle_data = {
                        'cathetus_a': cathetus_a,
                        'cathetus_b': cathetus_b,
                        'hypotenuse': hypotenuse,
                    }
                    solution_steps = (
                        f"1. Используем теорему Пифагора: b² = c² - a²<br>"
                        f"2. Подставляем значения: b² = {hypotenuse}² - {cathetus_a}²<br>"
                        f"3. Вычисляем: b² = {hypotenuse ** 2} - {cathetus_a ** 2} = {hypotenuse ** 2 - cathetus_a ** 2}<br>"
                        f"4. Находим второй катет: b = √({hypotenuse ** 2 - cathetus_a ** 2}) = {cathetus_b:.2f}"
                    )
                else:
                    solution_steps = "Ошибка: Гипотенуза должна быть больше катета A."


            elif cathetus_b is not None and hypotenuse is not None:
                if hypotenuse > cathetus_b:
                    cathetus_a = math.sqrt(hypotenuse ** 2 - cathetus_b ** 2)
                    triangle_data = {
                        'cathetus_a': cathetus_a,
                        'cathetus_b': cathetus_b,
                        'hypotenuse': hypotenuse,
                    }
                    solution_steps = (
                        f"1. Используем теорему Пифагора: a² = c² - b²<br>"
                        f"2. Подставляем значения: a² = {hypotenuse}² - {cathetus_b}²<br>"
                        f"3. Вычисляем: a² = {hypotenuse ** 2} - {cathetus_b ** 2} = {hypotenuse ** 2 - cathetus_b ** 2}<br>"
                        f"4. Находим первый катет: a = √({hypotenuse ** 2 - cathetus_b ** 2}) = {cathetus_a:.2f}"
                    )
                else:
                    solution_steps = "Ошибка: Гипотенуза должна быть больше катета B."

    else:
        form = TriangleForm()
    return render(request, 'object_detection/home.html', {'form': form, 'triangle_data': triangle_data, 'solution_steps': solution_steps})
