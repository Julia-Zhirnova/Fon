# Fon
https://remontka.pro/litamanager-free-remote-desktop-software/?ysclid=lmfzwo9b1j549823205
sudo systemctl status display-manager.service
Должен быть sddm.service
Если не он, то
su
dnf install sddm sddm-themes
systemctl disable gdm
systemctl enable sddm
перезагрузить reboot

su root
dnf install x11vnc
x11vnc -storepasswd "12345" /etc/vncpasswd
nano /lib/systemd/system/x11vnc.service

[Unit]
Description=x11vnc server for SDDM
After=display-manager.service

[Service]
ExecStart=/bin/bash -c "/usr/bin/x11vnc -display :0 -many -shared -dontdisconnect -repeat -auth /run/sddm/xauth* -noxdamage -rfbauth /etc/vncpasswd"
Restart=on-failure
RestartSec=10

[Install]
WantedBy=graphical.target

systemctl daemon-reload
systemctl enable x11vnc.service
systemctl start x11vnc.service
systemctl status x11vnc.service

ИЛИ
systemctl --full --force edit x11vnc
systemctl daemon-reload
systemctl restart x11vnc
systemctl status x11vnc
systemctl reenable x11vnc
