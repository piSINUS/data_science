9
Коэффициент корреляции Пирсона - может изменяться в пределах от -1 до 2 , где -1 отрицательная связь +1 - положительная, а 0 - отсутствие связи.

Нулевая гипотеза - связи нет, альтернативная - связь есть(не важно какая +-).Если коэффициент корреляции слишком большой по модулю, то нулевая гипотеза отвергается в пользу алтьр гип. 

есть аналог r критерию Пирсона - коэфф корреляции Спирмена

Чтобы вычислить, упорядочим котов от самого счастливого до самого несчастного  и присвоим им ранги. Затем мы перераспределим их от самого переедающего, до самого голодного и присвоим ранги уже по этому признаку. Если результаты обоих ранжирований будут совпадать между собой, то мы имеем + связь, если же они диаметрально противоположны то (-).

Мы получаем корреляционную матрицу. В ней записаны все вычисленные коэффициенты корреляции. Чтобы найти, какие переменные связаны с счастьем, достаточно найти нужный столбик и посмотреть, какие из этих коэффициентов являются значимыми. !!! Если мы находим несколько коэфоф корреляции одновременно, то используем поправку Бонферрони : поделив критический p-уровень значимости(0,05) на кол-во вычисл критериев и сравнив наш pуровень с получ значением.

10
Регрессионный анализ (стр97).Коефф b1 определяется как tgугла между линией котиков и оси x. Чем больше этот коефф, тем сильнее растет уровень счастья от каждой порции. b0 - величина которая показывает, насколько счастливы котики, если их совсем не кормить. По итогу, линейную взаимосвязь между количеством еды и котиковым счастьем можно описать так : счастье = b0 + (b1 * еду). Регрессионный анализ - прямая заменяющая группу  с мин  потерей данных. Регрессионный остаток - различие(отклонение) от регрессионной прямой.
Подвигаем эту точку, чем дальше от прямой тем отклонение больше, чем ближе, тем меньше, если стоит на прямой, то = 0. И таких точек много т.е. если все точки находятся на  прямой, то их совокупный остаток =0. Но при удалении от этой прямой общий остаток начнет увеличиваться. Чтобы найти совокупный аналог мы складываем квадраты остатков (Чем больше получившаяся сумма тем хуже прямая описывает наши данные. И суть регрессионного анализа заключается в том, чтобы подобрать такую прямую, при которой эта сумма была бы минимальной). Мы можем посмотреть какие факторы сильно влияют на счастье, и предсказывать , насколько будет счастлив тот или иной котик по их значениям.

Например:: Счастье = b0 + b1 * еда + b2 * мебель + b3 * клубок. Кроме самой формулы мы можем получить информацию о том, можно ли в неё что-нибудь добавить. В этом нам поможет коэфф детерминации R  ** 2. Он изменяется в промежутках от 0 до 1, и чем ближе к 1, тем лучше наша формула объясняет наблюдаемые данные. Низкий коэфф детерминации говорит о том, что нужно поискать, другие которые связаны с нашей формулой. (Связь не всегда является линейной. Есть взаимосвязи: которые можно описать с помощью полиноминального уравнения y = b0 +bx ** 2 или  y = b0 + b ** x или y = b0 + b/x) ^d601cd

11
Логистическая регрессия и Дискриминантный анализ.

Логарифм шанса - величина которая позволяет рассчитать вероятность того, что данный котик счастлив.(В данной ситуации шанс = (вероятность того что котик счастлив)/(вероятность того что котик несчастлив)).

От шанса берут натуральный логарифм и подставляют эту величину в [[#^d601cd|регрессионное уравнение]]. Если логарифм шанса положителен, то данный котик считается счастливым, а если отрицательным- то несчастным.

Дискриминантный анализ.
Мы можем видеть график(стр110) на нем представлены 2 группы котов счастливые и несчастные и сколько они едят.  Очевидно, что счастливые котики едят больше и мы можем провести между ними границу по этому фактору.  Алгоритм нахождения таких границ и называется дискриминантным анализом.  А формула которая задает границы - дискриминантной функцией.  Дискриминантный анализ может работать и с большим 
 количеством групп. Число границ всегда на 1 меньше чем число групп.

Проблема мультиколлениарности -  возникает в случаях. когда некоторые факторы сильно коррелируют между собой, приводит к неустойчивости получившегося уравнения. Проявляется в двух формах :
1. При добавлении всего одного двух котиков уравнение может измениться до неузнаваемости.
2. Формулы, построенные на двух сходных выборках котов, будут различаться

Эту проблему решают 3мя способами:

    1) Исключают 1 из коррелирующих переменных из анализа.

    2) предварительно проводят  процедуру факторного анализа.

    3) Проводят операцию пошаговой регрессии. Такая регрессия  постепенно вводит в уравнение по одной переменной и затем сразу проверяет вклад всех остальных. В итоге если одна из корреллирующих  переменных была выбрана. как фактор, то вторая скорее всего туда не попадет.

  

Вторая проблема - проблема переобучения заключается в том, что уравнение, полученное на одних котиках может не работать на других, она может возникать из-за того,  что  в нашей выборке могут быть закономерности которые не характерны для всех котиков в целом. И зачастую они попадают в регрессионную модель.(стр 114)

  

Для того, чтобы предотвратить переобучение, используют критерий,который искусственно ограничивает количество факторов, включенных в уравнение.(https://wiki.loginom.ru/articles/aic.html или  https://wiki.loginom.ru/articles/bic.html)

  

12  Основы математического моделирования.

Математическая модель - по сути, это аналог котика, который позволяет изучать его поведение без проведения реальных экспериментов. Все математические модели делятся на функциональные и структурные. Функциональные модели описывают влияние внешних факторов на котиковое состояние(регрессионное уравнение).

  

Структурные же модели могут описать компоненты счастья. Как правило функциональные модели, записываются с помощью уравнений. А вот структурные могут достаточно разнообразны : от таблиц до блок-схем.

  

Любая математическая модель строиться в 2 этапа. В первом  мы прикидываем, какие факторы в прицепе могут влиять на счастье или из каких компонентов оно может состоять.  Этот этап называется построением содержательной модели.

  

Второй этап  включает в себя сбор реальных данных и их мат обработку. Он называется построением  формальной модели. Формальную модель уже можно использовать, как аналог реального котика. Изменяя различные параметры это модели, вы сможете понять, как функционирует котик, не прибегая к опытам над животными.


Классификация мат моделей.
В частности бывают модели статические и динамические. Первые описывают состояние котика в какой то конкретный момент. Вторые же  на изменениях которые претерпевает котик. рис(стр118)
Кроме того делятся на линейные и нелинейные(стр119). Линейные включают в себя только линейные взаимосвязи (пример корелляционный и регрессионный анализ). Нелинейные взаимосвязи могут включать в себя нелинейные взаимосвязи(пример полиномиальная регрессия).

Также мы  можем разделить модели на непрерывные и дискрентные.
Если  состояние измеряется такой точной переменной то чтобы построить функциональную модель, нам необходима линейная регрессия. И они имеют переменные с бесконечным множеством значений.
Дискретные же модели работают с переменными, которые имеют ограниченное количество значений. Например, тот же размер, но имеющий только 3 значения: маленький, средний, большой. Построить эти модели  с дискретными целевыми переменными позволяет логистическая регрессия и дискриминантный анализ. 


13 Основы кластерного анализа. Методы которые позволяют рассортировать котиков по группам и выделять эти самые группы. Это все называется кластерным анализом.

Могут возникнуть 2 ситуации:
	1) Мы знаем, на сколько групп делятся котики, но не знаем, где о ни находиться.
	2) Мы не знаем итоговое количество групп.

Начнем со 2.
	Пример: Чтобы понять степень похожести, ==НАДО ПРОСТО НАЙТИ РАЗНОСТЬ МЕЖДУ РАЗМЕРАМИ==, чем она меньше, тем они более похожими являются котики.
	Итак, мы вычисляем все возможные разности между размерами котиков. Далее пара самых похожих котиков объединяем в группу(кластер). Затем мы опять вычисляем разности и объединяем похожих. И так происходит до тех пор, пока у нас все котики не объединятся в один большой кластер. Этот алгоритм относиться к методам иерархической кластеризации. Их довольно много, но каждый из них обладает следующими свойствами:
		1) Эти методы могут работать с большим количеством переменных - мы можем брать и размер, и степень пушистости, и длину коготков, и прочие котиковые признаки одновременно.
		2) На основе этих признаков мы вычисляем степень похожести котиков(чаще используется термин расстояние.)
		3) Объединяться в группы могут как было показано выше(метод ближайшего соседа, а может и по другим принципам.
		4) По итогу  вы получаете график, называемый дендрограммой. По ней можно определить, на какие группы делаться котики, и к какой группе они принадлежат.

Использование k -средних.
	Идея достаточно проста:
	Предположим, мы подозреваем, что все котики делятся на  три различающихся группы. Тогда у каждой группы есть свой представитель, который обладает самыми типичными для котиков характеристиками. Такой котик называется центроидом.  Основная задача алгоритма k -средних найти, каким именно размером эти центроиды обладают. Происходит это пошагово. На первом этапе(стр 127) мы  произвольно расставляем центроииды. На втором этапе вычисляются расстояния от каждого котика до каждого центроида (стр 128). На третьем  - определяем принадлежность котиков к тому или иному центроиду. Т.е смотрим к какому центроиду ближе котик. На 4ом этапе мы вычисляем средний размер при каждом центроиде. И центроид перемещается в этот размер. А потом алгоритм повторяется со второго шага. И так  повторяем до тех пор пока несколько пробегов центроиды будут неизменны. 

Метрики расстояний. 

Самая простая из них - эвклидово - есть просто самый кратчайший путь между двумя точками(стр131)

Иногда используют Манхэттенское расстояние. Когда мы не можем напрямую попасть из а в б. Его мы используем, если подозреваем что в нашей выборке есть выбросы.(стр 132)

Чаще всего используют расстояние Чебышева(стр132).

14 Основы факторного анализа.
Факторный анализ проходит в несколько этапов:
	1) Рассчитывается корреляционная матрица между всеми переменными, которые мы собирали:
		Размер, колво еды, царапучество
	2) Переменные которые коррелируют меж собой заменяются факторами.(стр 136)

В итоге мы получаем факторную матрицу.  В  каждой ячейке  такой таблицы - коэффициент корреляции между одним из факторов и конкретной переменной. называется он факторной нагрузкой.

Сумма эффектов корреляции называется собственным значением.
Далее происходит процедура вращения. Цель её заключается в том, чтобы большие коэффициенты корреляции в факторной матрице стали ещё больше, а маленькие еще меньше. Это означает, что каждый фактор  будет связан  только с опр группой переменных и ни с каким другим. (вращение стр 140) 

Вращение бывает двух видов:
	 Ортогональное и косоугольное.
	 В первом случае получившимся факторам запрещается коррелировать между собой, а во втором - нет.
Далее идет отсеивание лишних факторов, которые слабо связаны  с первоначальными переменными. Для этого существует 2 способа. 
	Первый(критерий Кайзера)
		он заключается в том, чтобы откинуть все факторы с собственным значением 
		ниже  1.
	Второй(критерий Кеттелла). Для того чтобы им воспользоваться, нужно построить график собственных значений.(стр 142)  На горизонтальной оси этого графика располагаются факторы,  а на вертикальной - их собственные значения. На  определенной точке этого графика происходит перегиб. И все факторы , которые находятся за этой точкой, отсеиваются.

Важно знать!!!
факторный анализ решает 2 проблемы:
1) Сокращение кол -ва переменных.
2) Это устранение  мултиколлениарности у регрессионных моделей (Эта проблема заключаеться в том, что если  две или более переменныне взаимосвязаны между собой, результаты регрессионного анализа будут крайне ненадежными.Поэтому мы заменяем такие переменные факторами.)