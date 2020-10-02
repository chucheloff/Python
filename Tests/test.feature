#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "ya.ru"
  Then push button with text 'Найти'
  Then page include text 'Задан пустой поисковый запрос'
