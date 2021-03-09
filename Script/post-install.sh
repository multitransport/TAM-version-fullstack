#!/bin/bash

# sudo apt install sshpass
# Installe sshpass pour gérer le mot de passe de connexion ssh

read -p "login de la VM : " login
read -p "@ip de la VM : " ipaddress
echo -n Password:
read -s mdp
echo $mdp > /mnt/c/Users/utilisateur/.ssh/mdp2.ini

sshpass -p $mdp ssh-copy-id -i /mnt/c/Users/utilisateur/.ssh/id_rsa.pub $login@$ipaddress
# read -p "Chemin du script à copier : " path_script
# read -p "Nom du script : " name_script_sh
# scp $path_script sshpass -p $mdp ssh $login@$mdp:/
# sshpass -p $mdp ssh $login@$mdp "chmod +x $name_script_sh"
# sshpass -p $mdp ssh $login@$mdp "sed -i -e 's/\r$//' $name_script_sh"
sshpass -p $mdp ssh $login@$mdp "sudo git clone https://github.com/multitransport/TAM-version-fullstack.git"