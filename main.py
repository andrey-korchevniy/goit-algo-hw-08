import heapq

def minimize_connection_cost(lengths):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(lengths)
    total_cost = 0

    # Виконуємо процес поки не залишиться один кабель
    while len(lengths) > 1:
        # Виймаємо два найменших кабелі
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Об'єднуємо їх і додаємо витрати
        new_length = first + second
        total_cost += new_length

        # Вставляємо новий кабель назад до купи
        heapq.heappush(lengths, new_length)

    return total_cost


cable_lengths = [5, 4, 2, 8, 6]
print("Мінімальні витрати на об'єднання кабелів:", minimize_connection_cost(cable_lengths))