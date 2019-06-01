# Botascript - Instructions

## Interface

### Essential to know

Tout ce dont tu as besoin c'est de savoir manipuler un objet de la class Order().

Ces objets te permettent de retirer des informations sous forme d'attributs:

- *tag* 		Qui est l'action à réaliser **(Ex: "ADD", "LIKE", "COMMENT", ... )**
- *args* 		Qui est un dictionnaire d'arguments pour l'action **(Ex: {"Until":100} )**
- *network* 	Qui est le nom du Network sur lequel opérer. **(Ex: "Linkedin", "Twitter")**
- *login* 		Qui est le login/username de l'utilisateur sur ce network.
- *password* 	Qui est le password de l'utilisateur sur ce network.

Les objets Order() permettent également de récupérer les logs les plus pertinentes pour les remonter à l'utilisateur par le biais du site.
Pour remonter une log, il suffit d'appeler la méthode *.logs(your_message_here)*


### Best practice ever !

```python
orders = Orders() # Orders list creation, empty.
orders.getWork() # Fill the list with orders to execute.

for order in orders:
	# Some interesting stuff on the order...
	# Some interesting stuff on the order...
	# Oooooh some strange stuff here !
	order.logs("WARNING::: It seems that strange_thing_here happened.")
	# Some interesting stuff on the order...
	# Some interesting stuff on the order...
	# Oh, this order finished to execute !
	order.logs("SUCCESS::: Some relative success message juste here.")

		

orders.finished() #Ensure to notify database that these orders were executed.

```

Si tu suis ce schéma d'utilisation, seul la method *.logs()* et les attributs *tag*, *args*, *network*, *login*, *password* te seront utile, le reste est géré par le code ci-dessus.


