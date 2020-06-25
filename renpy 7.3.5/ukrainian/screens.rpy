# TODO: Translation updated at 2019-08-27 23:20

translate ukrainian strings:

    # gui/game/screens.rpy:9
    old "## Styles"
    new "## Стилі"

    # gui/game/screens.rpy:81
    old "## In-game screens"
    new "## Ігрові екрани"

    # gui/game/screens.rpy:85
    old "## Say screen"
    new "## Екран повідомлення"

    # gui/game/screens.rpy:87
    old "## The say screen is used to display dialogue to the player. It takes two parameters, who and what, which are the name of the speaking character and the text to be displayed, respectively. (The who parameter can be None if no name is given.)"
    new "## Екран повідомлення використовується для відображення розмови з гравцем. Він приймає два показники: who (хто) і what (що), що є ім'ям персонажа що говорить і відображуваним текстом, відповідно. (показник who може бути None, якщо ім'я не вказано.)"

    # gui/game/screens.rpy:92
    old "## This screen must create a text displayable with id \"what\", as Ren'Py uses this to manage text display. It can also create displayables with id \"who\" and id \"window\" to apply style properties."
    new "## Цей екран повинен створити текст, який відображається з ідентифікатором \"what\", оскільки Ren'Py використовує це для управління відображенням тексту. Він також може створювати покази з ідентифікатором \"who\" та ідентифікатором \"window\" щоб застосувати властивости стилю."

    # gui/game/screens.rpy:96
    old "## https://www.renpy.org/doc/html/screen_special.html#say"
    new "## https://www.renpy.org/doc/html/screen_special.html#say"

    # gui/game/screens.rpy:114
    old "## If there's a side image, display it above the text. Do not display on the phone variant - there's no room."
    new "## Якщо є бічне зображення, виводить його над текстом. Не показується на варіанті телефону - немає місця."

    # gui/game/screens.rpy:120
    old "## Make the namebox available for styling through the Character object."
    new "## Зробіть поле імен доступним для стилізації через об'єкт Character."

    # gui/game/screens.rpy:164
    old "## Input screen"
    new "## Екран введення"

    # gui/game/screens.rpy:166
    old "## This screen is used to display renpy.input. The prompt parameter is used to pass a text prompt in."
    new "## Цей екран використовується для відображення renpy.input. Параметр prompt використовується для передачі текстового запиту ???."

    # gui/game/screens.rpy:169
    old "## This screen must create an input displayable with id \"input\" to accept the various input parameters."
    new "## Цей екран повинен створити вхід, на який можна відображатись id \"input\" щоб приймати різні вхідні параметри ???."

    # gui/game/screens.rpy:172
    old "## https://www.renpy.org/doc/html/screen_special.html#input"
    new "## https://www.renpy.org/doc/html/screen_special.html#input"

    # gui/game/screens.rpy:199
    old "## Choice screen"
    new "## Екран вибору"

    # gui/game/screens.rpy:201
    old "## This screen is used to display the in-game choices presented by the menu statement. The one parameter, items, is a list of objects, each with caption and action fields."
    new "## Цей екран використовується для відображення відмін у грі, представлених випискою меню. Один параметр, елементи, - це список об'єктів, кожен із полями заголовків та дій ???."

    # gui/game/screens.rpy:205
    old "## https://www.renpy.org/doc/html/screen_special.html#choice"
    new "## https://www.renpy.org/doc/html/screen_special.html#choice"

    # gui/game/screens.rpy:215
    old "## When this is true, menu captions will be spoken by the narrator. When false, menu captions will be displayed as empty buttons."
    new "## Коли це правда, оповідач промовить підписи меню. Якщо помилково, підписи меню відображатимуться як порожні кнопки."

    # gui/game/screens.rpy:238
    old "## Quick Menu screen"
    new "## Екран швидкого меню"

    # gui/game/screens.rpy:240
    old "## The quick menu is displayed in-game to provide easy access to the out-of-game menus."
    new "## Швидке меню відображається в грі, щоб забезпечити легкий доступ до меню поза грою"

    # gui/game/screens.rpy:245
    old "## Ensure this appears on top of other screens."
    new "## Переконайтеся, що це відображається поверх інших екранів"

    # gui/game/screens.rpy:256
    old "Back"
    new "Назад"

    # gui/game/screens.rpy:257
    old "History"
    new "Історія"

    # gui/game/screens.rpy:258
    old "Skip"
    new "Пропустити"

    # gui/game/screens.rpy:259
    old "Auto"
    new "Автоматично"

    # gui/game/screens.rpy:260
    old "Save"
    new "Збереження"

    # gui/game/screens.rpy:261
    old "Q.Save"
    new "Шв. Збереження"

    # gui/game/screens.rpy:262
    old "Q.Load"
    new "Шв. Завантаження"

    # gui/game/screens.rpy:263
    old "Prefs"
    new "Налаштування"

    # gui/game/screens.rpy:266
    old "## This code ensures that the quick_menu screen is displayed in-game, whenever the player has not explicitly hidden the interface."
    new "## Цей код ґарантує, що екран швидкого меню відображатиметься в грі, коли гравець не приховував явно інтерфейс ???."

    # gui/game/screens.rpy:284
    old "## Main and Game Menu Screens"
    new "## Основний екран та екран меню ігор"

    # gui/game/screens.rpy:287
    old "## Navigation screen"
    new "## Навіґаційний екран"

    # gui/game/screens.rpy:289
    old "## This screen is included in the main and game menus, and provides navigation to other menus, and to start the game."
    new "## Цей екран включений в основне та ігрове меню і забезпечує навіґацію до інших меню і запуск гри."

    # gui/game/screens.rpy:304
    old "Start"
    new "Нова гра"

    # gui/game/screens.rpy:312
    old "Load"
    new "Завантаження"

    # gui/game/screens.rpy:314
    old "Preferences"
    new "Налаштування"

    # gui/game/screens.rpy:318
    old "End Replay"
    new "Кінець повтору"

    # gui/game/screens.rpy:322
    old "Main Menu"
    new "Головне меню"

    # gui/game/screens.rpy:324
    old "About"
    new "Про нас"

    # gui/game/screens.rpy:328
    old "## Help isn't necessary or relevant to mobile devices."
    new "## Довідка не потрібна або підходить тільки для стільникових пристроїв"

    # gui/game/screens.rpy:329
    old "Help"
    new "Довідка"

    # gui/game/screens.rpy:331
    old "## The quit button is banned on iOS and unnecessary on Android."
    new "## Кнопка виходу заборонена на iOS та непотрібна на Android."

    # gui/game/screens.rpy:332
    old "Quit"
    new "Вихід"

    # gui/game/screens.rpy:346
    old "## Main Menu screen"
    new "## Екран головного меню"

    # gui/game/screens.rpy:348
    old "## Used to display the main menu when Ren'Py starts."
    new "## Використовується для відображення головного меню під час запуску Ren'Py."

    # gui/game/screens.rpy:350
    old "## https://www.renpy.org/doc/html/screen_special.html#main-menu"
    new "## https://www.renpy.org/doc/html/screen_special.html#main-menu"

    # gui/game/screens.rpy:354
    old "## This ensures that any other menu screen is replaced."
    new "## Це гарантує заміну будь-якого іншого екрана меню ???."

    # gui/game/screens.rpy:361
    old "## This empty frame darkens the main menu."
    new "## Цей порожній кадр затемнює головне меню ???."

    # gui/game/screens.rpy:365
    old "## The use statement includes another screen inside this one. The actual contents of the main menu are in the navigation screen."
    new "## Заява про використання включає ще один екран всередині цього. Фактичний вміст головного меню знаходиться на екрані навіґації ???."

    # gui/game/screens.rpy:408
    old "## Game Menu screen"
    new "## Екран меню гри"

    # gui/game/screens.rpy:410
    old "## This lays out the basic common structure of a game menu screen. It's called with the screen title, and displays the background, title, and navigation."
    new "## Тут викладається основна загальна структура екрана меню гри. Він називається заголовок екрана та відображає тло, заголовок та навіґацію ???."

    # gui/game/screens.rpy:413
    old "## The scroll parameter can be None, or one of \"viewport\" or \"vpgrid\". When this screen is intended to be used with one or more children, which are transcluded (placed) inside it."
    new "## Параметр прокрутки може бути None, або одним із \"viewport\" чи \"vpgrid\". Коли цей екран призначений для використання з одним або декількома дітьми, які включені (розміщені) всередині нього ???."

    # gui/game/screens.rpy:431
    old "## Reserve space for the navigation section."
    new "## Зарезервуйте простір для навіґаційної частини ???."

    # gui/game/screens.rpy:473
    old "Return"
    new "Повернутися"

    # gui/game/screens.rpy:536
    old "## About screen"
    new "## Екран «Про нас»"

    # gui/game/screens.rpy:538
    old "## This screen gives credit and copyright information about the game and Ren'Py."
    new "## Цей екран надає відомости про творців та їх права на гру та Ren'Py ???."

    # gui/game/screens.rpy:541
    old "## There's nothing special about this screen, and hence it also serves as an example of how to make a custom screen."
    new "## У цьому екрані немає нічого особливого, а значить, він також слугує прикладом того, як зробити власний екран ???."

    # gui/game/screens.rpy:548
    old "## This use statement includes the game_menu screen inside this one. The vbox child is then included inside the viewport inside the game_menu screen."
    new "## This use statement includes the game_menu screen inside this one. The vbox child is then included inside the viewport inside the game_menu screen."

    # gui/game/screens.rpy:558
    old "Version [config.version!t]\n"
    new "Версія [config.version!t]\n"

    # gui/game/screens.rpy:560
    old "## gui.about is usually set in options.rpy."
    new "## gui.about is usually set in options.rpy."

    # gui/game/screens.rpy:564
    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Зроблено за допомогою {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"

    # gui/game/screens.rpy:567
    old "## This is redefined in options.rpy to add text to the about screen."
    new "## This is redefined in options.rpy to add text to the about screen."

    # gui/game/screens.rpy:579
    old "## Load and Save screens"
    new "## Load and Save screens"

    # gui/game/screens.rpy:581
    old "## These screens are responsible for letting the player save the game and load it again. Since they share nearly everything in common, both are implemented in terms of a third screen, file_slots."
    new "## These screens are responsible for letting the player save the game and load it again. Since they share nearly everything in common, both are implemented in terms of a third screen, file_slots."

    # gui/game/screens.rpy:585
    old "## https://www.renpy.org/doc/html/screen_special.html#save https://www.renpy.org/doc/html/screen_special.html#load"
    new "## https://www.renpy.org/doc/html/screen_special.html#save https://www.renpy.org/doc/html/screen_special.html#load"

    # gui/game/screens.rpy:604
    old "Page {}"
    new "Сторінка {}"

    # gui/game/screens.rpy:604
    old "Automatic saves"
    new "Автоматичні збереження"

    # gui/game/screens.rpy:604
    old "Quick saves"
    new "Швидкі збереження"

    # gui/game/screens.rpy:610
    old "## This ensures the input will get the enter event before any of the buttons do."
    new "## Це гарантує, що вхід отримає подія введення раніше, ніж будь-яка з кнопок."

    # gui/game/screens.rpy:614
    old "## The page name, which can be edited by clicking on a button."
    new "## Назва сторінки, яку можна відредагувати, натиснувши кнопку."

    # gui/game/screens.rpy:626
    old "## The grid of file slots."
    new "## Сітка комірок для файлів."

    # gui/game/screens.rpy:646
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%A, %B %d %Y, %H:%M"

    # gui/game/screens.rpy:646
    old "empty slot"
    new "порожня комірка"

    # gui/game/screens.rpy:654
    old "## Buttons to access other pages."
    new "## Buttons to access other pages."

    # gui/game/screens.rpy:663
    old "<"
    new "<"

    # gui/game/screens.rpy:666
    old "{#auto_page}A"
    new "{#auto_page}A"

    # gui/game/screens.rpy:669
    old "{#quick_page}Q"
    new "{#quick_page}Q"

    # gui/game/screens.rpy:671
    old "## range(1, 10) gives the numbers from 1 to 9."
    new "## range(1, 10) gives the numbers from 1 to 9."

    # gui/game/screens.rpy:675
    old ">"
    new ">"

    # gui/game/screens.rpy:710
    old "## Preferences screen"
    new "## Екран налаштувань"

    # gui/game/screens.rpy:712
    old "## The preferences screen allows the player to configure the game to better suit themselves."
    new "## The preferences screen allows the player to configure the game to better suit themselves."

    # gui/game/screens.rpy:715
    old "## https://www.renpy.org/doc/html/screen_special.html#preferences"
    new "## https://www.renpy.org/doc/html/screen_special.html#preferences"

    # gui/game/screens.rpy:732
    old "Display"
    new "Дисплей"

    # gui/game/screens.rpy:733
    old "Window"
    new "Вікно"

    # gui/game/screens.rpy:734
    old "Fullscreen"
    new "Повноекранний"

    # gui/game/screens.rpy:738
    old "Rollback Side"
    new "Відкатний бік"

    # gui/game/screens.rpy:739
    old "Disable"
    new "Вимкнути"

    # gui/game/screens.rpy:740
    old "Left"
    new "Ліво"

    # gui/game/screens.rpy:741
    old "Right"
    new "Право"

    # gui/game/screens.rpy:746
    old "Unseen Text"
    new "Непрочитаний текст"

    # gui/game/screens.rpy:747
    old "After Choices"
    new "Після виборів"

    # gui/game/screens.rpy:748
    old "Transitions"
    new "Переходи"

    # gui/game/screens.rpy:750
    old "## Additional vboxes of type \"radio_pref\" or \"check_pref\" can be added here, to add additional creator-defined preferences."
    new "## Additional vboxes of type \"radio_pref\" or \"check_pref\" can be added here, to add additional creator-defined preferences."

    # gui/game/screens.rpy:761
    old "Text Speed"
    new "Швидкість тексту"

    # gui/game/screens.rpy:765
    old "Auto-Forward Time"
    new "Час самочитання"

    # gui/game/screens.rpy:772
    old "Music Volume"
    new "Гучність музики"

    # gui/game/screens.rpy:779
    old "Sound Volume"
    new "Гучність звуку"

    # gui/game/screens.rpy:785
    old "Test"
    new "Перевірка"

    # gui/game/screens.rpy:789
    old "Voice Volume"
    new "Гучність голосу"

    # gui/game/screens.rpy:800
    old "Mute All"
    new "Заглушити усе"

    # gui/game/screens.rpy:876
    old "## History screen"
    new "## Екран історії"

    # gui/game/screens.rpy:878
    old "## This is a screen that displays the dialogue history to the player. While there isn't anything special about this screen, it does have to access the dialogue history stored in _history_list."
    new "## This is a screen that displays the dialogue history to the player. While there isn't anything special about this screen, it does have to access the dialogue history stored in _history_list."

    # gui/game/screens.rpy:882
    old "## https://www.renpy.org/doc/html/history.html"
    new "## https://www.renpy.org/doc/html/history.html"

    # gui/game/screens.rpy:888
    old "## Avoid predicting this screen, as it can be very large."
    new "## Avoid predicting this screen, as it can be very large."

    # gui/game/screens.rpy:899
    old "## This lays things out properly if history_height is None."
    new "## This lays things out properly if history_height is None."

    # gui/game/screens.rpy:909
    old "## Take the color of the who text from the Character, if set."
    new "## Take the color of the who text from the Character, if set."

    # gui/game/screens.rpy:918
    old "The dialogue history is empty."
    new "Історія розмов порожня."

    # gui/game/screens.rpy:921
    old "## This determines what tags are allowed to be displayed on the history screen."
    new "## This determines what tags are allowed to be displayed on the history screen."

    # gui/game/screens.rpy:968
    old "## Help screen"
    new "## Help screen"

    # gui/game/screens.rpy:970
    old "## A screen that gives information about key and mouse bindings. It uses other screens (keyboard_help, mouse_help, and gamepad_help) to display the actual help."
    new "## A screen that gives information about key and mouse bindings. It uses other screens (keyboard_help, mouse_help, and gamepad_help) to display the actual help."

    # gui/game/screens.rpy:989
    old "Keyboard"
    new "Набірниця"

    # gui/game/screens.rpy:990
    old "Mouse"
    new "Миша"

    # gui/game/screens.rpy:993
    old "Gamepad"
    new "Ґеймпад"

    # gui/game/screens.rpy:1006
    old "Enter"
    new "Enter"

    # gui/game/screens.rpy:1007
    old "Advances dialogue and activates the interface."
    new "Програє розмову та задіює інтерфейс."

    # gui/game/screens.rpy:1010
    old "Space"
    new "Прогалина"

    # gui/game/screens.rpy:1011
    old "Advances dialogue without selecting choices."
    new "Програє розмову без вибору відмін."

    # gui/game/screens.rpy:1014
    old "Arrow Keys"
    new "Кнопки зі стрілками"

    # gui/game/screens.rpy:1015
    old "Navigate the interface."
    new "Навіґація по інтерфейсу."

    # gui/game/screens.rpy:1018
    old "Escape"
    new "Escape"

    # gui/game/screens.rpy:1019
    old "Accesses the game menu."
    new "Доступ до меню гри."

    # gui/game/screens.rpy:1022
    old "Ctrl"
    new "Ctrl"

    # gui/game/screens.rpy:1023
    old "Skips dialogue while held down."
    new "Пропускає розмову, будучи утриманим."

    # gui/game/screens.rpy:1026
    old "Tab"
    new "Tab"

    # gui/game/screens.rpy:1027
    old "Toggles dialogue skipping."
    new "Перемикає пропускання розмови."

    # gui/game/screens.rpy:1030
    old "Page Up"
    new "Page Up"

    # gui/game/screens.rpy:1031
    old "Rolls back to earlier dialogue."
    new "Повернення до попередньої розмови."

    # gui/game/screens.rpy:1034
    old "Page Down"
    new "Page Down"

    # gui/game/screens.rpy:1035
    old "Rolls forward to later dialogue."
    new "Перехід до подальшої розмови."

    # gui/game/screens.rpy:1039
    old "Hides the user interface."
    new "Приховує користувацький інтерфейс."

    # gui/game/screens.rpy:1043
    old "Takes a screenshot."
    new "Робить зняток екрану."

    # gui/game/screens.rpy:1047
    old "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}."
    new "Перемикає допоміжне {a=https://www.renpy.org/l/voicing}самоозвучення{/a}."

    # gui/game/screens.rpy:1053
    old "Left Click"
    new "Ліва кнопка миші"

    # gui/game/screens.rpy:1057
    old "Middle Click"
    new "Середня кнопка миші"

    # gui/game/screens.rpy:1061
    old "Right Click"
    new "Права кнопка миші"

    # gui/game/screens.rpy:1065
    old "Mouse Wheel Up\nClick Rollback Side"
    new "Коліщатко миші вгору\nКлац по коліщатку"

    # gui/game/screens.rpy:1069
    old "Mouse Wheel Down"
    new "Коліщатко миші вниз"

    # gui/game/screens.rpy:1076
    old "Right Trigger\nA/Bottom Button"
    new "Правий джойстик\nA/Нижня кнопка"

    # gui/game/screens.rpy:1080
    old "Left Trigger\nLeft Shoulder"
    new "Лівий джойстик\nЛіве плечико"

    # gui/game/screens.rpy:1084
    old "Right Shoulder"
    new "Праве плечико"

    # gui/game/screens.rpy:1089
    old "D-Pad, Sticks"
    new "Хрестовина, Стіки"

    # gui/game/screens.rpy:1093
    old "Start, Guide"
    new "Start, Guide"

    # gui/game/screens.rpy:1097
    old "Y/Top Button"
    new "Y/Верхня кнопка"

    # gui/game/screens.rpy:1100
    old "Calibrate"
    new "Вивіряти"

    # gui/game/screens.rpy:1128
    old "## Additional screens"
    new "## Додаткові екрани"

    # gui/game/screens.rpy:1132
    old "## Confirm screen"
    new "## Екран підтвердження"

    # gui/game/screens.rpy:1134
    old "## The confirm screen is called when Ren'Py wants to ask the player a yes or no question."
    new "## Екран підтвердження викликається, коли Ren'Py хоче поставити гравцеві питання \"так\" чи \"ні\"."

    # gui/game/screens.rpy:1137
    old "## https://www.renpy.org/doc/html/screen_special.html#confirm"
    new "## https://www.renpy.org/doc/html/screen_special.html#confirm"

    # gui/game/screens.rpy:1141
    old "## Ensure other screens do not get input while this screen is displayed."
    new "## Переконайтесь, що під час відображення цього екрана інші екрани не відображаються."

    # gui/game/screens.rpy:1165
    old "Yes"
    new "Так"

    # gui/game/screens.rpy:1166
    old "No"
    new "Ні"

    # gui/game/screens.rpy:1168
    old "## Right-click and escape answer \"no\"."
    new "## Права кнопка миші та escape є відповіддю \"ні\"."

    # gui/game/screens.rpy:1195
    old "## Skip indicator screen"
    new "## Екран покажчика пропуску"

    # gui/game/screens.rpy:1197
    old "## The skip_indicator screen is displayed to indicate that skipping is in progress."
    new "## Екран skip_indicator (покажчика пропуску) відображається, щоб вказати, що пропуск триває."

    # gui/game/screens.rpy:1200
    old "## https://www.renpy.org/doc/html/screen_special.html#skip-indicator"
    new "## https://www.renpy.org/doc/html/screen_special.html#skip-indicator"

    # gui/game/screens.rpy:1212
    old "Skipping"
    new "Пропускання"

    # gui/game/screens.rpy:1219
    old "## This transform is used to blink the arrows one after another."
    new "## Це перетворення використовується для миготіння стрілок одна за одною."

    # gui/game/screens.rpy:1246
    old "## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE glyph in it."
    new "## Нам потрібно використовувати шрифт, що має символ U+25B8 (стрілка вище)."

    # gui/game/screens.rpy:1251
    old "## Notify screen"
    new "## Екран сповіщень"

    # gui/game/screens.rpy:1253
    old "## The notify screen is used to show the player a message. (For example, when the game is quicksaved or a screenshot has been taken.)"
    new "## Екран сповіщень використовується, щоб показати гравцеві сповіщення. (Наприклад, коли гра самозбереглася, або був зроблений зняток екрану)"

    # gui/game/screens.rpy:1256
    old "## https://www.renpy.org/doc/html/screen_special.html#notify-screen"
    new "## https://www.renpy.org/doc/html/screen_special.html#notify-screen"

    # gui/game/screens.rpy:1290
    old "## NVL screen"
    new "## Екран NVL"

    # gui/game/screens.rpy:1292
    old "## This screen is used for NVL-mode dialogue and menus."
    new "## Цей екран використовується для розмов та меню режиму NVL."

    # gui/game/screens.rpy:1294
    old "## https://www.renpy.org/doc/html/screen_special.html#nvl"
    new "## https://www.renpy.org/doc/html/screen_special.html#nvl"

    # gui/game/screens.rpy:1305
    old "## Displays dialogue in either a vpgrid or the vbox."
    new "## Показує розмову в vpgrid чи vbox."

    # gui/game/screens.rpy:1318
    old "## Displays the menu, if given. The menu may be displayed incorrectly if config.narrator_menu is set to True, as it is above."
    new "## Показує меню, якщо є. Меню може показувати некоректно, якщо config.narrator_menu встановлено на True."

    # gui/game/screens.rpy:1348
    old "## This controls the maximum number of NVL-mode entries that can be displayed at once."
    new "## Це керує щонайбільшою кількістю записів у режимі NVL, які можуть відображатися одночасно."

    # gui/game/screens.rpy:1410
    old "## Mobile Variants"
    new "## Мобільні варіанти"

    # gui/game/screens.rpy:1417
    old "## Since a mouse may not be present, we replace the quick menu with a version that uses fewer and bigger buttons that are easier to touch."
    new "## Якщо миша може не використовуватися, ми замінили швидке меню версією, що використовує менше кнопок, але великих за розміром, щоб їх було легше натискати.."

    # gui/game/screens.rpy:1435
    old "Menu"
    new "Меню"

# TODO: Translation updated at 2020-04-22 02:28

translate ukrainian strings:

    # gui/game/screens.rpy:333
    old "## The quit button is banned on iOS and unnecessary on Android and Web."
    new "Кнопка виходу заборонена на iOS та непотрібна в Android і Web"

