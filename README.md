# FTP Client & Server Python Socket Programming
Programming Language: python 
### Group members
Gina Lee &nbsp;&nbsp;&nbsp;&nbsp; ginnaaleee@csu.fullerton.edu

Karson Lant &nbsp;&nbsp;&nbsp;&nbsp;Karson@csu.fullerton.edu              

Zachary Faulkner &nbsp;&nbsp;&nbsp;&nbsp;zachfaulkner02@gmail.com

## Execute program
To execute and run the server and client, call the appropriate program from the terminal. 

Run python server.py in a terminal to start the server.
                                python3 pythonserver.py
Run python client.py in another terminal to start the client.
Use commands like GET filename, PUT filename, ls, and quit  in the client to interact with the server and perform file transfers.


Zachary Faulkner &nbsp;&nbsp;&nbsp;&nbsp;zachfaulkner02@gmail.com
## Client.py 

Upon connecting to the server, the client prints out ftp>, which allows the user to execute the following commands:

        ftp> get <file name> (downloads file <file name> from the server) 

        ftp> put <filename> (uploads file <file name> to the server)

        ftp> ls(lists files on theserver)

        ftp> quit (disconnects from the server and exits)

## Server.py
        pythonserv.py <PORTNUMBER>

        <PORTNUMBER> specifies the port at which ftp server accepts connection requests.

For example: pythonserv.py 1234
