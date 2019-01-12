## Полезности

* Формальные [требования к курсовым](https://github.com/bdemeshev/course_works/blob/master/coursework_requirements.md)
* Популярные [ошибки в презентациях](https://github.com/bdemeshev/course_works/blob/master/typical_techinal_errors.md)
* Советы [пищущим курсовые](https://github.com/bdemeshev/epsilon/raw/master/e_001/metrics-errors/metrics-errors.pdf)


## Идеи проектов и курсовых

Что-то из этого тянет на проект, что-то на курсовую, что-то вообще никак :)


Идеи проектов:

* Научиться генерить переменные так, чтобы:
Сразу выкинуть Х1 и Х2 - гипотеза отвергается.
Сначала выкинуть Х1, затем выкинуть Х2 -
гипотеза не отвергается.
Понять, в чем особенность такого набора данных.
Попытаться найти такую ситуацию в реальных данных.

Связанная задача (с известным ответом - мультиколлинеарность)
Сразу выкинуть Х1 и Х2 - гипотеза отвергается.
Выкинуть отдельно Х1 - гипотеза не отвергается.
Выкинуть отдельно Х2 - гипотеза не отвергается.

* Плакат про все подходы к методу главных компонент
[Niels Richard Hansen, PC](www.math.ku.dk/~richard/courses/statlearn2011/pca.pdf)
  * Как поиск ближайшей плоскости. Пример задачи.
  * Как максимизация разброса. Пример задачи.
  * Как максимизация R^2. Пример задачи.
  * Как SVD.


* Общая идея: плакат с оригинальной и красивой визуализацией набора данных.

* Построить визуализацию, аналогичную https://www.r-bloggers.com/french-mortality-poster/ по России (там есть ссылка на данные с 1950х)

* Плакат про энтропию, [colah.github.io](http://colah.github.io/posts/2015-09-Visual-Information/)

* Плакат с визуализацией ставок в лотерее. Идея — показать, насколько люди ставят
неравномерно. Например, исторические [данные по Спортлото](https://timelottery.ru/lottery/sovetskoe-sportloto-istoriya-i-arhiv-tirazhej/)


* Доделать до плаката/чит-шита [словарик stata-R](https://github.com/andrey-lukyanov/Econometrics_project_2018).

* Общая идея: облегчение доступа к некоторому набору данных.

* Плакат про данные RLMS + развитие пакета [rlms](https://github.com/bdemeshev/rlms). На плакате — рассказ про данные, пример загрузки, решение задач в жанре «зная, как респондент ответил на вопрос в прошлом году, присвоить переменной текущего года какое-то значение».

* Развитие и публикацие на CRAN пакета для скачивания [данных с сайта ЦБ](https://github.com/bdemeshev/cbr).

* Пакет explainer. Пакет, который объясняет результаты модели или теста словами.
Словами говорит предпосылки, аккуратно пишет нулевую и альтернативную гипотезу,
результат. Добавлять новое описание можно с помощью какого-нибудь yaml, там нужно
как-то присмотреть ветвление? Несколько языков: русский и английский? Чтение текста слабовидящим? Функция `equation` в пакете `fable`, текстовое описание в пакете
`CausalImpact`.

* Пакет по данным росстата. Чем ограничить?

* Пакет с данными по балансам банков. Сами данные плюс функции для пополнения.

* Плакат для ознакомления с открытыми наборами данных и пакетами для их скачивания.
Примеры ближе к России. Например, [quandl](quandl.com), [imf](https://github.com/christophergandrud/imfr), [finam](https://quanttools.bitbucket.io/_site/get_started.html) и прочее, и прочее... Слишком много источников? Разбить на макро и финансы, условно?













## 2017-2018

Артём Кондрашов, [Сжатые байесовские BVAR](https://github.com/akondrashov96/RcppBVAR)

Оля Гнилова, [How Gauss-Markov and Pythagoras met: Geometry in Econometrics](https://github.com/olyagnilova/gauss-markov-pythagoras)

Пётр Гармидер, [LSTM для прогнозирования макроэкономических показателей](https://github.com/PetrGarm/coursework)

Зехов Матвей, [LSTM для прогнозирования макроэкономических рядов](https://github.com/Pyatachokk/Course_work)

Маша Сапельникова, [Рекуррентные нейронные сети для прогнозирования макроэкономических показателей](https://github.com/maschasap/rnn)

Вика Шрамова, [Модификация тета-метода](https://github.com/VictoriaShramova/diploma)

Настя Волкова, [Прогнозирование рядов с помощью SSA](https://github.com/Anastasia4111/SSA)

Аким Цвигун, [Прогнозирование рядов с LSTM](https://github.com/Aktsvigun/term_paper)

Михаил Пьянков, [Прогнозирование рядов с prophet](https://github.com/MikhailPyankov/Course-paper)

Аня Кожевина, [Прогнозирование с помощью BVAR](https://github.com/akozhevina/kursach)


## 2016-2017

Оля Гнилова, [Прогнозирование рядов с помощью модели состояние-наблюдение](https://github.com/olyagnilova/term-paper/tree/master/2017)

Вика Шрамова, [Анализ и прогнозирование рядов в BSTS и prophet](https://github.com/VictoriaShramova/bsts_prophet_code)

Айдар Исхаков, [NLP and deep learning](https://github.com/bdemeshev/course_works/tree/master/2016_2017/iskhakov_nlp_deep_learning)

Артём Кондрашов, [Моделирование в STAN](https://github.com/bdemeshev/course_works/tree/master/2016_2017/kondrashov_stan)


## 2015-2016

Артём Кондрашов, [Карты в R](https://github.com/akondrashov96/Tutorials-Scripts/tree/master/Visualisation_maps)

Эдуард Аюнц, [Моделирование процентных ставок](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_2b_ayunts_eduard_interest_rates)

Иван Барабанов, [Отмены заказов в яндекс такси](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_3b_baranov_ivan_yandex_taxi)

Полина Деткова, [Модель MIDAS](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_3b_detkova_polina_midas)

Мира Федотова, [На Лабутенах и с офигетельной вкр](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_3b_fedotova_mira_louboutin)

Аня Кузина, [Модель MIDAS](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_3b_kuzina_anna_midas)

Женя Волкова, [Эволюция портфеля](https://github.com/bdemeshev/course_works/tree/master/2015_2016/2015_3b_volkova_jenia_evolutsia_portfelia)


## 2014-2015

Аня Кузина, [Экспоненциальное сглаживание](https://github.com/bdemeshev/course_works/tree/master/2014_2015/2014_2b_Kuzina_Anna_exponential_smoothing)


## 2013-2014

Аня Тихонова, [Прогнозирование банкротства предприятий](https://github.com/bdemeshev/course_works/tree/master/2013_2014/2013_4b_tikhonova_bankruptcy)


## 2012-2013

Карина Хусаинова, [Скандинавские аукционы](https://github.com/bdemeshev/course_works/tree/master/2012_2013/2012_2b_karina_khusainova_scandinavian_auctions)

Никита Петров, [Доходы депутатов](https://github.com/bdemeshev/course_works/tree/master/2012_2013/2012_2b_nikita_petrov_dohod_deputatov)

Вазген Бадалян, [Модели процентных ставок](https://github.com/bdemeshev/course_works/tree/master/2012_2013/2012_2b_vazgen_badalyan_interest_rate_models)

Ярослав Захаров, [Модели процентных ставок](https://github.com/bdemeshev/course_works/tree/master/2012_2013/2012_3b_vasieliev_sergey_lasso)

Сергей Васильев, [Модель LASSO](https://github.com/bdemeshev/course_works/tree/master/2012_2013/2012_3b_vasieliev_sergey_lasso)



## 2011-2012

Артём Пузанов, [Анализ сговора участников аукциона](https://github.com/bdemeshev/course_works/tree/master/2011_2012/2011_4b_artem_puzanov)
