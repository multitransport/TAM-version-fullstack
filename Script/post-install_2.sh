#!/bin/bash

echo "PASSWORD SUDO DISABLE"
sudo sed -i "s/%sudo ALL=(ALL) ALL/%admin ALL=(ALL) NOPASSWD:ALL/" /etc/ssh/sshd_config
#Désactive le mot de passe sudo le temps de l'installation


echo "Time zone change for Paris"
sudo timedatectl set-timezone Europe/Paris
#La commande timedateectl permet de changer de fuseau horaire au niveau du serveur


# echo "UBUNTU POST-INSTALL SCRIPT"
# echo "Updating APT..."
# sudo apt-get -y update
# sudo apt-get -y upgrade
# Les mises à jours sont déjà présente sur la VM pour gagner du temps lors de l'execution du script


echo "Password desactivation"
sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
#Désactive l'authentification ssh par mot de passe
sudo /etc/init.d/ssh restart
#Relance le servcie ssh pour appliquer les modifications


echo "Installation de Apache pour le serveur http"
sudo apt install apache2
# Mode restrictif avec autorisation d'accès sur le port 80
sudo ufw allow 'Apache'
# Vérification du status du serveur
sudo systemctl status apache2


echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip
sudo pip3 install --upgrade pip

echo "Installation des librairie python utile au brief"
sudo pip3 install -r requirements.txt

echo "PASSWORD SUDO ENABLE"
sudo sed -i "s/%sudo ALL=(ALL) NOPASSWD:ALL/%admin ALL=(ALL) ALL/" /etc/ssh/sshd_config
#Remet le mot de passe sudo à la fin de l'installation
exit

