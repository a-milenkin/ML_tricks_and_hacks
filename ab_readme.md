```

print('Эксперимент воспроизводимый (легко расследовать, эвентов не задваиваются на беке)')
print("Aleron ->", get_ab_group("Aleron", context="утро", n_groups=2))
print("Aleron ->", get_ab_group("Aleron", context="утро", n_groups=2))
print()

print('Контекст меняет группу (Switch-Back тестирование')
print("Aleron + вечер ->", get_ab_group("Aleron", context="вечер", n_groups=2))
print()

print('Число групп можно варировать (A/A и мульти A/B тестирование)')
print("Виктория ->", get_ab_group("Виктория", context="вечер", n_groups=3))
print()

print('Исключаем эффект "памяти" за счет нового разбиения (солим хеш)')
print("Виктор + week_1 ->", get_ab_group("Виктор", context="вечер", salt_seed="week_1", n_groups=2))
print("Виктор + week_4 ->", get_ab_group("Виктор", context="вечер", salt_seed="week_4", n_groups=2))
print()
```

#######################################################################################

Эксперимент воспроизводимый (легко расследовать, эвентов не задваиваются на беке)
Aleron -> test_1
Aleron -> test_1

Контекст меняет группу (Switch-Back тестирование
Aleron + вечер -> control

Число групп можно варировать (A/A и мульти A/B тестирование)
Виктория -> test_2

Исключаем эффект "памяти" за счет нового разбиения (солим хеш)
Виктор + week_1 -> test_1
Виктор + week_4 -> control
