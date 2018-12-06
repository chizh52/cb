### 20 сентября 2018

Привет и добро пожаловать в учебное пространство! По мере прохождения курса, в этом репозитории будут появляться все необходимые материалы:
* Лабораторные работы и суперачивки — `/labs`. 
* Слайды и презентации с лекций и семинаров, а также другие полезные материалы — `/materials`.

Вы можете склонировать все текущие материалы себе локально с помощью стандартной команды git:

`git clone https://github.com/newprolab/content_bigdata9`

И в дальнейшем синхронизировать обновления:

`git pull`

Либо просто заходить на эту страницу: все обновления будут отражаться в этом README-файле, а github умеет рендерить все нужные нам типы документов.

:warning: Справочная информация:

:heavy_exclamation_mark:[**Важные сайты**](important_sites.md), :arrow_right:[**Как зайти на мастер**](extra/login_to_master.md), :link:[**Настройка прокси**](extra/proxy.md), :snake: [**Питон на кластере**](extra/python_instructions.md)

:chart_with_upwards_trend:[**Оформление проектов**](extra/review-ds.md), :snake:[**Стиль питона**](extra/review-python.md), :wrench:[**Git pull-request HOWTO**](students/README.md)

| :calendar: :video_camera: |:postbox:|:blue_book:|:computer:|:books:|:cake:|
| :-----------| -------:| ------:| -------:|------:|----:|
|Дата/Тема/Видео|Спикер|Презентации|Лабы|Ноутбуки|Доп.|
|**2018-09-20** О программе. Знакомство. Введение в большие данные |[Артем Пичугин](https://www.facebook.com/apichugin)|[О программе «Специалист по большим данным»](materials/2018-09-20_О-программе_Артем-Пичугин.pptx), [Введение в большие данные: MapReduce, Hadoop, YARN](materials/2018-09-20_Введение-в-большие-данные_Артем-Пичугин.pptx) | [lab01](labs/lab01),[решение](solutions/lab01s) | | | 
|**2018-09-22**  [Основы Linux]() |[Никита Силаев]() | [Основы Linux](materials/2018-09-25-Основы_Linux-Никита_Силаев.pdf) || |[Упражнения](extra/2017-09-23_Linux_exercises.pdf) [Команды Shell](extra/2017-09-23_Команды_в_Linux_Никита_Силаев.pdf), [Основы Линукс от Николая Маркова](extra/2018-03-24-Основы_Linux-Николай_Марков.pdf) |
|**2018-09-25**  [Основы Python]() |[Николай Марков]() | [Основы Python Descriptive Analysis](materials/2018-09-26-Основы_Python-Descriptive-analysys-Николай_Марков.pdf) || |[Упражнения](extra/2017-09-26_Python_light_exercises.pdf)  |
|**2018-09-27**  [Map-Reduce]() |[Николай Марков]() | [Приемы и стратегии работы с Map-Reduce](materials/2018-09-27-Приёмы_и_стратегии_работы_с_MR-Nikolay.pdf) || | [статья от Гугл](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf),[Hadoop Streaming manual](http://hadoop.apache.org/docs/r2.8.3/hadoop-streaming/HadoopStreaming.html), [MR Tutorial](http://hadoop.apache.org/docs/r2.8.3/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html), [MR Tutorial Yahoo](https://developer.yahoo.com/hadoop/tutorial/module4.html), [UI для мониторинга Hadoop-джобов на кластере](http://master.cluster-lab.com:8088/cluster) - :warning: - через [прокси](extra/proxy.md), [примеры от Николая](extra/mapreduce_practice) |
|**2018-09-29**  [HDFS]() |[Антон Пилипенко]() | [HDFS](materials/2018-09-29-HDFS_Anton_Pilipenko.pdf) || |  |
|**2018-10-02**  [HBase]() |[Антон Пилипенко]() | [HBase](materials/2018-10-02-Основы_HBASE_Антон_Пилипенко.pdf) | [lab02](labs/lab02), [решение](solutions/lab02), [решение-с](solutoins/lab02s) | | |
|**2018-10-04**  [Python II]() |[Николай Марков]() | [Python II](materials/2018-10-04-Питон_matplotlib_ml_Николай_Марков.pdf) || | [тетрадки и дата](extra/python2_code_data) |
|**2018-10-06**  [Hive]() |[Антон Пилипенко]() | [Hive лекция](materials/2018-10-06-Hive_Pig_Hue_Антон_Пилипенко.pdf) [Hive семинар](materials/2018-10-06_Семинар_Hive_Антон_Пилипенко.pdf) |[lab03](labs/lab03), [решение](solutions/lab03), [решение-s](/solutions/lab03s)| | [Hive SQL cheat-sheet](https://hortonworks.com/blog/hive-cheat-sheet-for-sql-users/) [Продвинутый Hive](https://habrahabr.ru/company/dca/blog/305838/)|
|**2018-10-09**  [Введение в text mining]() |[Петр Ермаков]() | [Введение в text mining](materials/2018-10-09-Введение_в_Text-mining_Петр_Ермаков.pdf) | | [tf-idf.ipynb](extra/tf-idf.ipynb) [zipf.ipynb](extra/zipf.ipynb) | [упражнения](extra/2018-10-09_Text-mining_exercises.pdf) |
|**2018-10-11**  [Парсинг и похожесть текстов]() |[Петр Ермаков]() | | |[2018-10-11_Download_vacancies.ipynb](extra/2018-10-11_Download_vacancies.ipynb), [2018-10-11_Text_mining.ipynb](extra/2018-10-11_Text_mining.ipynb) | [data.pickle](extra/data.pickle) |
|**2018-10-13**  [DMP]() |[Илья Маркин]() |[DMP](materials/2018-10-13_DMP-Markin-Challenges.pdf) || |  |
|**2018-10-16** [Введение в ML]() |[Петр Ермаков]() | [Введение в ML](materials/2018-10-16-Intro_to_ML_Петр_Ермаков.pdf) | [lab04](labs/lab04), [решение](solutions/lab04/lab04_solution.ipynb) | | |
|**2018-10-18**  [Семинар ML]() |[Петр Ермаков]() | || [titanic.ipynb](extra/titanic.ipynb) | [Kaggle Titanic](https://www.kaggle.com/c/titanic) |
|**2018-10-20**  [Семинар ML]() |[Петр Ермаков]() | || | [npl_for_students](https://github.com/ermakovpetr/npl_for_students/) (ml_on_text_bow.ipynb + json data files), [ML workflow](extra/machine_learning_workflow.pdf), [кпражнения 1](extra/2018-10-20-excecises_ML1.pdf), [упражнения 2](extra/2018-10-20-excecises_ML2.pdf) |
|**2018-10-23**  [ML + text mining]() |[Петр Ермаков]() | |  [lab05](labs/lab05), [решение](solutions/lab05), [решение-с](solutions/lab05s) |  |  |
|**2018-10-27**  [Topic modelling]() |[Петр Ермаков]() | || [notebooks, data](https://github.com/ermakovpetr/npl_for_students/) | [упражнения](extra/2018-10-24_Topic_Modeling_exercises.pdf) |
|**2018-10-30**  [Ансимбли и Стэкинг]() |[Кирилл Данилюк]() |[Ансамбли и Стэкинг](materials/2018-10_30_ensemble_learning_kirill_danilyuk.pdf) || |  |
|**2018-11-01**  [Intro to Spark]() |[Павел Клеменков]() | | [lab06](labs/lab06), [решение](solutions/lab06) | [spark01](extra/spark01) | :warning: dataset в HDFS: /share/spark01 |
|**2018-11-03**  [Intro to RS]() |[Андрей Зимовнов]() | [Intro_to_RS](materials/2018-11-03_Intro_to_RS_Andrey_Zimovnov.pdf), [Nonpers. RS](materials/2019-11-03_Nonpers_Rec_Andrey_Zimovnov.pdf) | [project02](project02) | |  |
|**2018-11-06**  [Content Based RS. Collaborative filtering]() |[Андрей Зимовнов]() | [Collaborative](materials/2018-11-06_Коллаборативная_фильтрация_Андрей_Зимовнов.pdf), [Content-based](materials/2018-11-06_Контентные_рекомендации_Андрей_Зимовнов.pdf) | [lab07](labs/lab07), [solution](solutions/lab07) | |  |
|**2018-11-08**  [Spark Dataframe]() |[Павел Клеменков]() |[Catalyst](materials/2018-11-08_Catalyst_Pavel_Klemenkov.pdf) | | [spark02](extra/spark02) | :warning: dataset в HDFS: /share/ml-100k, /share/spark02 |
|**2018-11-10**  [CLI tools and Data Science]() |[Николай Марков]() |[CLI tools](materials/2018-11-10-CLI-tools-Data-science-Николай_Марков.pdf) || | [76-0.txt](/extra/76-0.txt), [imdb.xlsx](extra/imdb-250-1996-2011-lists-only.xlsx) |
|**2018-11-13**  [SVD, BMF]() |[Андрей Зимовнов]() | [Мaтричные факторизации](materials/2018-11-13_Митричные_факторизации.pdf) | [lab08](labs/lab08), [решение](solutions/lab08) | | [упр1](extra/2017-11-21_Упражнения_по_частым_множествам_БЕЗ_ответов_Дима_Игнатов.pptx), [упр2](extra/2017-11-21_Упражнения_по_частым_множествам_БЕЗ_ответов_Дима_Игнатов.pptx), [упр3](extra/2017-11-22_Упражнения_по_рек.сис._Дима_Игнатов.pdf) |
|**2018-11-15**  [Spark Classification]() |[Павел Клеменков]() | | | [spark03](extra/spark03) | :warning: dataset в HDFS: /share/toxic_comments |
|**2018-11-17**  [Data Science Process]() | [Олег Хомюк](), [Александр Ульянов]() | [Жизненный цикл DS](materials/2018-11-17_Жизненный_цикл_DS_проектов_Олег_Хомюк.pdf), [DS cases](materials/2018-11-17_Alexandr_Ulyanov_DS_cases.pdf) || |  |
|**2018-11-20**  [Выбор метрики и оценка фин. эффекта]() | [Александр Ульянов]() | [](),  |[lab09](labs/lab09), [решение](solutions/lab09)| |  |
|**2018-11-22**  [Spark Clusterization, ALS]() |[Павел Клеменков]() | | | [spark04](extra/spark04) |  |
|**2018-11-24**  [A/B testing]() | [Олег Хомюк]() | [АB](materials/2018-11-24_AB_testing_Олег_Хомюк.pdf.pdf)  || | :warning: dataset на мастере: /data/share/AB_testing |
|**2018-11-27**  [Оценка качества]() | [Андрей Зимовнов]() | [Оценка качества](materials/2018-11-27_Метрики_качества_RS.pdf), [Нейросети в РС](materials/2018-11-27_Нейросети_в_РС.pdf)|| | | 
|**2018-11-29**  [Spark Streaming]() |[Павел Клеменков]() | | | [spark05](extra/spark05) | :warning: dataset в hdfs: /share/spark05/amazon_train.parquet   |
|**2018-12-01**  [Making a story of your data]() | [Флександр Филатов]() | [Story telling](materials/2018-12-01_Storytelling.pdf])  || |  |
|**2018-12-04**  [Spark Graphs]() |[Наталья Притыковская]() | | | [spark06](extra/spark06) | :warning: dataset в HDFS: /share/LinkPrediction, на мастере: /data/share/LinkPrediction |
|**2018-12_06**  [Spark Config, Нейросети в РС]() | [Артем Пичугин](), [Артем Просветов]() | [Конфигурация Спарк](materials/2018-12-06_Artem_Pichugin_Spark_conf.pdf), [Нейросети в РС](materials/) || |  |
|**2018-12-08**  [Intro to DL]() |[Григорий Сапунов]() | [Введение в Deep Learning](materials/) | |  |  |
