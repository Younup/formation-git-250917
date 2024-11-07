# formation-git
Repo pour la formation Git

## Configuration du repo en local

Configurer son identité sur le client git :
```git config –-global user.name YourName```
```git config –-global user.email "your@email.com"```

Configurer l'éditeur de text par défaut sur git (avec vi dans cet exemple) :
```git config --global core.editor "vim"```

Génération de la clé pour utiliser le ssh avec git :
```
ssh-keygen -t ed25519 -C "your@email.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Ensuite, ajouter la clé SSH à GitHub :
Copiez la clé : 
```cat ~/.ssh/id_ed25519.pub```
Allez sur GitHub > Paramètres > SSH and GPG keys > New SSH key > Collez la clé et enregistrez.

Cloner le répertoire :
```git clone git@github.com:Younup/formation-git.git```
