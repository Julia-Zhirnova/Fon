# Fon
1. Хранитель экрана: убрать галочку у "Запускать хранитель экрана, когда компьютер простаивает" и "Блокировать экран, когда запущен хранитель экрана"
   ![image](https://github.com/user-attachments/assets/668bec36-3718-4828-8611-fb20b467a965)

2. Управление питанием: можно выбрать
Действия
Переводить компьютер в спящий режим в случае бездействия спустя: Никогда
Внешний вид
Отключать экран в случае бездействия спустя: Никогда
  ![image](https://github.com/user-attachments/assets/b688d423-bf9e-4366-a2ea-bffab9962a7b)

3. Сочетания клавиш клавиатуры: можно настроить:
Пригнать окно к восточной (правой) стороне экрана. Mod 4+Вправо
Пригнать окно к западной (левой) стороне экрана Mod4+Влево
  ![image](https://github.com/user-attachments/assets/baff6a38-ea54-4294-9f7f-259d3c13a14a)

4. Окно настройки РЕД ОС: убрать галочку у Показывать это окно при загрузке системы
  ![image](https://github.com/user-attachments/assets/c7877c47-9aea-45ad-a6e1-b7b945cafc4e)








https://remontka.pro/litamanager-free-remote-desktop-software/?ysclid=lmfzwo9b1j549823205

https://docs.google.com/document/d/1vxgWIKFuOPhAFZKVlFQjK8OMBMuYTvt8XFsYg5OiQAc/edit?usp=sharing


sudo systemctl status display-manager.service
Должен быть sddm.service
Если не он, то
<br>su
<br>dnf install sddm sddm-themes
<br>systemctl disable gdm
<br>systemctl enable sddm
<br>перезагрузить reboot

<br>su root
<br>dnf install x11vnc
<br>x11vnc -storepasswd "12345" /etc/vncpasswd
<br>nano /lib/systemd/system/x11vnc.service

<br>[Unit]
<br>Description=x11vnc server for SDDM
<br>After=display-manager.service

<br>[Service]
<br>ExecStart=/bin/bash -c "/usr/bin/x11vnc -display :0 -many -shared -dontdisconnect -repeat -auth /run/sddm/xauth* -noxdamage -rfbauth /etc/vncpasswd"
<br>Restart=on-failure
<br>RestartSec=10

<br>[Install]
<br>WantedBy=graphical.target

<br>systemctl daemon-reload
<br>systemctl enable x11vnc.service
<br>systemctl start x11vnc.service
<br>systemctl status x11vnc.service

ИЛИ
<br>systemctl --full --force edit x11vnc
<br>systemctl daemon-reload
<br>systemctl restart x11vnc
<br>systemctl status x11vnc
<br>systemctl reenable x11vnc
