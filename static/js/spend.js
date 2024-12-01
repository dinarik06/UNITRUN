document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript Loaded');  // Убедимся, что скрипт загружен
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;  // Получаем CSRF токен
    const spendButton = document.getElementById('spend');
    
    spendButton.addEventListener('click', function () {
        console.log('Button clicked!');  // Проверяем, что кнопка нажимается
        const cost = spendButton.dataset.cost; // Получаем стоимость из атрибута data-cost
        
        fetch('/spend-balance/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,  // Используем CSRF токен
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ amount: cost }), // Отправляем стоимость на сервер
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response:', data); // Логируем ответ сервера
            if (data.success) {
                // Массив картинок, которые могут появиться
                // Выбираем случайную картинку
                let randomImage = images[Math.floor(Math.random() * images.length)];
        

                // Создаем элемент img и добавляем его на страницу
                const imgElement = document.createElement('img');
                imgElement.src = randomImage;
                imgElement.width = 280;
                imgElement.height = 280;

                // Добавляем картинку в контейнер
                const container = document.getElementById('image-container');
                container.innerHTML = '';  // Очищаем контейнер перед добавлением
                container.appendChild(imgElement);
            } else {
                alert(data.error);  // Если монет не хватает
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
