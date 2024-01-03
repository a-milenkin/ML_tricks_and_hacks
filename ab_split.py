def get_ab_group(user_id, context="@datafeeling", n_groups=2, salt_seed="10.01.2024", seed=42):
    """Генерируем группу для аб"""

    # Группа зависит от user_id, контекста и группы эксперимента (она же соль)
    string = f"{user_id}_{context}_{salt_seed}"
    
    # Превращаем строку в число с помощью хэш функции
    # Результат превращем в номер группы делением на число групп
    groupid = mmh3.hash128(string, 42, False) % n_groups

    # Для удобства 0 будет контроль
    # Для безопасности по умолчанию контроль
    client_group = "control"
    
    # Меняем группу, если выпала тестовая группа
    if groupid != 0: 
        client_group = f"test_{groupid}"

    return client_group
