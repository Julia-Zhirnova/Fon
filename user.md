ctrl + l - очистка терминал
3  sudo fdisk -l 
    4  sudo fdisk /dev/sda
d - удаление раздела, p - проверка, n - номер раздела, enter - добавление памяти +300G, w - сохранить

    5  sudo mkdir /home/user1
    6  sudo mkdir /home/user2
    7  sudo mkdir /home/user3
    8  sudo systemctl --force --full edit home-user1.mount
    9  sudo mkfs.ext4 /dev/sda1
   10  sudo mkfs.ext4 /dev/sda2
   11  sudo mkfs.ext4 /dev/sda3
   12  cd /etc/systemd/system/   
   14  sudo cp home-user1.mount home-user2.mount 
   15  sudo cp home-user1.mount home-user.mount 
   17  sudo cp home-user1.mount home-user3.mount 
   18  sudo systemctl --force --full edit home-user2.mount
   19  sudo systemctl --force --full edit home-user3.mount
   20  sudo systemctl start home-user3.mount
   21  sudo systemctl start home-user2.mount
   22  sudo systemctl start home-user1.mount
   23  sudo systemctl enable home-user1.mount
   24  sudo systemctl enable home-user2.mount
   25  sudo systemctl enable home-user3.mount
   26  sudo adduser user1
   27  sudo adduser user2
   28  sudo adduser user3
   29  sudo passwd user1
   30  sudo passwd user2
   31  sudo passwd user3
   32  sudo chown user1: /home/user1
   33  sudo chown user2: /home/user2
   34  sudo chown user3: /home/user3
   35  ls -l /home/
   37  sudo chmod 700 /home/user1
   38  sudo chmod 700 /home/user2
   39  sudo chmod 700 /home/user3
   40  reboot 
   41  history 

[Unit]
Description=mount user2


[Mount]
What=/dev/sda2
Where=/home/user2
Options=defaults
Type=ext4


[Install]
WantedBy=multi-user.target


https://youtu.be/YGCqeZh1HfQ
