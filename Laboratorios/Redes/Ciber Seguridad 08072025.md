Ciber Seguridad 08-07-2025

Estremos hablando sobre o trabajando con "Cisco Packet Tracer"

Redes virtuales VLAN

al ingresar en pracketTracer hay dos usuarios

&nbsp;$ //"De forma de Administrador"

&nbsp;# //"Forma de Usuario shell"

-------------------------------------------------------------------

Comandos en Packet Tracer

cont t //

enable //Entrar al modo privilegiado

configure terminal // Entrar a la configuración global

exit // Sale del modo actual

end // Regresa al modo EXEC privilegiado

&nbsp;	Crear una VLAN

enable

configure terminal

vlan \[numero Vlan]

name \[nombre de la vlan]

exit

&nbsp;	Configuración interfaces

interface FastEthernet0/0   #

ip address 192.168.1.1 255.255.255.0

no shutdown 		    # Activa la interfaz

\*\*\*\*\*\*\*\*Configuración de rutas

ip route 0.0.0.0. 0.0.0.0 192.168.1.254 # Ruta por defecto (gateway)

\*\*\*\*\*\*\*\*Configurar nombres, contraseñas y banner

hostname Router1

**enable** secret cisco

line console 0

&nbsp; password cisco

&nbsp; login

banner motd #¡Acceso no autorizado prohibido!#

\*\*\*\*\*\*\*\*Guardar y ver configuracion

copy running-config startup-config    # Guarda configuración en memoria NVRAM

show running-config                  # Muestra configuración actual

show ip interface brief              # Estado de interfaces

show version                         # Información del dispositivo

\*\*\*\*\*\*\*\*Verificación y pruebas

ping 192.168.1.1                    # Verifica conectividad

traceroute 8.8.8.8                  # Ruta hacia destino

show cdp neighbors                  # Ver dispositivos vecinos

/\*Configuración para la parte admitiva\*/

enable

configure terminal

vlan 10

name admitiva

exit 

exit

write men

show vlan brief

/\*Configurar para la parte contable\*/

enable

configure terminal || conf t

vlan 20

name contabilidad

exit

exit

write men

show vlan brief

/\*Rango para trabajo Admitiva\*/

conf t

interface range f0/1-3

switchport mode Access

switchport Access vlan 10

/\*Rango para trabajo Contable\*/

conf t

interface range f0/4-5

switchport mode Access

switchport Access vlan 20

--------------------------------------------------------------------

En la segunda sección, vamos a trabajar wirshark, burpsite.

Se descargo la aplicación Burp Suite, nos fuimos al sitio web teshpanda.org, para poder practicar y usar la aplicacion



podimos sacar o miar la información al loguears, 

