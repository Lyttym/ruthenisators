# TODO: Translation updated at 2019-08-28 02:04

translate ukrainian strings:

    # game/about.rpy:39
    old "[version!q]"
    new "[version!q]"

    # game/about.rpy:43
    old "View license"
    new "Показати ліцензію"

    # game/add_file.rpy:28
    old "FILENAME"
    new "НАЗВА ФАЙЛУ"

    # game/add_file.rpy:28
    old "Enter the name of the script file to create."
    new "Введіть назву файлу сценарію, який потрібно створити."

    # game/add_file.rpy:37
    old "The file name may not be empty."
    new "Назва файлу не може бути порожньою."

    # game/add_file.rpy:41
    old "The filename must have the .rpy extension."
    new "Назва файлу повинно мати розширення .rpy."

    # game/add_file.rpy:50
    old "The file already exists."
    new "Файл вже існує."

    # game/add_file.rpy:61
    old "# Ren'Py automatically loads all script files ending with .rpy. To use this\n# file, define a label and jump to it from another file.\n"
    new "# Ren'Py самочинно завантажує всі файли сценаріїв з розширенням .rpy. Щоб скористатися цим\n# файлом, визначте мітку та перейдіть до неї з іншого файлу.\n"

    # game/android.rpy:30
    old "To build Android packages, please download RAPT, unzip it, and place it into the Ren'Py directory. Then restart the Ren'Py launcher."
    new "Щоб створити пакунки Android, завантажте RAPT, розпакуйте та помістіть його в каталог Ren'Py. Потім перезапустіть запускач Ren'Py."

    # game/android.rpy:31
    old "A 64-bit/x64 Java 8 Development Kit is required to build Android packages on Windows. The JDK is different from the JRE, so it's possible you have Java without having the JDK.\n\nPlease {a=http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html}download and install the JDK{/a}, then restart the Ren'Py launcher."
    new "Для створення пакунків Android для Windows потрібен Java 8 Development Kit (розробницький набір) для 64-bit/x64 Java 8. JDK відрізняється від JRE, тому можливо, у вас є Java, не маючи JDK.\n\nБудь ласка {a=http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html}завантажте та встановіть JDK{/a}, потім перезапустіть запускач Ren'Py."

    # game/android.rpy:32
    old "RAPT has been installed, but you'll need to install the Android SDK before you can build Android packages. Choose Install SDK to do this."
    new "RAPT встановлено, але вам потрібно буде встановити Android SDK, перш ніж ви зможете створити пакунки Android. Для цього виберіть Встановити SDK."

    # game/android.rpy:33
    old "RAPT has been installed, but a key hasn't been configured. Please create a new key, or restore android.keystore."
    new "RAPT встановлено, але ключ не налаштований. Створіть новий ключ або відновіть android.keystore."

    # game/android.rpy:34
    old "The current project has not been configured. Use \"Configure\" to configure it before building."
    new "Поточний проєкт не налаштовано. Використовуйте \"Налаштувати\", щоб налаштувати його перед складанням."

    # game/android.rpy:35
    old "Choose \"Build\" to build the current project, or attach an Android device and choose \"Build & Install\" to build and install it on the device."
    new "Оберіть \"Скласти\" щоб скласти поточний проєкт або приєднати пристрій Android і вибрати \"Скласти & Встановити\" щоб скласти та встановити його на пристрої."

    # game/android.rpy:37
    old "Attempts to emulate an Android phone.\n\nTouch input is emulated through the mouse, but only when the button is held down. Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "Спроби відтворити смартфон Android.\n\nСенсорне введення удаває миша, але лише тоді, коли кнопка утримується. Escape відображається на кнопці меню, а PageUp - на кнопці назад. ???"

    # game/android.rpy:38
    old "Attempts to emulate an Android tablet.\n\nTouch input is emulated through the mouse, but only when the button is held down. Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "Спроби відтворити планшет Android.\n\nСенсорне введення удаває миша, але лише тоді, коли кнопка утримується. Escape відображається на кнопці меню, а PageUp - на кнопці назад."

    # game/android.rpy:39
    old "Attempts to emulate a televison-based Android console, like the OUYA or Fire TV.\n\nController input is mapped to the arrow keys, Enter is mapped to the select button, Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "Спроби відтворити a televison-based Android console, like the OUYA or Fire TV.\n\nController input is mapped to the arrow keys, Enter is mapped to the select button, Escape is mapped to the menu button, and PageUp is mapped to the back button."

    # game/android.rpy:41
    old "Downloads and installs the Android SDK and supporting packages. Optionally, generates the keys required to sign the package."
    new "Завантажує та встановлює Android SDK та допоміжні пакунки. За бажанням створює ключі, необхідні для підписання пакунку."

    # game/android.rpy:42
    old "Configures the package name, version, and other information about this project."
    new "Налаштування назви пакунку, версії та інших відомостей про цей проєкт."

    # game/android.rpy:43
    old "Opens the file containing the Google Play keys in the editor.\n\nThis is only needed if the application is using an expansion APK. Read the documentation for more details."
    new "Відкриває файл, що містить ключі Google Play в редакторі.\n\nЦе потрібно лише в тому випадку, якщо проґрама використовує розширення APK. Прочитайте документацію для отримання більш докладних відомостей."

    # game/android.rpy:44
    old "Builds the Android package."
    new "Складає пакунок Android."

    # game/android.rpy:45
    old "Builds the Android package, and installs it on an Android device connected to your computer."
    new "Складає пакунок Android та встановлює його на пристрої Android, підключеному до комп'ютера."

    # game/android.rpy:46
    old "Builds the Android package, installs it on an Android device connected to your computer, then launches the app on your device."
    new "Складає пакунок Android, встановлює його на пристрої Android, підключеному до комп'ютера, а потім запускає застосунок на цьому пристрої."

    # game/android.rpy:48
    old "Retrieves the log from the Android device and writes it to a file."
    new "Отримує журнал з пристрою Android і записує його у файл."

    # game/android.rpy:50
    old "Selects the Debug build, which can be accessed through Android Studio. Changing between debug and release builds requires an uninstall from your device."
    new "Вибирає збірку відлагодження, доступ до якої можна отримати через Android Studio. Для зміни відлагодження та випуску складання потрібне видалення з Вашого пристрою."

    # game/android.rpy:51
    old "Selects the Release build, which can be uploaded to stores. Changing between debug and release builds requires an uninstall from your device."
    new "??? Вибирає версію випуску, яку можна завантажити в крамниці. Для зміни відлагодження та випуску складання потрібне видалення з Вашого пристрою."

    # game/android.rpy:245
    old "Copying Android files to distributions directory."
    new "Копіювання файлів Android у каталог дистрибутивів ???."

    # game/android.rpy:313
    old "Android: [project.current.display_name!q]"
    new "Android: [project.current.display_name!q]"

    # game/android.rpy:333
    old "Emulation:"
    new "Відтворення:"

    # game/android.rpy:342
    old "Phone"
    new "Смартфон"

    # game/android.rpy:346
    old "Tablet"
    new "Планшет"

    # game/android.rpy:350
    old "Television"
    new "Телевізор"

    # game/android.rpy:362
    old "Build:"
    new "Збірка:"

    # game/android.rpy:377
    old "Release"
    new "Випуск"

    # game/android.rpy:384
    old "Install SDK & Create Keys"
    new "Встановити SDK & Створити ключі"

    # game/android.rpy:388
    old "Configure"
    new "Настроїти"

    # game/android.rpy:392
    old "Build Package"
    new "Скласти пакунок"

    # game/android.rpy:396
    old "Build & Install"
    new "Скласти & Встановити"

    # game/android.rpy:400
    old "Build, Install & Launch"
    new "Скласти, Встановити & Запустити"

    # game/android.rpy:411
    old "Other:"
    new "Інше:"

    # game/android.rpy:419
    old "Logcat"
    new "Logcat"

    # game/android.rpy:452
    old "Before packaging Android apps, you'll need to download RAPT, the Ren'Py Android Packaging Tool. Would you like to download RAPT now?"
    new "Перед упакуванням застосунків для Android вам потрібно буде завантажити RAPT - знаряддя для упакування Android Ren'Py. Хочете завантажити RAPT зараз?"

    # game/android.rpy:505
    old "Retrieving logcat information from device."
    new "Отримання відомостей з logcat з пристрою."

    # game/androidstrings.rpy:7
    old "{} is not a directory."
    new "{} не є каталогом."

    # game/androidstrings.rpy:8
    old "{} does not contain a Ren'Py game."
    new "{} не містить гру Ren'Py."

    # game/androidstrings.rpy:9
    old "Run configure before attempting to build the app."
    new "Запустіть конфіґурацію, перш ніж намагатися створити застосунок ???."

    # game/androidstrings.rpy:10
    old "Google Play support is enabled, but build.google_play_key is not defined."
    new "Google Play підтримка увімкнена, але build.google_play_key не визначено."

    # game/androidstrings.rpy:11
    old "Updating project."
    new "Оновлення проєкту."

    # game/androidstrings.rpy:12
    old "Creating assets directory."
    new "Створення каталогу асетів ???."

    # game/androidstrings.rpy:13
    old "Creating expansion file."
    new "Створення файлу розширення."

    # game/androidstrings.rpy:14
    old "Packaging internal data."
    new "Упакування внутрішніх даних."

    # game/androidstrings.rpy:15
    old "I'm using Gradle to build the package."
    new "Я використовую Gradle для створення пакунку."

    # game/androidstrings.rpy:16
    old "Uploading expansion file."
    new "Завантаження файлу розширення."

    # game/androidstrings.rpy:17
    old "The build seems to have failed."
    new "Здається, складання не вдалося."

    # game/androidstrings.rpy:18
    old "Launching app."
    new "Запуск застосунку."

    # game/androidstrings.rpy:19
    old "The build seems to have succeeded."
    new "Схоже, складання успішно завершено."

    # game/androidstrings.rpy:20
    old "The arm64-v8a version works on newer Android devices, the armeabi-v7a version works on older devices, and the x86_64 version works on the simulator and chromebooks."
    new "Версія arm64-v8a працює на новіших пристроях Android, версія Armeabi-v7a працює на старих пристроях, а версія x86_64 працює на симуляторі та хромбуках."

    # game/androidstrings.rpy:21
    old "What is the full name of your application? This name will appear in the list of installed applications."
    new "Як називається повна назва Вашого застосунку? Ця назва з’явиться у списку встановлених проґрам."

    # game/androidstrings.rpy:22
    old "What is the short name of your application? This name will be used in the launcher, and for application shortcuts."
    new "Яке коротке найменування Вашого застосунку? Ця назва буде використана як у запускачі, так і для ярликів застосунків ???."

    # game/androidstrings.rpy:23
    old "What is the name of the package?\n\nThis is usually of the form com.domain.program or com.domain.email.program. It may only contain ASCII letters and dots. It must contain at least one dot."
    new "Як називається пакунок?\n\nЗазвичай назва має форму com.domain.program або com.domain.email.program. Вона може містити лише ASCII букви та крапки. Вона повинна містити хоча б одну крапку."

    # game/androidstrings.rpy:24
    old "The package name may not be empty."
    new "Ім'я пакунку може бути порожнім."

    # game/androidstrings.rpy:25
    old "The package name may not contain spaces."
    new "Назва пакунку може не містити проґалин."

    # game/androidstrings.rpy:26
    old "The package name must contain at least one dot."
    new "Назва пакету повинна містити принаймні одну крапку."

    # game/androidstrings.rpy:27
    old "The package name may not contain two dots in a row, or begin or end with a dot."
    new "Назва пакунку може не містити двох крапок підряд або починатися чи закінчуватися крапкою."

    # game/androidstrings.rpy:28
    old "Each part of the package name must start with a letter, and contain only letters, numbers, and underscores."
    new "Кожна частина назви пакунку повинна починатися з букви та містити лише букви, числа та підкреслення."

    # game/androidstrings.rpy:29
    old "{} is a Java keyword, and can't be used as part of a package name."
    new "{} є ключовим словом Java, і його не можна використовувати як частину назви пакунку."

    # game/androidstrings.rpy:30
    old "What is the application's version?\n\nThis should be the human-readable version that you would present to a person. It must contain only numbers and dots."
    new "Яка версія проґрами?\n\nЦе має бути версія, яку ви представили б людині. Вона повинен містити лише числа і крапки."

    # game/androidstrings.rpy:31
    old "The version number must contain only numbers and dots."
    new "Номер версії повинен містити лише числа та крапки ???."

    # game/androidstrings.rpy:32
    old "What is the version code?\n\nThis must be a positive integer number, and the value should increase between versions."
    new "Що таке код версії?\n\nЦе повинно бути додатне ціле число, а значення повинно зростати між версіями."

    # game/androidstrings.rpy:33
    old "The numeric version must contain only numbers."
    new "Числова версія повинна містити лише числа."

    # game/androidstrings.rpy:34
    old "How would you like your application to be displayed?"
    new "Як ви хочете, щоб Ваша проґрама відображалася?"

    # game/androidstrings.rpy:35
    old "In landscape orientation."
    new "У ландшафтній орієнтації ???."

    # game/androidstrings.rpy:36
    old "In portrait orientation."
    new "У портретній орієнтації ???."

    # game/androidstrings.rpy:37
    old "In the user's preferred orientation."
    new "У бажаній орієнтації користувача ???."

    # game/androidstrings.rpy:38
    old "Which app store would you like to support in-app purchasing through?"
    new "Через яку крамницю застосунків ви хочете підтримувати покупку через застосунок?"

    # game/androidstrings.rpy:39
    old "Google Play."
    new "Google Play."

    # game/androidstrings.rpy:40
    old "Amazon App Store."
    new "Amazon App Store."

    # game/androidstrings.rpy:41
    old "Both, in one app."
    new "Обидва, в одному застосунку."

    # game/androidstrings.rpy:42
    old "Neither."
    new "Ніде."

    # game/androidstrings.rpy:43
    old "Would you like to create an expansion APK?"
    new "Хочете створити розширення APK?"

    # game/androidstrings.rpy:44
    old "No. Size limit of 100 MB on Google Play, but can be distributed through other stores and sideloaded."
    new "Ні. Обмеження розміру до 100 Мб в Google Play, але його можна розповсюджувати через інші крамниці та завантажувати."

    # game/androidstrings.rpy:45
    old "Yes. 2 GB size limit, but won't work outside of Google Play. (Read the documentation to get this to work.)"
    new "Так. Обмеження розміром 2 Гб, але воно не працює за межами Google Play. (Прочитайте документацію, щоб змусити це працювати.)"

    # game/androidstrings.rpy:46
    old "Do you want to allow the app to access the Internet?"
    new "Ви бажаєте дозволити застосунку мати доступ до Всемережжя?"

    # game/androidstrings.rpy:47
    old "Do you want to automatically update the generated project?"
    new "Ви бажаєте самочинно оновлювати складений проєкт?"

    # game/androidstrings.rpy:48
    old "Yes. This is the best choice for most projects."
    new "Так. Це найкращий вибір для більшості проєктів."

    # game/androidstrings.rpy:49
    old "No. This may require manual updates when Ren'Py or the project configuration changes."
    new "Ні. Це може потребувати оновлень вручну, за зміни Ren'Py або конфіґурації проєкту."

    # game/androidstrings.rpy:50
    old "Unknown configuration variable: {}"
    new "Невідома змінна конфіґурації: {}"

    # game/androidstrings.rpy:51
    old "I'm compiling a short test program, to see if you have a working JDK on your system."
    new "Я компілюю коротку перевірочну проґраму, щоб побачити, чи працює JDK у Вашій системі."

    # game/androidstrings.rpy:52
    old "I was unable to use javac to compile a test file. If you haven't installed the Java Development Kit yet, please download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nThe JDK is different from the JRE, so it's possible you have Java without having the JDK. Without a working JDK, I can't continue."
    new "Я не зміг використати javac для компіляції перевірочного файлу. Якщо ви ще не встановили набір Java Development Kit, завантажте його з:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nJDK відрізняється від JRE, тому можливо, у вас є Java, не маючи JDK. Без JDK, що працює я не можу продовжувати."

    # game/androidstrings.rpy:53
    old "The version of Java on your computer does not appear to be JDK 8, which is the only version supported by the Android SDK. If you need to install JDK 8, you can download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nYou can also set the JAVA_HOME environment variable to use a different version of Java."
    new "Версія Java на Вашому комп'ютері не JDK 8, що є єдиною версією, підтримуваною Android SDK. Якщо вам потрібно встановити JDK 8, ви можете завантажити його з:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nВи також можете встановити змінну середовища JAVA_HOME для використання іншої версії Java."

    # game/androidstrings.rpy:54
    old "The JDK is present and working. Good!"
    new "JDK присутній і працює. Добре!"

    # game/androidstrings.rpy:55
    old "The Android SDK has already been unpacked."
    new "Android SDK вже розпаковано."

    # game/androidstrings.rpy:56
    old "Do you accept the Android SDK Terms and Conditions?"
    new "Чи приймаєте ви Загальні положення та умови Android SDK?"

    # game/androidstrings.rpy:57
    old "I'm downloading the Android SDK. This might take a while."
    new "Я завантажую Android SDK. Це може зайняти деякий час."

    # game/androidstrings.rpy:58
    old "I'm extracting the Android SDK."
    new "Я розпаковую Android SDK."

    # game/androidstrings.rpy:59
    old "I've finished unpacking the Android SDK."
    new "Я завершив розпакування Android SDK."

    # game/androidstrings.rpy:60
    old "I'm about to download and install the required Android packages. This might take a while."
    new "Я збираюся завантажити та встановити необхідні пакунки Android. Це може зайняти деякий час."

    # game/androidstrings.rpy:61
    old "I was unable to accept the Android licenses."
    new "Я не зміг прийняти ліцензії Android."

    # game/androidstrings.rpy:62
    old "I was unable to install the required Android packages."
    new "Не вдалося встановити необхідні пакунки Android."

    # game/androidstrings.rpy:63
    old "I've finished installing the required Android packages."
    new "Я завершив встановлення необхідних пакунків Android."

    # game/androidstrings.rpy:64
    old "You set the keystore yourself, so I'll assume it's how you want it."
    new "Ви самі встановили сховище ключів, тож я припускаю, що все так як задумано."

    # game/androidstrings.rpy:65
    old "You've already created an Android keystore, so I won't create a new one for you."
    new "Ви вже створили сховище ключів для Android, тому я не буду створювати нове для вас"

    # game/androidstrings.rpy:66
    old "I can create an application signing key for you. Signing an application with this key allows it to be placed in the Android Market and other app stores.\n\nDo you want to create a key?"
    new "Я можу створити для вас ключ підписання застосунку. Підписання застосунку за допомогою цього ключа дозволяє розміщувати його в Android Market та інших крамницях застосунків.\n\nВи бажаєте створити ключ?"

    # game/androidstrings.rpy:67
    old "I will create the key in the android.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\n\\You also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of android.keystore, and keep it in a safe place?"
    new "Я створю ключ в файлі android.keystore.\n\nВам потрібно створити запасну копію цього файлу. Якщо ви втратите її, ви не зможете оновити свій застосунок.\n\n\\Також потрібно зберігати ключ у безпеці. Якщо злочинці отримають цей файл, вони можуть зробити підроблені версії Вашого застосунку та можливо вкрасти дані Ваших користувачів.\n\nЧи будете ви робити запасну копію android.keystore та зберігати її в безпечному місці?"

    # game/androidstrings.rpy:68
    old "Please enter your name or the name of your organization."
    new "Введіть своє ім’я або назву Вашої орґанізації."

    # game/androidstrings.rpy:69
    old "Could not create android.keystore. Is keytool in your path?"
    new "Не вдалося створити android.keystore. Чи keytool є у Вашому каталозі?"

    # game/androidstrings.rpy:70
    old "I've finished creating android.keystore. Please back it up, and keep it in a safe place."
    new "Я завершив створення android.keystore. Будь ласка, створіть запасні копії та зберігайте їх у безпечному місці."

    # game/androidstrings.rpy:71
    old "It looks like you're ready to start packaging games."
    new "Схоже, ви готові розпочати складання ігор."

    # game/choose_directory.rpy:88
    old "Ren'Py was unable to run python with tkinter to choose the directory. Please install the python-tk or tkinter package."
    new "Ren'Py не зміг запустити python з tkinter для вибору каталогу. Встановіть пакунок python-tk або tkinter."

    # game/choose_directory.rpy:106
    old "The selected projects directory is not writable."
    new "Вибраний каталог проєктів не підлягає запису."

    # game/choose_theme.rpy:303
    old "Could not change the theme. Perhaps options.rpy was changed too much."
    new "Не вдалося змінити тему. Можливо, options.rpy були змінені занадто сильно."

    # game/choose_theme.rpy:370
    old "Planetarium"
    new "Планетарій"

    # game/choose_theme.rpy:425
    old "Choose Theme"
    new "Оберіть тему"

    # game/choose_theme.rpy:438
    old "Theme"
    new "Тема"

    # game/choose_theme.rpy:463
    old "Color Scheme"
    new "Кольорова тема"

    # game/choose_theme.rpy:495
    old "Continue"
    new "Продовжити"

    # game/choose_theme.rpy:507
    old "changing the theme"
    new "зміна теми"

    # game/consolecommand.rpy:84
    old "INFORMATION"
    new "ВІДОМОСТІ"

    # game/consolecommand.rpy:84
    old "The command is being run in a new operating system console window."
    new "Команда виконується у новому вікні консолі операційної системи."

    # game/distribute.rpy:445
    old "Scanning project files..."
    new "Зчитування файлів проєкту..."

    # game/distribute.rpy:461
    old "Building distributions failed:\n\nThe build.directory_name variable may not include the space, colon, or semicolon characters."
    new "??? Помилка побудови дистрибутивів:\n\nЗмінна build.directory_name не може містити знаків проґалини, двокрапки або крапки з комою."

    # game/distribute.rpy:506
    old "No packages are selected, so there's nothing to do."
    new "Пакунки не обрані, тому нічого робити."

    # game/distribute.rpy:518
    old "Scanning Ren'Py files..."
    new "Зчитування файлів Ren'Py..."

    # game/distribute.rpy:577
    old "All packages have been built.\n\nDue to the presence of permission information, unpacking and repacking the Linux and Macintosh distributions on Windows is not supported."
    new "Усі пакунки складено.\n\nЧерез наявність відомостей про дозвіл розпакування та перепакування дистрибутивів Linux та Macintosh у Windows не підтримується ???."

    # game/distribute.rpy:760
    old "Archiving files..."
    new "Запакування файлів..."

    # game/distribute.rpy:1082
    old "Unpacking the Macintosh application for signing..."
    new "Розпакування застосунку Macintosh для підписання..."

    # game/distribute.rpy:1092
    old "Signing the Macintosh application...\n(This may take a long time.)"
    new "Підписання застосунку Macintosh...\n(This may take a long time.)"

    # game/distribute.rpy:1114
    old "Creating the Macintosh DMG..."
    new "Створення Macintosh DMG..."

    # game/distribute.rpy:1123
    old "Signing the Macintosh DMG..."
    new "Підписання Macintosh DMG..."

    # game/distribute.rpy:1318
    old "Writing the [variant] [format] package."
    new "Запис [variant] [format] пакунку ???."

    # game/distribute.rpy:1331
    old "Making the [variant] update zsync file."
    new "Створення [variant] оновлення файлу zsync."

    # game/distribute.rpy:1441
    old "Processed {b}[complete]{/b} of {b}[total]{/b} files."
    new "Обробляється {b}[complete]{/b} з {b}[total]{/b} файлів."

    # game/distribute_gui.rpy:157
    old "Build Distributions: [project.current.display_name!q]"
    new "Дистрибутиви складання: [project.current.display_name!q]"

    # game/distribute_gui.rpy:171
    old "Directory Name:"
    new "Назва каталогу:"

    # game/distribute_gui.rpy:175
    old "Executable Name:"
    new "Назва виконуваного файлу:"

    # game/distribute_gui.rpy:185
    old "Actions:"
    new "Дії:"

    # game/distribute_gui.rpy:193
    old "Edit options.rpy"
    new "Правити options.rpy"

    # game/distribute_gui.rpy:194
    old "Add from clauses to calls, once"
    new "Одинично додати функціи from до calls"

    # game/distribute_gui.rpy:195
    old "Refresh"
    new "Оновити"

    # game/distribute_gui.rpy:199
    old "Upload to itch.io"
    new "Завантажити в itch.io"

    # game/distribute_gui.rpy:215
    old "Build Packages:"
    new "Пакунки складання:"

    # game/distribute_gui.rpy:234
    old "Options:"
    new "Налаштування:"

    # game/distribute_gui.rpy:239
    old "Build Updates"
    new "Оновлення складання"

    # game/distribute_gui.rpy:241
    old "Add from clauses to calls"
    new "Додати функції from до calls"

    # game/distribute_gui.rpy:242
    old "Force Recompile"
    new "Примусово рекомпілювати"

    # game/distribute_gui.rpy:246
    old "Build"
    new "Скласти"

    # game/distribute_gui.rpy:250
    old "Adding from clauses to call statements that do not have them."
    new "Додавання функції from до операторів call, якщо вони їх не мають."

    # game/distribute_gui.rpy:271
    old "Errors were detected when running the project. Please ensure the project runs without errors before building distributions."
    new "Помилки були виявлені під час запуску проєкту. Будь ласка, переконайтеся, що проєкт працює без помилок перед складанням дистрибутивів. ???"

    # game/distribute_gui.rpy:288
    old "Your project does not contain build information. Would you like to add build information to the end of options.rpy?"
    new "Ваш проєкт не містить відомостей про збірку. Ви бажаєте додати відомості про збірку до кінця options.rpy?"

    # game/dmgcheck.rpy:50
    old "Ren'Py is running from a read only folder. Some functionality will not work."
    new "Ren'Py працює з каталогами лише для читання. Деякі можливості не працюватимуть."

    # game/dmgcheck.rpy:50
    old "This is probably because Ren'Py is running directly from a Macintosh drive image. To fix this, quit this launcher, copy the entire %s folder somewhere else on your computer, and run Ren'Py again."
    new "Це, мабуть, тому, що Ren'Py працює безпосередньо із образом диска Macintosh. Щоб виправити це, закрийте цей запускач, скопіюйте весь %s каталог де-небудь ще на Вашому обчислювач та знову запустіть Ren'Py."

    # game/editor.rpy:152
    old "(Recommended) A modern and approachable text editor."
    new "(Пораджено) Сучасний і доступний текстовий редактор."

    # game/editor.rpy:164
    old "Up to 150 MB download required."
    new "Потрібно завантажити до 150 Мб."

    # game/editor.rpy:178
    old "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input."
    new "Перевірений часом редактор. У редакторі відсутня підтримка IME, необхідна для введення тексту китайською, японською та корейською мовами."

    # game/editor.rpy:179
    old "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input. On Linux, Editra requires wxPython."
    new "Перевірений часом редактор. У редакторі відсутня підтримка IME, необхідна для введення тексту китайською, японською та корейською мовами. У Linux для правлення потрібен wxPython."

    # game/editor.rpy:195
    old "This may have occured because wxPython is not installed on this system."
    new "Це може статися через те, що wxPython не встановлений у цій системі."

    # game/editor.rpy:197
    old "Up to 22 MB download required."
    new "Потрібно завантажити до 22 Мб."

    # game/editor.rpy:210
    old "A mature editor that requires Java."
    new "Перевірений часом редактор, якому потрібна Java."

    # game/editor.rpy:210
    old "1.8 MB download required."
    new "Потрібне завантаження 1.8 Мб."

    # game/editor.rpy:210
    old "This may have occured because Java is not installed on this system."
    new "Це може статися через те, що Java не встановлена в цій системі."

    # game/editor.rpy:219
    old "System Editor"
    new "Системний редактор"

    # game/editor.rpy:219
    old "Invokes the editor your operating system has associated with .rpy files."
    new "Викликає редактор, у якому Ваша операційна система пов’язана з файлами .rpy."

    # game/editor.rpy:235
    old "None"
    new "Немає"

    # game/editor.rpy:235
    old "Prevents Ren'Py from opening a text editor."
    new "Заважає Ren'Py відкривати текстовий редактор."

    # game/editor.rpy:338
    old "Edit [text]."
    new "Правити [text]."

    # game/editor.rpy:387
    old "An exception occured while launching the text editor:\n[exception!q]"
    new "Стався виняток під час запуску текстового редактора:\n[exception!q]"

    # game/editor.rpy:519
    old "Select Editor"
    new "Оберіть редактор"

    # game/editor.rpy:534
    old "A text editor is the program you'll use to edit Ren'Py script files. Here, you can select the editor Ren'Py will use. If not already present, the editor will be automatically downloaded and installed."
    new "Текстовий редактор - це проґрама, яку ви використовуєте для правлення файлів сценаріїв Ren'Py. Тут ви можете вибрати редактор, який буде використовувати Ren'Py. Якщо його ще немає, редактор самочинно завантажується та встановлюється."

    # game/front_page.rpy:35
    old "Open [text] directory."
    new "Відкрити каталог [text]."

    # game/front_page.rpy:91
    old "PROJECTS:"
    new "ПРОЄКТИ:"

    # game/front_page.rpy:93
    old "refresh"
    new "оновити"

    # game/front_page.rpy:120
    old "+ Create New Project"
    new "+ Створити новий проєкт"

    # game/front_page.rpy:130
    old "Launch Project"
    new "Запустити проєкт"

    # game/front_page.rpy:147
    old "[p.name!q] (template)"
    new "[p.name!q] (template)"

    # game/front_page.rpy:149
    old "Select project [text]."
    new "Вибрати проєкт [text]."

    # game/front_page.rpy:165
    old "Tutorial"
    new "Посібник"

    # game/front_page.rpy:166
    old "The Question"
    new "Велике питання"

    # game/front_page.rpy:182
    old "Active Project"
    new "Поточний проєкт"

    # game/front_page.rpy:190
    old "Open Directory"
    new "Відкрити каталог"

    # game/front_page.rpy:195
    old "game"
    new "game"

    # game/front_page.rpy:196
    old "base"
    new "base"

    # game/front_page.rpy:197
    old "images"
    new "images"

    # game/front_page.rpy:198
    old "gui"
    new "gui"

    # game/front_page.rpy:204
    old "Edit File"
    new "Правити файл"

    # game/front_page.rpy:215
    old "Open project"
    new "Відкрити проєкт"

    # game/front_page.rpy:217
    old "All script files"
    new "Усі файли сценаріїв"

    # game/front_page.rpy:221
    old "Actions"
    new "Дії"

    # game/front_page.rpy:230
    old "Navigate Script"
    new "Навіґація по сценарію"

    # game/front_page.rpy:231
    old "Check Script (Lint)"
    new "Перевірити сценарій (Lint)"

    # game/front_page.rpy:234
    old "Change/Update GUI"
    new "Змінити/Оновити інтерфейс"

    # game/front_page.rpy:236
    old "Change Theme"
    new "Змінити тему"

    # game/front_page.rpy:239
    old "Delete Persistent"
    new "Видалити сталі"

    # game/front_page.rpy:248
    old "Build Distributions"
    new "Скласти дистрибутив"

    # game/front_page.rpy:250
    old "Android"
    new "Android"

    # game/front_page.rpy:251
    old "iOS"
    new "iOS"

    # game/front_page.rpy:252
    old "Web"
    new "Web"

    # game/front_page.rpy:252
    old "(Beta)"
    new "(Beta)"

    # game/front_page.rpy:253
    old "Generate Translations"
    new "Утворити переклади"

    # game/front_page.rpy:254
    old "Extract Dialogue"
    new "Витягти розмови"

    # game/front_page.rpy:271
    old "Checking script for potential problems..."
    new "Перевірка сценарію на наявність можливих проблем..."

    # game/front_page.rpy:286
    old "Deleting persistent data..."
    new "Видалення сталих даних..."

    # game/front_page.rpy:294
    old "Recompiling all rpy files into rpyc files..."
    new "Компіляція наново всіх .rpy та .rpyc файлів..."

    # game/gui7.rpy:252
    old "Select Accent and Background Colors"
    new "Виберіть наголошені барви та тло"

    # game/gui7.rpy:266
    old "Please click on the color scheme you wish to use, then click Continue. These colors can be changed and customized later."
    new "Клацніть на барвовій гамі, яку ви хочете використовувати, а потім натисніть Продовжити. Ці барви можна змінити та налаштувати пізніше."

    # game/gui7.rpy:311
    old "{b}Warning{/b}\nContinuing will overwrite customized bar, button, save slot, scrollbar, and slider images.\n\nWhat would you like to do?"
    new "{b}Увага{/b}\nПродовження замінить налаштовані панелі, кнопки, зберегти комірку, смугу прокрутки та ковзач ???.\n\nЩо б Ви хотіли зробити?"

    # game/gui7.rpy:311
    old "Choose new colors, then regenerate image files."
    new "Виберіть нові барви, а потім відновіть файли зображень."

    # game/gui7.rpy:311
    old "Regenerate the image files using the colors in gui.rpy."
    new "Переродити файли зображень за допомогою барв у gui.rpy."

    # game/gui7.rpy:339
    old "What resolution should the project use? Although Ren'Py can scale the window up and down, this is the initial size of the window, the size at which assets should be drawn, and the size at which the assets will be at their sharpest.\n\nThe default of 1280x720 is a reasonable compromise."
    new "Яку роздільну здатність повинен використовувати проєкт? Хоча Ren'Py може збільшувати вікно вгору та вниз, це початковий розмір вікна, розмір, на якому потрібно намалювати дії, і розмір, при якому дії будуть найменшими.\n\nУсталено 1280x720 є розумним рішенням."

    # game/gui7.rpy:339
    old "Custom. The GUI is optimized for a 16:9 aspect ratio."
    new "Користувацькі. GUI увигіднено для співвідношення сторін 16:9."

    # game/gui7.rpy:355
    old "WIDTH"
    new "ШИРИНА"

    # game/gui7.rpy:355
    old "Please enter the width of your game, in pixels."
    new "Введіть, будь ласка, ширину екрана Вашої гри, у пікселях."

    # game/gui7.rpy:365
    old "The width must be a number."
    new "Ширина повинна бути числом."

    # game/gui7.rpy:371
    old "HEIGHT"
    new "ВИСОТА"

    # game/gui7.rpy:371
    old "Please enter the height of your game, in pixels."
    new "Введіть, будь ласка, висоту екрана Вашої гри, у пікселях."

    # game/gui7.rpy:381
    old "The height must be a number."
    new "Висота повинна бути числом."

    # game/gui7.rpy:425
    old "Creating the new project..."
    new "Створення нового проєкту..."

    # game/gui7.rpy:427
    old "Updating the project..."
    new "Оновлення проєкту..."

    # game/gui7.rpy:429
    old "creating a new project"
    new "створення нового проєкту"

    # game/gui7.rpy:433
    old "activating the new project"
    new "задіювання нового проєкту"

    # game/interface.rpy:119
    old "Documentation"
    new "Документація"

    # game/interface.rpy:120
    old "Ren'Py Website"
    new "Ren'Py вебсайт"

    # game/interface.rpy:121
    old "Ren'Py Games List"
    new "Ren'Py список ігор"

    # game/interface.rpy:129
    old "update"
    new "оновлення"

    # game/interface.rpy:131
    old "preferences"
    new "налаштування"

    # game/interface.rpy:132
    old "quit"
    new "вихід"

    # game/interface.rpy:136
    old "Ren'Py Sponsor Information"
    new "Ren'Py Відомості про коштодавців"

    # game/interface.rpy:264
    old "Due to package format limitations, non-ASCII file and directory names are not allowed."
    new "Через обмеження формату пакунку, не-ASCII імена файлів та каталогів заборонені."

    # game/interface.rpy:360
    old "ERROR"
    new "ПОМИЛКА"

    # game/interface.rpy:372
    old "opening the log file"
    new "відкриття файлу журналу"

    # game/interface.rpy:394
    old "While [what!qt], an error occured:"
    new "Поки [what!qt], виникла помилка:"

    # game/interface.rpy:394
    old "[exception!q]"
    new "[exception!q]"

    # game/interface.rpy:427
    old "Text input may not contain the {{ or [[ characters."
    new "Введення тексту може не містити {{ або [[ знаків."

    # game/interface.rpy:432
    old "File and directory names may not contain / or \\."
    new "Назви файлів і каталогів можуть не містити / або \\."

    # game/interface.rpy:438
    old "File and directory names must consist of ASCII characters."
    new "Назви файлів і каталогів повинні складатися зі знаків ASCII."

    # game/interface.rpy:506
    old "PROCESSING"
    new "ОБРОБКА"

    # game/interface.rpy:523
    old "QUESTION"
    new "ПИТАННЯ"

    # game/interface.rpy:536
    old "CHOICE"
    new "ВИБІР"

    # game/ios.rpy:28
    old "To build iOS packages, please download renios, unzip it, and place it into the Ren'Py directory. Then restart the Ren'Py launcher."
    new "Щоб створити пакунки iOS, завантажте renios, розпакуйте та помістіть їх у каталог Ren'Py. Потім перезапустіть пусковий апарат Ren'Py."

    # game/ios.rpy:29
    old "The directory in where Xcode projects will be placed has not been selected. Choose 'Select Directory' to select it."
    new "Каталог, де розміщуватимуться проєкти Xcode, не обраний. Оберіть «Вибрати каталог», щоб вибрати його."

    # game/ios.rpy:30
    old "There is no Xcode project corresponding to the current Ren'Py project. Choose 'Create Xcode Project' to create one."
    new "Не існує проєкту Xcode, що відповідає поточному проєкту Ren'Py. Виберіть «Створити проєкт Xcode», щоб створити його."

    # game/ios.rpy:31
    old "An Xcode project exists. Choose 'Update Xcode Project' to update it with the latest game files, or use Xcode to build and install it."
    new "Проєкт Xcode існує. Виберіть «Оновити проєкт Xcode», щоб оновити його останніми ігровими файлами, або скористайтеся Xcode для його складання та встановлення."

    # game/ios.rpy:33
    old "Attempts to emulate an iPhone.\n\nTouch input is emulated through the mouse, but only when the button is held down."
    new "Спроби відтворити iPhone.\n\nСенсорне введення відтворюється мишею, але лише тоді, коли кнопка утримується."

    # game/ios.rpy:34
    old "Attempts to emulate an iPad.\n\nTouch input is emulated through the mouse, but only when the button is held down."
    new "Спроби відтворити iPad.\n\nСенсорне введення відтворюється мишею, але лише тоді, коли кнопка утримується."

    # game/ios.rpy:36
    old "Selects the directory where Xcode projects will be placed."
    new "Обирає каталог, де будуть розміщуватися проєкти Xcode."

    # game/ios.rpy:37
    old "Creates an Xcode project corresponding to the current Ren'Py project."
    new "Створює проєкт Xcode, що відповідає поточному проєкту Ren'Py."

    # game/ios.rpy:38
    old "Updates the Xcode project with the latest game files. This must be done each time the Ren'Py project changes."
    new "Оновлення проєкту Xcode за допомогою останніх ігрових файлів. Це потрібно робити щоразу, коли проєкт Ren'Py змінюється."

    # game/ios.rpy:39
    old "Opens the Xcode project in Xcode."
    new "Відкриває проєкт Xcode в Xcode."

    # game/ios.rpy:41
    old "Opens the directory containing Xcode projects."
    new "Відкриває каталог, що містить проєкти Xcode."

    # game/ios.rpy:131
    old "The Xcode project already exists. Would you like to rename the old project, and replace it with a new one?"
    new "Проєкт Xcode вже існує. Ви бажаєте перейменувати старий проєкт та замінити його на новий?"

    # game/ios.rpy:225
    old "iOS: [project.current.display_name!q]"
    new "iOS: [project.current.display_name!q]"

    # game/ios.rpy:254
    old "iPhone"
    new "iPhone"

    # game/ios.rpy:258
    old "iPad"
    new "iPad"

    # game/ios.rpy:278
    old "Select Xcode Projects Directory"
    new "Вибрати каталог проєктів Xcode"

    # game/ios.rpy:282
    old "Create Xcode Project"
    new "Створити проєкт Xcode"

    # game/ios.rpy:286
    old "Update Xcode Project"
    new "Оновити проєкт Xcode"

    # game/ios.rpy:291
    old "Launch Xcode"
    new "Запустити Xcode"

    # game/ios.rpy:326
    old "Open Xcode Projects Directory"
    new "Відкрийте каталог проєктів Xcode"

    # game/ios.rpy:359
    old "Before packaging iOS apps, you'll need to download renios, Ren'Py's iOS support. Would you like to download renios now?"
    new "Перед упакуванням застосунків для iOS вам потрібно завантажити renios, підтримку iOS Ren'Py. Бажаєте завантажити renios зараз?"

    # game/ios.rpy:368
    old "XCODE PROJECTS DIRECTORY"
    new "ПУТЬ ПРОЄКТІВ XCODE"

    # game/ios.rpy:368
    old "Please choose the Xcode Projects Directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"
    new "Виберіть каталог проєктів Xcode, використовуючи знаряддя вибору каталогу.\n{b}За цим вікном може відкритись обирач каталогу.{/b}"

    # game/ios.rpy:373
    old "Ren'Py has set the Xcode Projects Directory to:"
    new "Ren'Py встановив каталог проєктів Xcode на:"

    # game/itch.rpy:43
    old "Downloading the itch.io butler."
    new "Завантаження Itch.io butler."

    # game/itch.rpy:96
    old "The built distributions could not be found. Please choose 'Build' and try again."
    new "Убудованих дистрибутивів не вдалося знайти. Виберіть «Скласти» і повторіть спробу."

    # game/itch.rpy:134
    old "No uploadable files were found. Please choose 'Build' and try again."
    new "Не знайдено файлів, які можна завантажити. Виберіть «Скласти» і повторіть спробу."

    # game/itch.rpy:140
    old "The butler program was not found."
    new "Проґрама butler не знайдена."

    # game/itch.rpy:140
    old "Please install the itch.io app, which includes butler, and try again."
    new "Установіть застосунок itch.io, до якого входить butler, та спробуйте ще раз ???."

    # game/itch.rpy:149
    old "The name of the itch project has not been set."
    new "Назву itch-проєкту не встановлено."

    # game/itch.rpy:149
    old "Please {a=https://itch.io/game/new}create your project{/a}, then add a line like \n{vspace=5}define build.itch_project = \"user-name/game-name\"\n{vspace=5} to options.rpy."
    new "Будь ласка {a=https://itch.io/game/new}створіть новий проєкт{/a}, потім додайте рядок на зразок \n{vspace=5}define build.itch_project = \"user-name/game-name\"\n{vspace=5} до options.rpy."

    # game/mobilebuild.rpy:110
    old "{a=%s}%s{/a}"
    new "{a=%s}%s{/a}"

    # game/navigation.rpy:168
    old "Navigate: [project.current.display_name!q]"
    new "Навіґація ???: [project.current.display_name!q]"

    # game/navigation.rpy:178
    old "Order: "
    new "Впорядкування: "

    # game/navigation.rpy:179
    old "alphabetical"
    new "абетково"

    # game/navigation.rpy:181
    old "by-file"
    new "за файлом"

    # game/navigation.rpy:183
    old "natural"
    new "натурально"

    # game/navigation.rpy:195
    old "Category:"
    new "Катеґорія:"

    # game/navigation.rpy:198
    old "files"
    new "файли"

    # game/navigation.rpy:199
    old "labels"
    new "написи"

    # game/navigation.rpy:200
    old "defines"
    new "визначення"

    # game/navigation.rpy:201
    old "transforms"
    new "перетворення"

    # game/navigation.rpy:202
    old "screens"
    new "екрани"

    # game/navigation.rpy:203
    old "callables"
    new "викликовувані"

    # game/navigation.rpy:204
    old "TODOs"
    new "Списки завдань"

    # game/navigation.rpy:243
    old "+ Add script file"
    new "+ Додати файл сценарію"

    # game/navigation.rpy:251
    old "No TODO comments found.\n\nTo create one, include \"# TODO\" in your script."
    new "Не знайдено коментарів списку завдань.\n\nЩоб створити такий, включіть \"# TODO\" до Вашого скрипту."

    # game/navigation.rpy:258
    old "The list of names is empty."
    new "Список імен порожній."

    # game/new_project.rpy:38
    old "New GUI Interface"
    new "Новий інтерфейс GUI"

    # game/new_project.rpy:48
    old "Both interfaces have been translated to your language."
    new "Обидва інтерфейси перекладені Вашою мовою."

    # game/new_project.rpy:50
    old "Only the new GUI has been translated to your language."
    new "На Вашу мову перекладено лише новий графічний інтерфейс."

    # game/new_project.rpy:52
    old "Only the legacy theme interface has been translated to your language."
    new "На Вашу мову перекладено лише застарілий інтерфейс теми."

    # game/new_project.rpy:54
    old "Neither interface has been translated to your language."
    new "Жоден інтерфейс не перекладений Вашою мовою."

    # game/new_project.rpy:63
    old "The projects directory could not be set. Giving up."
    new "Не вдалося встановити каталог проєктів. Здаюся."

    # game/new_project.rpy:70
    old "Which interface would you like to use? The new GUI has a modern look, supports wide screens and mobile devices, and is easier to customize. Legacy themes might be necessary to work with older example code.\n\n[language_support!t]\n\nIf in doubt, choose the new GUI, then click Continue on the bottom-right."
    new "Який інтерфейс ви б хотіли використовувати? Новий графічний інтерфейс має сучасний вигляд, підтримує широкі екрани та стільникові пристрої, і його простіше налаштувати. Спадкові теми можуть знадобитися для роботи зі старшим прикладом коду.\n\n[language_support!t]\n\nЯкщо ви сумніваєтесь, виберіть новий графічний інтерфейс, а потім натисніть Продовжити внизу праворуч ???."

    # game/new_project.rpy:70
    old "Legacy Theme Interface"
    new "Старі теми інтерфейсу"

    # game/new_project.rpy:81
    old "You will be creating an [new_project_language]{#this substitution may be localized} language project. Change the launcher language in preferences to create a project in another language."
    new "Ви будете створювати проєкт українською мовою. Змініть мову запускача в налаштуваннях, щоб створити проєкт іншою мовою."

    # game/new_project.rpy:86
    old "PROJECT NAME"
    new "НАЗВА ПРОЄКТУ"

    # game/new_project.rpy:86
    old "Please enter the name of your project:"
    new "Введіть назву Вашого проєкту:"

    # game/new_project.rpy:96
    old "The project name may not be empty."
    new "Назва проєкту не може бути порожньою."

    # game/new_project.rpy:102
    old "[project_name!q] already exists. Please choose a different project name."
    new "[project_name!q] вже існує. Виберіть іншу назву проєкту."

    # game/new_project.rpy:106
    old "[project_dir!q] already exists. Please choose a different project name."
    new "[project_dir!q] вже існує. Виберіть іншу назву проєкту."

    # game/new_project.rpy:124
    old "Choose Project Template"
    new "Виберіть шаблон проєкту"

    # game/new_project.rpy:142
    old "Please select a template to use for your new project. The template sets the default font and the user interface language. If your language is not supported, choose 'english'."
    new "Виберіть шаблон для нового проєкту. Шаблон встановлює усталений шрифт та мову інтерфейсу користувача. Якщо Ваша мова не підтримується, виберіть «англійська мова»."

    # game/preferences.rpy:73
    old "Launcher Preferences"
    new "Налаштування запускача"

    # game/preferences.rpy:94
    old "Projects Directory:"
    new "Каталог місцезнаходження проєктів:"

    # game/preferences.rpy:101
    old "[persistent.projects_directory!q]"
    new "[persistent.projects_directory!q]"

    # game/preferences.rpy:103
    old "Projects directory: [text]"
    new "Каталог проєктів: [text]"

    # game/preferences.rpy:105
    old "Not Set"
    new "Не встановлено"

    # game/preferences.rpy:120
    old "Text Editor:"
    new "Текстовий редактор:"

    # game/preferences.rpy:126
    old "Text editor: [text]"
    new "Текстовий редактор: [text]"

    # game/preferences.rpy:145
    old "Navigation Options:"
    new "Налаштування навіґації:"

    # game/preferences.rpy:149
    old "Include private names"
    new "Включити особисті імена"

    # game/preferences.rpy:150
    old "Include library names"
    new "Включити назви бібліотек"

    # game/preferences.rpy:160
    old "Launcher Options:"
    new "Налаштування запускача:"

    # game/preferences.rpy:164
    old "Hardware rendering"
    new "Апаратне відмальовування"

    # game/preferences.rpy:165
    old "Show edit file section"
    new "Показати розділ правлення файлів"

    # game/preferences.rpy:166
    old "Large fonts"
    new "Великі написи"

    # game/preferences.rpy:169
    old "Console output"
    new "Виведення на консоль"

    # game/preferences.rpy:173
    old "Force new tutorial"
    new "Примусовий новий посібник"

    # game/preferences.rpy:177
    old "Legacy options"
    new "Увімкнути старі теми"

    # game/preferences.rpy:180
    old "Show templates"
    new "Відображати шаблони"

    # game/preferences.rpy:182
    old "Sponsor message"
    new "Повідомлення коштодавців"

    # game/preferences.rpy:202
    old "Open launcher project"
    new "Відкрити проєкт запускача"

    # game/preferences.rpy:216
    old "Language:"
    new "Мова:"

    # game/project.rpy:49
    old "After making changes to the script, press shift+R to reload your game."
    new "Після внесення змін у сценарій натисніть shift+R, щоб перезавантажити гру."

    # game/project.rpy:49
    old "Press shift+O (the letter) to access the console."
    new "Натисніть shift+O(буква), щоб отримати доступ до консолі."

    # game/project.rpy:49
    old "Press shift+D to access the developer menu."
    new "Натисніть shift+D, щоб перейти до меню розробника."

    # game/project.rpy:49
    old "Have you backed up your projects recently?"
    new "Ви створювали нещодавно запасну копію проєктів?"

    # game/project.rpy:281
    old "Launching the project failed."
    new "Запуск проєкту не вдався."

    # game/project.rpy:281
    old "Please ensure that your project launches normally before running this command."
    new "Переконайтеся, що Ваш проєкт запускається нормально перед запуском цієї вказівки."

    # game/project.rpy:297
    old "Ren'Py is scanning the project..."
    new "Ren'Py зчитує проєкт..."

    # game/project.rpy:729
    old "Launching"
    new "Запускання"

    # game/project.rpy:763
    old "PROJECTS DIRECTORY"
    new "КАТАЛОГ ПРОЄКТІВ"

    # game/project.rpy:763
    old "Please choose the projects directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"
    new "Виберіть каталог проектів за допомогою обирача каталогу.\n{b}За цим вікном, можливо, відкрився обирач каталогу.{/b}"

    # game/project.rpy:763
    old "This launcher will scan for projects in this directory, will create new projects in this directory, and will place built projects into this directory."
    new "Цей запускач зчитуватиме проєкти в цьому каталозі, створюватиме нові проєкти в цьому каталозі та розміщуватиме вбудовані проєкти у ньому."

    # game/project.rpy:768
    old "Ren'Py has set the projects directory to:"
    new "Ren'Py встановив каталог проєкту:"

    # game/translations.rpy:91
    old "Translations: [project.current.display_name!q]"
    new "Переклади: [project.current.display_name!q]"

    # game/translations.rpy:132
    old "The language to work with. This should only contain lower-case ASCII characters and underscores."
    new "Мова для опрацювання. Вона повинна містити тільки малі знаки ASCII і знак підкреслення."

    # game/translations.rpy:158
    old "Generate empty strings for translations"
    new "Створити порожні рядки для перекладів"

    # game/translations.rpy:176
    old "Generates or updates translation files. The files will be placed in game/tl/[persistent.translate_language!q]."
    new "Створює або оновлює файли перекладу. Файли будуть розміщені в game/tl/[persistent.translate_language!q]."

    # game/translations.rpy:196
    old "Extract String Translations"
    new "Витягнути рядки перекладів"

    # game/translations.rpy:198
    old "Merge String Translations"
    new "Об’єднати рядки перекладів"

    # game/translations.rpy:203
    old "Replace existing translations"
    new "Замінити наявні переклади"

    # game/translations.rpy:204
    old "Reverse languages"
    new "Узворотнити мови"

    # game/translations.rpy:208
    old "Update Default Interface Translations"
    new "Оновити усталені переклади інтерфейсу"

    # game/translations.rpy:228
    old "The extract command allows you to extract string translations from an existing project into a temporary file.\n\nThe merge command merges extracted translations into another project."
    new "Вказівка витягнення дозволяє вам витягти рядки перекладів з наявного проєкту у тимчасовий файл.\n\nВказівка на об'єднання об'єднує витягнені переклади в інший проєкт."

    # game/translations.rpy:252
    old "Ren'Py is generating translations...."
    new "Ren'Py утворює переклади...."

    # game/translations.rpy:263
    old "Ren'Py has finished generating [language] translations."
    new "Ren'Py завершив утворення перекладів мовою [language]."

    # game/translations.rpy:276
    old "Ren'Py is extracting string translations..."
    new "Ren'Py витягує рядки перекладів..."

    # game/translations.rpy:279
    old "Ren'Py has finished extracting [language] string translations."
    new "Ren'Py завершив витягнення рядків перекладів мовою [language]."

    # game/translations.rpy:299
    old "Ren'Py is merging string translations..."
    new "Ren'Py об'єднує рядки перекладів..."

    # game/translations.rpy:302
    old "Ren'Py has finished merging [language] string translations."
    new "Ren'Py завершив об'єднання рядків перекладів мовою [language]."

    # game/translations.rpy:313
    old "Updating default interface translations..."
    new "Оновлення усталених перекладів інтерфейсу..."

    # game/translations.rpy:342
    old "Extract Dialogue: [project.current.display_name!q]"
    new "Витягнути розмову: [project.current.display_name!q]"

    # game/translations.rpy:358
    old "Format:"
    new "Формат:"

    # game/translations.rpy:366
    old "Tab-delimited Spreadsheet (dialogue.tab)"
    new "Табульована таблиця (dialogue.tab)"

    # game/translations.rpy:367
    old "Dialogue Text Only (dialogue.txt)"
    new "Тільки текст розмов (dialogue.txt)"

    # game/translations.rpy:380
    old "Strip text tags from the dialogue."
    new "Скласти текстові мітки з розмов."

    # game/translations.rpy:381
    old "Escape quotes and other special characters."
    new "Включати лапки та інші реґулярні вирази."

    # game/translations.rpy:382
    old "Extract all translatable strings, not just dialogue."
    new "Витягнути усі рядки що можливо перекласти, а не лише розмови."

    # game/translations.rpy:410
    old "Ren'Py is extracting dialogue...."
    new "Ren'Py витягує розмови...."

    # game/translations.rpy:414
    old "Ren'Py has finished extracting dialogue. The extracted dialogue can be found in dialogue.[persistent.dialogue_format] in the base directory."
    new "Ren'Py завершив витягнення розмов. Витягнуті розмови можна знайти в діалозі.[persistent.dialogue_format] в базовій каталогу. ???"

    # game/updater.rpy:63
    old "{b}Recommended.{/b} The version of Ren'Py that should be used in all newly-released games."
    new "{b}Пораджено.{/b} Версія Ren'Py, яку слід використовувати у всіх щойно випущених іграх ???."

    # game/updater.rpy:65
    old "Prerelease"
    new "Передвипуск"

    # game/updater.rpy:66
    old "A preview of the next version of Ren'Py that can be used for testing and taking advantage of new features, but not for final releases of games."
    new "Попередній перегляд наступної версії Ren'Py, яку можна використовувати для перевірки та використання нових можливостей, але не для остаточного випуску ігор."

    # game/updater.rpy:68
    old "Experimental"
    new "Випробувальний"

    # game/updater.rpy:69
    old "Experimental versions of Ren'Py. You shouldn't select this channel unless asked by a Ren'Py developer."
    new "Випробувальні версії Ren'Py. Не слід вибирати цей канал, якщо не попросить розробник Ren'Py."

    # game/updater.rpy:71
    old "Nightly"
    new "Нічний"

    # game/updater.rpy:72
    old "The bleeding edge of Ren'Py development. This may have the latest features, or might not run at all."
    new "Найпередовіший в розвитку Ren'Py. Він може мати останні можливості, або може не працювати взагалі."

    # game/updater.rpy:90
    old "Select Update Channel"
    new "Виберіть канал оновлення"

    # game/updater.rpy:101
    old "The update channel controls the version of Ren'Py the updater will download."
    new "Канал оновлення керує версією Ren'Py, яку оновлювач завантажить."

    # game/updater.rpy:110
    old "• This version is installed and up-to-date."
    new "• Ця версія встановлена та оновлена."

    # game/updater.rpy:118
    old "%B %d, %Y"
    new "%B %d, %Y"

    # game/updater.rpy:140
    old "An error has occured:"
    new "Сталася помилка:"

    # game/updater.rpy:142
    old "Checking for updates."
    new "Перевірка оновлень."

    # game/updater.rpy:144
    old "Ren'Py is up to date."
    new "Ren'Py найновіший."

    # game/updater.rpy:146
    old "[u.version] is now available. Do you want to install it?"
    new "[u.version] тепер доступна. Ви хочете встановити її?"

    # game/updater.rpy:148
    old "Preparing to download the update."
    new "Підготовка до завантаження оновлення."

    # game/updater.rpy:150
    old "Downloading the update."
    new "Завантаження оновлення."

    # game/updater.rpy:152
    old "Unpacking the update."
    new "Розпакування оновлення."

    # game/updater.rpy:154
    old "Finishing up."
    new "Завершення."

    # game/updater.rpy:156
    old "The update has been installed. Ren'Py will restart."
    new "Оновлення встановлено. Ren'Py перезапуститься."

    # game/updater.rpy:158
    old "The update has been installed."
    new "Оновлення встановлено."

    # game/updater.rpy:160
    old "The update was cancelled."
    new "Оновлення скасовано."

    # game/updater.rpy:177
    old "Ren'Py Update"
    new "Ren'Py Оновлення"

    # game/updater.rpy:183
    old "Proceed"
    new "Продовжити"

    # game/updater.rpy:188
    old "Fetching the list of update channels"
    new "Отримання списку каналів оновлення"

    # game/updater.rpy:194
    old "downloading the list of update channels"
    new "завантаження списку каналів оновлення"

    # game/updater.rpy:198
    old "parsing the list of update channels"
    new "розбір списку каналів оновлення"

    # game/web.rpy:118
    old "Web: [project.current.display_name!q]"
    new "Web: [project.current.display_name!q]"

    # game/web.rpy:148
    old "Build Web Application"
    new "Скласти Web-застосунок"

    # game/web.rpy:149
    old "Build and Open in Browser"
    new "Скласти та відкрити у веб-оглядачі"

    # game/web.rpy:150
    old "Open in Browser"
    new "Відкрити у веб-оглядачі"

    # game/web.rpy:151
    old "Open build directory"
    new "Відкрити каталог складання"

    # game/web.rpy:155
    old "Support:"
    new "Підтримка:"

    # game/web.rpy:163
    old "RenPyWeb Home"
    new "RenPyWeb Home"

    # game/web.rpy:164
    old "Beuc's Patreon"
    new "Patreon Бевка"

    # game/web.rpy:182
    old "Ren'Py web applications require the entire game to be downloaded to the player's computer before it can start."
    new "Мережеві додатки Ren'Py вимагають завантаження всієї гри на обчислювач гравця, перш ніж вона може розпочатися."

    # game/web.rpy:186
    old "Current limitations in the web platform mean that loading large images, audio files, or movies may cause audio or framerate glitches, and lower performance in general."
    new "Поточні обмеження на мережевому майданчику означають, що завантаження великих зображень, звукофайлів чи рамкові глюки може спричинити збої в звуковій або кадрній частоті та знизити плідність в цілому ???."

    # game/web.rpy:195
    old "Before packaging web apps, you'll need to download RenPyWeb, Ren'Py's web support. Would you like to download RenPyWeb now?"
    new "Перед упакуванням мережевих застосунків вам потрібно завантажити RenPyWeb, мережеву підтримку Ren'Py. Хочете завантажити RenPyWeb зараз?"

# TODO: Translation updated at 2020-04-22 02:28

translate ukrainian strings:

    # game/front_page.rpy:198
    old "audio"
    new "audio"

