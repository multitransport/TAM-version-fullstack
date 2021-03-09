#!/bin/bash

# sudo apt install sshpass
# Installe sshpass pour gérer le mot de passe de connexion ssh

read -p "login de la VM : " login
read -p "@ip de la VM : " ipaddress
echo -n Password:
read -s mdp
echo $mdp > /mnt/c/Users/utilisateur/.ssh/mdp2.ini

# Copie de la clé vers la VM
sshpass -p $mdp ssh-copy-id -i /mnt/c/Users/utilisateur/.ssh/id_rsa.pub $login@$ipaddress

# Git clone du repo sur la VM
sshpass -p $mdp ssh $login@$ipaddress "git clone https://github.com/multitransport/TAM-version-fullstack.git"

# Rend executable le fichier post-install_2.sh
sshpass -p $mdp ssh $login@$ipaddress "chmod +x ./TAM-version-fullstack/Script/post-install_2.sh"

# Retire les mauvais caractères mis par Windows
sshpass -p $mdp ssh $login@$ipaddress "sed -i -e 's/\r$//' ./TAM-version-fullstack/Script/post-install_2.sh"

# Execute le fichier post-install_2.sh
cat /mnt/c/Users/Damien/.ssh/mdp2.ini | sshpass -p $mdp ssh -T $login@$ipaddress "sudo -S ./TAM-version-fullstack/Script/post-install_2.sh"