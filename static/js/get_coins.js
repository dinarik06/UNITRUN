let balance = 0; // Баланс пользователя

// Увеличиваем баланс на 1 после каждого клика
function incrementClick() {
    balance++; // Увеличиваем локальный баланс
    updateBalanceDisplay(); // Обновляем отображение баланса
}

// Отправляем баланс на сервер и сбрасываем локальный баланс
function sendClicks() {
    fetch('/update_balance/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() // Добавляем CSRF токен для безопасности
        },
        body: JSON.stringify({ balance: balance }) // Отправляем баланс
    })
        .then(response => {
            if (response.ok) {
                console.log('Баланс успешно отправлен!');
                balance = 0; // Сбрасываем локальный баланс
                updateBalanceDisplay(); // Обновляем отображение баланса
            } else {
                console.error('Ошибка при отправке баланса.');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}

// Обновляем отображение баланса на странице
function updateBalanceDisplay() {
    document.getElementById('balance').innerText = balance;
}

// Получение CSRF токена для защиты POST запросов
function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}