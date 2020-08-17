# Software requirements for the LOVD local installation:
A webserver to run PHP scripts like Apache webserver.
PHP 5.3.0 or higher
Mysql 4.1.2 or higher

## Download and Install XAMPP:
Click [here](https://www.apachefriends.org/index.html) to download XAMPP.

XAMPP is a PHP development environment which provides Apache, Mysql, PHP and Perl.

## Download & Extract LOVD:

Go to LOVD homepage and download and extract [LOVD 3.0](http://www.lovd.nl/3.0/home)

### Pre-install configuration:
The standard config file “config.ini.php-lovd” should be renamed to “config.ini.php” and edited in a text editor. This is definitely mandatory because it is required to enter the MySQL hostname, username, password and database name here. In my case, as I used XAMPP, the hostname: “localhost”, username: “root” and password: “” which means empty. No quotes around the values are needed. 

## Start the installation:
1. Run XAMPP.
2. Copy LOVD installation folder to the desired folder provided by the server. The address format in macOS is: http://[localhost]/LOVDv.3.0/ for example: http://192.168.64.2/dashboard/LOVDv.3.0

..* Installing LOVD consists of only 4 simple steps and takes only a couple of minutes. Each step contains various forms and filling them is pretty straight forward. 



