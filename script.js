function showModule(moduleId) {
    const moduleDetails = document.getElementById('module-details');
    const moduleTitle = document.getElementById('module-details-title');
    const moduleContent = document.getElementById('module-details-content');
    
    const module = modulesData.find(m => m.id === moduleId);
    if (!module) return;
    
    moduleTitle.textContent = module.title;
    
    if(moduleId === 'programming') {
        moduleContent.innerHTML = `
            <div class="works-info">
                <p>Все работы выполнены в рамках обучения по дисциплине "Программирование".</p>
            </div>
            
            <div class="semester-title" onclick="toggleSemester('sem4')">
                <h3 class="mb-0">Семестр 4</h3>
            </div>
            <div id="sem4" class="semester-content">
                <ul class="list-unstyled">
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr1" class="work-link" target="_blank">Лабораторная работа 1. Рекурсивное построение бинарного дерева.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr2" class="work-link" target="_blank">Лабораторная работа 2. Нерекурсивное построение бинарного дерева.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr3" class="work-link" target="_blank">Лабораторная работа 3. Сравнение способов построения бинарного дерева.</a></li>
                    <li><a href="https://replit.com/@zhamall/Laboratornaia-rabota-4#README.md" class="work-link" target="_blank">Лабораторная работа 4. Типы данных.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr5" class="work-link" target="_blank">Лабораторная работа 5. Sqlite.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr6" class="work-link" target="_blank">Лабораторная работа 6. Sqlite + Singleton.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr7" class="work-link" target="_blank">Лабораторная работа 7. Работа с Json.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem4/lr8" class="work-link" target="_blank">Лабораторная работа 8. Sqlite + Orator.</a></li>
                </ul>
            </div>
            
            <div class="semester-title" onclick="toggleSemester('sem5')">
                <h3 class="mb-0">Семестр 5</h3>
            </div>
            <div id="sem5" class="semester-content">
                <ul class="list-unstyled">
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr1" class="work-link" target="_blank">Лабораторная работа 1. Создание собственного модуля и пакета.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr2" class="work-link" target="_blank">Лабораторная работа 2. Реализация удаленного импорта.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr3" class="work-link" target="_blank">Лабораторная работа 3. Использование API. </a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr4" class="work-link" target="_blank">Лабораторная работа 4. Создание итератора по ряду Фибоначчи.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr5" class="work-link" target="_blank">Лабораторная работа 5. Создание приложения для получения курса валют.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr6" class="work-link" target="_blank">Лабораторная работа 6. Дополнение к ЛР 5 (Реализация Singleton)</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr7" class="work-link" target="_blank">Лабораторная работа 7. Тест Singleton.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem5/lr8" class="work-link" target="_blank">Лабораторная работа 8. Паттерн MVC. </a></li>
                </ul>
            </div>
            
            <div class="semester-title" onclick="toggleSemester('sem6')">
                <h3 class="mb-0">Семестр 6</h3>
            </div>
            <div id="sem6" class="semester-content">
                <ul class="list-unstyled">
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem6/lr1-2" class="work-link" target="_blank">Лабораторная работа 1-2. Анализ данных.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem6/lr3" class="work-link" target="_blank">Лабораторная работа 3. Кэширование.</a></li>
                    <li><a href="https://colab.research.google.com/drive/1p-CMSCkhfpNEfGhmjTe5K4BtaT00IsK5?usp=sharing" class="work-link" target="_blank">Лабораторная работа 4-5. Машинное обучение. </a></li>
                    <li><a href="https://colab.research.google.com/drive/1-HUxJyZYXwkCZJQHaWtf9HEOuC6l-hFy?usp=sharing" class="work-link" target="_blank">Лабораторная работа 6. Предсказание цены поддержанного авто.</a></li>
                    <li><a href="https://colab.research.google.com/drive/1S5dipS21WgDevJS21tX91L4GR3UFgQnT?usp=sharing" class="work-link" target="_blank">Лабораторная работа 7. Предсказание дефолта по кредиту.</a></li>
                    <li><a href="https://ivanovvnikita.github.io/movieMVC/" class="work-link" target="_blank">Лабораторная работа 8. Sphinx.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem6/lr9" class="work-link" target="_blank">Лабораторная работа 9. Развертывание приложения на FastAPI.</a></li>
                </ul>
            </div>
            
            <div class="semester-title" onclick="toggleSemester('sem7')">
                <h3 class="mb-0">Семестр 7</h3>
            </div>
            <div id="sem7" class="semester-content">
                <ul class="list-unstyled">
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/lr1" class="work-link" target="_blank">Лабораторная работа 1. Введение в Django.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/lr2" class="work-link" target="_blank">Лабораторная работа 2. Применение форм в Django. Аутентификация и регистрация пользователей.</a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/lr3" class="work-link" target="_blank">Лабораторная работа 3. Django REST Framework: (микро)сервисы. </a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/lr4" class="work-link" target="_blank">Лабораторная работа 4. Простые паттерны интеграции с Apache Camel </a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/pr1" class="work-link" target="_blank">Практическая работа 1. Настройка OAuth 2.0 авторизации в Django приложении. </a></li>
                    <li><a href="https://github.com/IvanovvNikita/portfolio-prog/tree/main/sem7/pr2" class="work-link" target="_blank">Практическая работа 2. RESTful веб-приложение на Spring Boot.</a></li>
                </ul>
            </div>
        `;
    } else {
        const disciplines = disciplinesData[moduleId] || [];
        
        let disciplinesHTML = '';
        if (disciplines.length > 0) {
            disciplinesHTML = '<ul class="discipline-list">';
            disciplines.forEach(discipline => {
                disciplinesHTML += `
                    <li class="discipline-item">
                        <a href="${discipline.link}" class="discipline-link" target="_blank">
                            <i class="fas fa-book"></i> ${discipline.name}
                        </a>
                    </li>
                `;
            });
            disciplinesHTML += '</ul>';
        } else {
            disciplinesHTML = '<p>Информация о дисциплинах будет добавлена позже.</p>';
        }
        
        moduleContent.innerHTML = `
            <h3 class="mb-4">Дисциплины модуля</h3>
            ${disciplinesHTML}
        `;
    }
    moduleDetails.style.display = 'block';
}

function closeModule() {
    document.getElementById('module-details').style.display = 'none';
}

function toggleSemester(semesterId) {
    const content = document.getElementById(semesterId);
    if (content.style.display === 'block') {
        content.style.display = 'none';
    } else {
        content.style.display = 'block';
    }
}

function renderModuleCards() {
    const container = document.getElementById('modules-container');
    
    container.innerHTML = '';
    
    modulesData.forEach(module => {
        container.innerHTML += `
            <div class="module-card" onclick="showModule('${module.id}')">
                <div class="module-icon ${module.iconClass}">
                    <i class="${module.icon}"></i>
                </div>
                <div class="module-content">
                    <h3 class="module-title">${module.title}</h3>
                </div>
            </div>
        `;
    });
}

window.addEventListener('click', function(event) {
    const moduleDetails = document.getElementById('module-details');
    if (event.target === moduleDetails) {
        closeModule();
    }
});

window.addEventListener('DOMContentLoaded', function() {
    renderModuleCards();
    
    setTimeout(() => {
        if (document.getElementById('sem4')) {
            document.getElementById('sem4').style.display = 'block';
        }
    }, 500);
});