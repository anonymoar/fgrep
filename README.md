# fgrep

Команда fgrep просматривает входные файлы в поиске строк, содержащих заданную цепочку_символов. Если файлы не указаны, используется стандартный ввод (stdin). Каждая успешно сопоставленная строка пишется в стандартный вывод (stdout); если исходных файлов несколько, перед найденной строкой выдается имя файла.

## Examples

```bash
$ python -m fgrep test tests/fixtures/test_file.txt
strtesting2
test
```

### Create virtualenv and install requirements

    make init

### Run autoformat

    make pretty

### Run linters

    make lint

### Run tests

    make test

### Add precommit hook

    make precommit_install
