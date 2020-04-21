# TODO: Translation updated at 2019-08-28 02:04

translate ukrainian strings:

    # gui/game/options.rpy:1
    old "## This file contains options that can be changed to customize your game."
    new "## Цей файл містить настройки для підлаштування гри ???."

    # gui/game/options.rpy:4
    old "## Lines beginning with two '#' marks are comments, and you shouldn't uncomment them. Lines beginning with a single '#' mark are commented-out code, and you may want to uncomment them when appropriate."
    new "## Рядки, що починаються двома знаками '#' — коментарі й діставати їх не варто. Рядки, що починаються одним знаком '#' — are commented-out code, and you may want to uncomment them when appropriate. ???"

    # gui/game/options.rpy:10
    old "## Basics"
    new "## Основи"

    # gui/game/options.rpy:12
    old "## A human-readable name of the game. This is used to set the default window title, and shows up in the interface and error reports."
    new "## «Людська» назва гри. Вона впливає на заголовок вікна, з'являється у помилках та інтерфейсі."

    # gui/game/options.rpy:15
    old "## The _() surrounding the string marks it as eligible for translation."
    new "## _() навколишній рядок позначає її як придатну для перекладу ???."

    # gui/game/options.rpy:17
    old "Ren'Py 7 Default GUI"
    new "Усталений інтерфейс Ren'Py 7"

    # gui/game/options.rpy:20
    old "## Determines if the title given above is shown on the main menu screen. Set this to False to hide the title."
    new "## Визначає, чи вказаний вище заголовок на екрані головного меню. Установіть це значення False, щоб приховати заголовок."

    # gui/game/options.rpy:26
    old "## The version of the game."
    new "## Версія гри."

    # gui/game/options.rpy:31
    old "## Text that is placed on the game's about screen. Place the text between the triple-quotes, and leave a blank line between paragraphs."
    new "## Текст, розташований на екрані «Про гру». Текст повинен бути між потрійними лапками, а між абзацами потрібно залишати пустий рядок."

    # gui/game/options.rpy:38
    old "## A short name for the game used for executables and directories in the built distribution. This must be ASCII-only, and must not contain spaces, colons, or semicolons."
    new "## Коротка назва гри, яка використовується для виконуваних файлів та путей у вбудованому дистрибутиві. Це повинно бути лише ASCII, і не повинно містити проґалин, колонок чи крапки з комою ???."

    # gui/game/options.rpy:45
    old "## Sounds and music"
    new "## Звуки та музика"

    # gui/game/options.rpy:47
    old "## These three variables control which mixers are shown to the player by default. Setting one of these to False will hide the appropriate mixer."
    new "## Ці три змінні визначають мікшери, що показуватимуться гравцю за усталенням. Змінюючи одну з них на False, ви сховаєте відповідний мікшер ???."

    # gui/game/options.rpy:56
    old "## To allow the user to play a test sound on the sound or voice channel, uncomment a line below and use it to set a sample sound to play."
    new "## Щоб дозволити користувачеві відтворювати випробувальні звуки у звуковому чи голосовому каналі, дістаньте з коментаря вказаний внизу рядок та вкажіть випробувальний звук."

    # gui/game/options.rpy:63
    old "## Uncomment the following line to set an audio file that will be played while the player is at the main menu. This file will continue playing into the game, until it is stopped or another file is played."
    new "## Заберіть цей рядок з коментарів, аби виставити звуковий файл, що програватиметься, поки гравець знаходиться у головному меню. Цей файл продовжить грати, поки його не буде зупинено чи допоки не запуститься інший файл."

    # gui/game/options.rpy:70
    old "## Transitions"
    new "## Переходи"

    # gui/game/options.rpy:72
    old "## These variables set transitions that are used when certain events occur. Each variable should be set to a transition, or None to indicate that no transition should be used."
    new "## Ці змінні визначають переходи, що використовуються після певних подій. Кожна змінна повинна бути виставлена як перехід чи None (щоби вказати, що переходу немає)."

    # gui/game/options.rpy:76
    old "## Entering or exiting the game menu."
    new "## Вхід та вихід з ігрового меню."

    # gui/game/options.rpy:82
    old "## Between screens of the game menu."
    new "## Між екранами ігрового меню."

    # gui/game/options.rpy:87
    old "## A transition that is used after a game has been loaded."
    new "## Перехід, що використовується по завантаженню гри."

    # gui/game/options.rpy:92
    old "## Used when entering the main menu after the game has ended."
    new "## При вході до ігрового меню після закінчення гри."

    # gui/game/options.rpy:97
    old "## A variable to set the transition used when the game starts does not exist. Instead, use a with statement after showing the initial scene."
    new "## Змінна, що виставляє перехід на початку гри, не існує. Замість того, використайте твердження with після показу початкової сцени ???."

    # gui/game/options.rpy:102
    old "## Window management"
    new "## Управління вікнами"

    # gui/game/options.rpy:104
    old "## This controls when the dialogue window is displayed. If \"show\", it is always displayed. If \"hide\", it is only displayed when dialogue is present. If \"auto\", the window is hidden before scene statements and shown again once dialogue is displayed."
    new "## Визначає умови показу діаголового вікна. Якщо виставлено \"show\", вікно буде завжди присутнім. Якщо ж виставлено значення \"hide\", воно відображатиметься тільки коли програється діалог. При \"auto\", вікно ховатиметься перед сценами і з'являтиметься, коли програється діалог."

    # gui/game/options.rpy:109
    old "## After the game has started, this can be changed with the \"window show\", \"window hide\", and \"window auto\" statements."
    new "## Коли гру почато, це значення можна змінити на \"window show\", \"window hide\", та \"window auto\"."

    # gui/game/options.rpy:115
    old "## Transitions used to show and hide the dialogue window"
    new "## Переходи появи та зникнення діалогового вікна"

    # gui/game/options.rpy:121
    old "## Preference defaults"
    new "## Усталені налаштування"

    # gui/game/options.rpy:123
    old "## Controls the default text speed. The default, 0, is infinite, while any other number is the number of characters per second to type out."
    new "## Визначає усталену швидкість тексту. Типове значення, 0, позначає нескінченність, а будь-яке інше число визначатиме кількість видрукуваних знаків за секунду."

    # gui/game/options.rpy:129
    old "## The default auto-forward delay. Larger numbers lead to longer waits, with 0 to 30 being the valid range."
    new "## Усталена затримка самоперекидання ???. Що більші числа, то довше очікування. Припустимі значення від 0 до 30."

    # gui/game/options.rpy:135
    old "## Save directory"
    new "## Путь для збереження"

    # gui/game/options.rpy:137
    old "## Controls the platform-specific place Ren'Py will place the save files for this game. The save files will be placed in:"
    new "## Визначає місце (залежне від платформи), де Ren'Py зберігатиме файли прогресу для цієї гри. Файли прогресу з'являтимуться у:"

    # gui/game/options.rpy:140
    old "## Windows: %APPDATA\\RenPy\\<config.save_directory>"
    new "## Windows: %APPDATA\\RenPy\\<config.save_directory>"

    # gui/game/options.rpy:142
    old "## Macintosh: $HOME/Library/RenPy/<config.save_directory>"
    new "## Macintosh: $HOME/Library/RenPy/<config.save_directory>"

    # gui/game/options.rpy:144
    old "## Linux: $HOME/.renpy/<config.save_directory>"
    new "## Linux: $HOME/.renpy/<config.save_directory>"

    # gui/game/options.rpy:146
    old "## This generally should not be changed, and if it is, should always be a literal string, not an expression."
    new "## Загалом, це значення краще не змінювати, але якщо вже на те пішло, використовувати можна лише буквальний рядок, а не вираз ???."

    # gui/game/options.rpy:152
    old "## Icon"
    new "## Значок"

    # gui/game/options.rpy:154
    old "## The icon displayed on the taskbar or dock."
    new "## Значок, що відображатиметься на панелі завдань чи у доці ???."

    # gui/game/options.rpy:159
    old "## Build configuration"
    new "## Настройка збірки"

    # gui/game/options.rpy:161
    old "## This section controls how Ren'Py turns your project into distribution files."
    new "## Цей відділ визначає те, як Ren'Py перетворює проєкт на дистрибутивні файли.."

    # gui/game/options.rpy:166
    old "## The following functions take file patterns. File patterns are case- insensitive, and matched against the path relative to the base directory, with and without a leading /. If multiple patterns match, the first is used."
    new "## Вказані тут функції є файловими зразками. Ці зразки є нечутливими до регістру та починаються з відносного шляху основної папки, з чи без знаку /. Якщо спрацьовують кілька зразків, використовується перший з них ???."

    # gui/game/options.rpy:171
    old "## In a pattern:"
    new "## За зразком:"

    # gui/game/options.rpy:173
    old "## / is the directory separator."
    new "## / розділяє папки."

    # gui/game/options.rpy:175
    old "## * matches all characters, except the directory separator."
    new "## * відповідає усім знакам, окрім розділителя папок."

    # gui/game/options.rpy:177
    old "## ** matches all characters, including the directory separator."
    new "## ** відповідає усім знакам, навіть розділитель папок."

    # gui/game/options.rpy:179
    old "## For example, \"*.txt\" matches txt files in the base directory, \"game/**.ogg\" matches ogg files in the game directory or any of its subdirectories, and \"**.psd\" matches psd files anywhere in the project."
    new "## Наприклад, \"*.txt\" відповідає текстовим файлам в основній папці; \"game/**.ogg\" — ogg файлам у game та підпапках, а \"**.psd\" відповідатиме psd файлам будь-де всередині проєкту."

    # gui/game/options.rpy:183
    old "## Classify files as None to exclude them from the built distributions."
    new "## Позначаючи файли як None, ви виключите їх із зібраного дистрибутива ???."

    # gui/game/options.rpy:191
    old "## To archive files, classify them as 'archive'."
    new "## Щоб архівувати файли, позначте їх з допомогою 'archive'."

    # gui/game/options.rpy:196
    old "## Files matching documentation patterns are duplicated in a mac app build, so they appear in both the app and the zip file."
    new "## Файли на зразок документації подвоюються у збірці додатку для mac, тому вони з'являтимуться і в додатку, і у zip-файлі."

    # gui/game/options.rpy:202
    old "## Set this to a string containing your Apple Developer ID Application to enable codesigning on the Mac. Be sure to change it to your own Apple-issued ID."
    new "## Вставте сюди string свій Apple Developer ID Application, щоби зробити співпрацю доступною на Mac. Змініть на власний ідентифікатор, виданий Apple."

    # gui/game/options.rpy:209
    old "## A Google Play license key is required to download expansion files and perform in-app purchases. It can be found on the \"Services & APIs\" page of the Google Play developer console."
    new "## Вкажіть тут ліцензійний ключ Google Play, потрібний для стягнення файлів доповнень та здійснення покупок усередині гри. Його можна знайти на сторінці \"Services & APIs\" у розробницькій консолі Google Play."

    # gui/game/options.rpy:216
    old "## The username and project name associated with an itch.io project, separated by a slash."
    new "## Користувацьке ім'я та назва проєкту, прив'язані до проєкту itch.io, розділені скісною рискою."

