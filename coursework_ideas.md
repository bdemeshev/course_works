# Темы курсовых работ (Борис Демешев)

Общий комментарий ко всем работам:
Работа должна быть выполнена с использованием LaTeX. 
Скорее всего в работе потребуется программировать на R или Python. 
Это не должно отпугивать, предварительных знаний LaTeX, R, Python не требуется, 
всё это можно освоить по ходу работы. 
Если интересно работать со мной, то не бойтесь предложить любую свою тему. 


### 2 курс. Научная анимация.
Разобраться с созданием анимированных графиков в R/Python.
Разобраться с построением карт в R/Python.
Построить анимацию показывающую изменение какого-либо экономического показателя в России.
Написать понятную инструкцию для желающих сотворить подобную анимацию


### 3 курс. Построение регрессии с большим количеством наблюдений
Раздобыть огромный массив реальных данных
Огромный - это не меньше 4 гигабайт, чтобы он целиком не влезал в оперативную память компьютера
Построить регрессию по данному массиву
Доступно для повторения описать проделанное
Если есть возможность, то рассмотреть регрессию с большим количеством переменных
Вероятно, потребуется разобраться с SQL


### 3 курс. LASSO и ridge regression
разобраться с техникой LASSO, Ridge regression
реализовать в открытых пакетах: R, Python.
сравнить LASSO на реальных примерах с проверкой гипотез
интерпретация с точки зрения байесовского подхода


### 3 курс. Использование алгоритма классификации randomForest
Разобраться с алгоритмом randomForest и его реализацией в R/Python
Сравнить на реальном примере результаты randomForest и logit/probit регрессии
Написать доступную для повторения инструкцию
Сюда же можно добавить SVM


### 3 курс и выше. Исследование цен на отели по данным booking.com
Написать робота, который бы выкачивал данные с booking.com (можно взять другой сайт)
Описать данные.
Сформулировать содержательные гипотезы и проверить их


### 3 курс и выше. Исследование цен на авиаперелеты.
Написать робота, который бы выкачивал данные с momondo.com (можно взять другой сайт)
Описать данные.
Сформулировать содержательные гипотезы и проверить их


### 3 курс и выше. Исследование цен на подержанные авто.
Написать робота, который бы выкачивал данные с auto.yandex.ru (можно взять другой сайт)
Описать данные.
Сформулировать содержательные гипотезы и проверить их

### 3 курс. Реализовать в виде plugin'а к gretl какие-нибудь алгоритмы из spss/stata.
Не хватает всяких многомерных классификации. Спросить у Марины Храмовой.
Перевод (письмо Gretl project on the launchpad, Ivan Sopov)


### 3 курс и выше
анализ цен на бриллианты
Есть готовый набор данных в R

### 3 курс и выше 
Анализ цен на аукционах
Сотбис
для статистики:
http://www.auction-air.com/inflight-auction/Low-Bid-Auction/Lot-14027-Results.aspx


### 3 курс и выше
Реализовать multivariate ordered probit в jags/stan/pymc/голом R/голом python

### 2 курс и выше:
создать подборку примеров оцененных моделей с комментариями в jags или stan
Каждый пример должен содержать 4 файла:
1. набор данных
2. описание модели в jags/stan
3. программу R, загружающую данные и оценивающую модели
4. описание данных и модели


### 3 курс и выше:
реализовать модальную параметрическую регрессию в R
Weixin
есть его матлабовский код
Сравнить классическую, квантильную и модальную регрессию на простом наборе данных


Плохо продуманные, нуждаются в доработке
----------------------------------------


### 2 курс (??? пока не хватает на курсовую)
Хранение данных открыто в интернете:
Использование google docs + google api
Храним все данные в интернете, строим регрессии по ним...
http://precedings.nature.com/documents/4918/version/1/files/npre20104918-1.pdf
облачные вычисления:
http://www.picloud.com/
сервис коротких ссылок
...
описать установку R/jags/stan/python/pymc на amazon (или другой сервер)
запустить его дистанционно, загрузить данные, выгрузить данные

http://public.opencpu.org/pages/
чтение данных из google.docs в R с помощью Rcurl



* gapminder
* xkcd/980
* сжатие площадей стран пропорционально показателю
* визуализация потоков мигрантов/товаров
* Iterated prisoner's dilemma Dyson, Press
* Авторешатель для тигров
* Прогнозирование результатов экзаменов



### 3 курс:
Научиться генерить переменные так, чтобы:
Сразу выкинуть Х1 и Х2 - гипотеза отвергается.
Сначала выкинуть Х1, затем выкинуть Х2 -
гипотеза не отвергается.
Понять, в чем особенность такого набора данных.
Попытаться найти такую ситуацию в реальных данных.

Связанная задача (с известным ответом - мультиколлинеарность)
Сразу выкинуть Х1 и Х2 - гипотеза отвергается.
Выкинуть отдельно Х1 - гипотеза не отвергается.
Выкинуть отдельно Х2 - гипотеза не отвергается.



