Title: Seguirle la pista a un comando
Date: 2023-01-24 20:00
Category: bash
Tags: apt, packages, cli, bash
Authors: Juan Manuel Díaz Nevado
Summary: Repasamos como buscar información sobre comandos y los paquetes que los instalan.


Bueno, hoy tabulando en mi consola he encontrado un comando que no sabia que tenia en el servidor, 
como estaba modificando el script de creación de servidores me rayó lo suficiente como para buscar
de donde había salido.

Lo mas obvio es mirar si un paquete con ese nombre se había colado en mi instalación:

```bash
apt-cache show <nombre del paquete>
```

obviamente no encontró nada, el comando es un script que algún otro paquete instaló, así que necesitamos
encontrar `que paquete es responsable de este archivo para ello ejecutamos:
`
```bash
dpkg -S <path completo al archivo>
```

El comando `dpkg` es nuestro mejor aliado para preguntar por paquetes que estén instalados en el sistema,
el flag *-S* nos permite buscar que paquete es el dueño del archivo que pasemos como parámetro.

Este comando nos devuelve el paquete responsable de ponerlo en el sistema, pero esto no ayudo, pq
está claro que no íbamos a tener la suerte de que fuera un paquete que nosotros instalamos.

Así que, como nos encontramos ante un paquete que ha sido instalado como dependencia de otro tenemos
que pedir los paquetes que lo tengan como dependencia.

```bash
apt-cache rdepends --installed <nombre del paquete>
```

Al buscar las dependencias volvemos a apt, en este caso con `apt-cache` junto con rdepends para
buscar dependencias inversas. Si usáramos rdepends directamente nos veríamos desbordados por la
enorme lista de dependencias de todos los paquetes de los repos de nuestra distro.

Así que tenemos que usar el flag `--installed` para que solo muestre aquellos que tenemos en el 
sistema que es lo que queríamos.

En esta salida de ejemplo, buscamos las dependencias inversas del paquete fuse. El resultado
es una lista tabulada donde lista en el nivel más externo los paquetes que tiene de dependencia el buscado
y en el siguiente nivel el paquete concreto del que depende.

En este caso, vemos como al buscar lo que encuentra es la dependencia con fuse3, ya que es el paquete 
que lo sustituye. Esto suele pasar cuando los nombres de paquetes se versionan para hacer convivir varias
versiones como python2 y python3.
			
```bash
juandn@dev:/$ apt-cache rdepends --installed fuse
fuse
Reverse Depends:
  ntfs-3g
	fuse3
  libfuse2
  xdg-desktop-portal
	fuse3
  ntfs-3g
	fuse3
  fuse3
	fuse3
  fuse3
  exfat-fuse
	fuse3
  libfuse2
	fuse3

```

Otra salida que podemos encontrar es un *|* delante del nombre del paquete como en:

```bash
juandn@dev:/mnt$ apt-cache rdepends --installed apache2
apache2
Reverse Depends:
  task-web-server
  libapache2-mod-php7.4
 |javascript-common
  apache2-doc
  task-web-server
  libapache2-mod-php7.4
  apache2-doc
 |analog

```

Aquí vemos como varios paquetes dependen de apache2, pero javascript-common y analog tiene delante un *|*.
Si mostramos la información del paquete javascript-common, vemos que depende de apache2 o de otros, no "y" de otros.

```bash
juandn@dev:/mnt$ apt-cache show javascript-common
Package: javascript-common
Version: 11+nmu1
Installed-Size: 33
Maintainer: Debian Javascript Maintainers <pkg-javascript-devel@lists.alioth.debian.org>
Architecture: all
*Suggests: apache2 (>= 2.4.6~) | lighttpd | httpd*
Description-en: Base support for JavaScript library packages
 Web applications that use JavaScript need to distribute it through HTTP. Using
 a common path for every script avoids the need to enable this path in the HTTP
 server for every package.
 .
 This is a helper package that creates /usr/share/javascript and enables it in
 the Apache and Lighttpd webserver.
Description-md5: 1c8d846310501114a6acd24c4e760036
Section: javascript
Priority: optional
Filename: pool/main/j/javascript-common/javascript-common_11+nmu1_all.deb

```
Pero un momento, no hay entrada *depends*, apache2 aparece como opción a elegir en 
la entrada *Suggests*. Esto nos lleva a otra vuelta mas de tuerca, la búsqueda de dependencias 
se complica pq hay varios motivos por los que un paquete depende de otro, no solo la 
dependencia directa de instalación.

Si ejecutamos `man apt-cache` podemos encontrar opciones para controlar la salida de 
los comandos depends y rdepends.

>  --no-pre-depends, --no-depends, --no-recommends, --no-suggests, --no-conflicts,
>   --no-breaks, --no-replaces, --no-enhances
>       Per default the depends and rdepends print all dependencies. This can be tweaked with
>       these flags which will omit the specified dependency type. Configuration Item:
>       APT::Cache::ShowDependencyType e.g.  APT::Cache::ShowRecommends.
>
>   --implicit
>       Per default depends and rdepends print only dependencies explicitly expressed in the
>       metadata. With this flag it will also show dependencies implicitly added based on the
>       encountered data. A Conflicts: foo e.g. expresses implicitly that this package also
>       conflicts with the package foo from any other architecture. Configuration Item:
>       APT::Cache::ShowImplicit.

En general con esto es más que suficiente para seguirle la pista a ese archivo que no
sabéis de donde ha salido en vuestro sistema y recordad, las man-pages son vuestras amigas.




