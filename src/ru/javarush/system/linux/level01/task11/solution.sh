# Создаем папку project с вложенными папками src и docs
mkdir project
mkdir -p project/src
mkdir -p project/docs

# Создаем файл readme.txt в папке docs
touch project/docs/readme.txt

# Копируем файл readme.txt из папки docs в папку src
cp project/docs/readme.txt project/src/readme.txt

# Перемещаем файл readme.txt из папки src в корневую папку project
mv project/src/readme.txt project/readme.txt
