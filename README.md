# Fon
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
