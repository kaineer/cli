# ingrave

 * check if dotfiles repository is in place
 * put specified script into files/bash/scripts directory
 * modify scripts.yml var file

## Последовательность

 1. Проверить, что dotfiles установлен
```
 $HOME/git/config/dotfiles [1]
 $HOME/git/config/dotfiles/ansible/files/bash/scripts [2]
 $HOME/git/config/dotfiles/ansible/vars/scripts.yml [3]
```
 2. Если тест прошел, копируем скрипт и его подкаталоги в [2]
 3. Добавляем имя скрипта в массив [3] .scripts

## Исключения

Вся внутренняя механика cli

 * install
 * new
 * ingrave
