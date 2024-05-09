# FTP Client & Server Python Socket Programming
Programming Language: python 
### Group members
Gina Lee                 ginnaaleee@gmail.com

Karson Lant               

Zachary Faulkner         zachfaulkner02@gmail.com
## Client.py
Upon connecting to the server, the client prints out ftp>, which allows the user to execute the following commands:

        ftp> get <file name> (downloads file <file name> from the server) 

        ftp> put <filename> (uploads file <file name> to the server)

        ftp> ls(lists files on theserver)

        ftp> quit (disconnects from the server and exits)

## Server.py
        pythonserv.py <PORTNUMBER>

        <PORTNUMBER> specifies the port at which ftp server accepts connection requests.

For example: python serv.py 1234
