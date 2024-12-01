let clickCount = 0; // Текущий счётчик кликов
let balance = 0;    // Баланс пользователя

// Увеличение счётчика кликов
function incrementClick() {
    clickCount++;
    document.getElementById('clickCount').innerText = clickCount;
}

// Отправка кликов на баланс
function sendClicks() {
    balance += clickCount; // Добавляем клики к балансу
    clickCount = 0;        // Обнуляем счётчик кликов
    document.getElementById('clickCount').innerText = clickCount;
    document.getElementById('balance').innerText = balance;
}