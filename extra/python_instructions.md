# Гид по питону на кластере

## /usr/bin/python

Системный питон версии 2.7. Не используется в нашем курсе. Устанавливается вместе с системой и используется во многих скриптах системы или внешних программах.

## /usr/bin/python3

Тоже самое, используется для многих компонентов системы и внешних приложений. 

### Как использовать

Вызов в командной строке `/usr/bin/python3` или `python3`
В программах, в тос числе и hadoop-streaming - `#!/usr/bin/python3`. Однако помните, что пакеты, которые вы установили в своей среде на местер-сервере не становятся доступными на всех узлах кластера! Смотрите ниже про среду conda.

Так как это системный питон, то он содержит только те пакеты, которые нужны приложениям системы, у которых специфические версии. В многопользовательской среде у каждого могут быть свои требуемые пакеты, а так же их версии, зачастую кофликтущие. Поэтому каждый пользователь может устанавливать пакет только в свою собственную домашнюю директорию.

Хороший способ не запутаться в версиях и зависимостфых - работать с виртуальными средами.

### Через virtualenv

Создать новую изолированную среду:

```
$ virtualenv p1
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /data/home/artem.trunov/proj1/p1/bin/python3
Also creating executable in /data/home/artem.trunov/proj1/p1/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
```

создаст среду и папку p1 c подпапками для файлов проекта - это делается один раз.
Каждый раз, когда вы работаете над проектом p1, просто делайте:

```
artem.trunov@master:~$ source p1/bin/activate
(p1) artem.trunov@master:~$ 
```
Заметьте, что название среду появилось в промпте, чтоб вы не забывали о ней.
Ваша среда будет изолирована он системного питона, и в ней можно устанавливать свои пакеты:

`pip install requests`

Когда работа закончена, или надо перейти в другую среду, вызывайте:

`deactivate`

## /opt/anaconda/envs/bd9/bin/python

Питон из дистрибуции анаконды + все пакеты, испольуемые на программе Биг Дата. Установлен на всех узлах кластера. Это важно, так как в вашей среде вы работаете только на master.

### Как использовать

```
artem.trunov@master:$ conda activate bd9
(bd9) artem.trunov@master:$ 
```
и тогда вы можете вызвать интерпретатор в командной строке как просто `python`. Заметьте, что и тут промпт показывает вам, в какой среде вы находитесь.

В программах, в том числе hadoop streaming, испольуйте: `#!/opt/anaconda/envs/bd9/bin/python` Важно использовать полный путь.

Выйти из среды:

`conda deactivate`

### Менеджер пакетов конда

Создать свою среду

```
artem.trunov@master:~$ conda create -n bd9at1 python=3.6 pip 
Solving environment: done

## Package Plan ##

  environment location: /data/home/artem.trunov/.conda/envs/bd9at1

  added / updated specs: 
    - pip
    - python=3.6


The following NEW packages will be INSTALLED:

    ca-certificates: 2018.03.07-0           
    certifi:         2018.8.24-py36_1       
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       8.2.0-hdf63c60_1       
    libstdcxx-ng:    8.2.0-hdf63c60_1       
    ncurses:         6.1-hf484d3e_0         
    openssl:         1.0.2p-h14c3975_0      
    pip:             10.0.1-py36_0          
    python:          3.6.6-hc3d631a_0       
    readline:        7.0-h7b6447c_5         
    setuptools:      40.2.0-py36_0          
    sqlite:          3.24.0-h84994c4_0      
    tk:              8.6.8-hbc83047_0       
    wheel:           0.31.1-py36_0          
    xz:              5.2.4-h14c3975_4       
    zlib:            1.2.11-ha838bed_2      

Proceed ([y]/n)? 
```

После чего новую среду надо активировать:

`conda activate bd9at1`

Установка новых пакетов:

`conda install numpy pandas`

Иногда надо поискать в другом репозитории пакетов:

`conda install -c conda_forge ...`

На худой конец, установить по-старинке, но все равно в пределах вашей среды.

`pip install ...`

## Ссылки

[virtualenv userguide](https://virtualenv.pypa.io/en/stable/userguide/)

[conda user guide](https://conda.io/docs/user-guide/getting-started.html)


