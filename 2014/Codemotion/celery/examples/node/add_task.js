var celery = require('node-celery'),
    client = celery.createClient({
        CELERY_BROKER_URL: 'amqp://guest:guest@localhost:5672//',
        CELERY_RESULT_BACKEND: 'amqp'
    });

client.on('connect', function() {
    var result = client.call('tasks.add', [1, 2]);
    result.on('ready', function(data) {
        console.log(data);
    });
});
