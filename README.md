# FTP Client & Server Python Socket Programming
**Programming Language:** Python 

FTP(File Transfer Protocol), serves as a network protocol within the TCP/IP suite for facilitating file transfers between computers. It operates at the application layer of the TCP/IP stack.


During an FTP session, the user's device/computer acts as the local host, while the server serves as the remote host.For successful FTP operations, both the local host and the remote host must be connected via a network and correctly configured.


To enable FTP, servers are configured to provide FTP services, allowing clients to establish connections and transfer files. On the client side, FTP software is essential, enabling users to interact with these services by uploading (PUT) files to the server or downloading (GET) files from the server using specific FTP commands


### Group members
Gina Lee &nbsp;&nbsp;&nbsp;&nbsp; ginnaaleee@csu.fullerton.edu

Karson Lant &nbsp;&nbsp;&nbsp;&nbsp;Karson@csu.fullerton.edu              

Zachary Faulkner &nbsp;&nbsp;&nbsp;&nbsp;zachfaulkner02@gmail.com

Patrick Valera &nbsp;&nbsp;&nbsp;&nbsp;patrickv@csu.fullerton.edu

## Goals
+ **To understand** the challenges of protocol design.
+ **To discover and appreciate** the challenges of developing complex, real-world network applications.
+ **Make sense of** real-world sockets programming APIs.
+ **To utilize** a sockets programming API to construct simplified FTP server and client
applications.

## Execute program
To execute and run the server and client, call the appropriate program from the terminal. 

Run pythonserver.py in a terminal to start the server.
       
        python3 pythonserv.py 
        
        python pythonserv.py (for windows)
Run python cli.py in another terminal to start the client.
     
        python3 cli.py
        
        python cli.py (for windows)

The client will then ask to
      
        Enter server port:

The client will then attempt a connection to the server.

## Client.py 

Upon successfully connecting to the server, the client prints out ftp>, which allows the user to execute the following commands:

        ftp> get <file name> (downloads file <file name> from the server) 

        ftp> put <filename> (uploads file <file name> to the server)

        ftp> ls(lists files on theserver)

        ftp> quit (disconnects from the server and exits)

## Server.py

The server facilitate file transfers over the internet. Uploading involves transferring files from a client to the server while,downloading involves transferring files from the server to the client. 

        pythonserv.py <PORTNUMBER>

        <PORTNUMBER> specifies the port at which ftp server accepts connection requests.

**For example:** pythonserv.py 1234

## Protocol Design
