#!/usr/bin/env python3
"""
Скрипт для поиска интерфейсов и типов в .ts файлах.
Использование: python find_ts_types.py [каталог]
"""

import os
import re
import sys
from pathlib import Path

ignored_names = [ "Props" ]

def find_ts_files(directory):
    """Рекурсивно находит все .ts файлы в каталоге."""
    ts_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ts'):
                ts_files.append(os.path.join(root, file))
    return ts_files

def extract_interfaces_and_types(file_path):
    """
    Извлекает имена интерфейсов и типов из .ts файла.
    Игнорирует определения в комментариях.
    Возвращает список имен.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"Ошибка чтения {file_path}: {e}", file=sys.stderr)
        return []
    
    # Удаляем комментарии
    content_without_comments = remove_comments(content)
    
    definitions = []
    
    # Паттерны для поиска
    patterns = [
        r'interface\s+(\w+)',      # interface Name
        r'type\s+(\w+)\s*=',       # type Name =
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content_without_comments)
        definitions.extend(matches)
    
    # Удаляем дубликаты, сохраняя порядок
    seen = set()
    unique_definitions = []
    for name in definitions:
        if name not in seen:
            seen.add(name)
            unique_definitions.append(name)
    
    return unique_definitions

def remove_comments(content):
    """
    Удаляет комментарии из TypeScript кода.
    Поддерживает:
    - Однострочные комментарии: // ...
    - Многострочные комментарии: /* ... */
    - JSDoc комментарии: /** ... */
    """
    result = []
    i = 0
    length = len(content)
    
    while i < length:
        # Проверяем начало многострочного комментария
        if i + 1 < length and content[i] == '/' and content[i + 1] == '*':
            # Ищем конец комментария */
            end = content.find('*/', i + 2)
            if end == -1:
                # Если конец не найден, пропускаем оставшуюся часть
                break
            i = end + 2
            continue
        
        # Проверяем начало однострочного комментария
        elif i + 1 < length and content[i] == '/' and content[i + 1] == '/':
            # Ищем конец строки
            end = content.find('\n', i + 2)
            if end == -1:
                # Если конец строки не найден, пропускаем оставшуюся часть
                break
            i = end + 1
            continue
        
        # Обычный текст
        else:
            result.append(content[i])
            i += 1
    
    return ''.join(result)

def list_types(base_dir = None):
    # Определяем каталог для поиска
    if base_dir is None:
        base_dir = os.getcwd()
    
    # Проверяем, что каталог существует
    if not os.path.isdir(base_dir):
        print(f"Error: [{base_dir}] is not a directory", file=sys.stderr)
        sys.exit(1)
    
    # Находим все .ts файлы
    ts_files = find_ts_files(base_dir)
    
    if not ts_files:
        print("There's no .ts files")
        return
    
    # Обрабатываем каждый файл
    results = {}  # Используем словарь: файл -> список типов
    for file_path in ts_files:
        # Получаем относительный путь
        rel_path = os.path.relpath(file_path, base_dir)
        
        # Извлекаем определения
        definitions = extract_interfaces_and_types(file_path)
        
        if definitions:
            # Сортируем определения по алфавиту
            results[rel_path] = sorted(definitions)    

    # Выводим результаты
    if results:
        for rel_path, definitions in sorted(results.items()):
            print(f"{rel_path}:")
            for name in definitions:
                print(f"  {name}")
            print()  # Пустая строка между файлами
    else:
        print("Definitions are not found")

if __name__ == "__main__":
    list_types(sys.argv[1])

