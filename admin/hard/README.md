# Too many files

### Statement
Окей. В их сети обнаружился еще один сервер. На этот раз с шеллом все в порядке, даже удалось сбрутить праоль одного из пользователей. Но вот колчество файлов там поражает. Возможно, есть какой-то способ быстро найти нужный?.. 
P.S. Пароль от user1 - find32
ssh user1@ctf-edu-t.orb.ru -p 1653

### Deploy
Build docker cotainer from `service` and expose port 22. SSH service
