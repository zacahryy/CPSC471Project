# FTP Client & Server Python Socket Programming

# Client.py
Upon connecting to the server, the client prints out ftp>, which allows the user to execute the following commands:

ftp> get <file name> (downloads file <file name> from the server) 

ftp> put <filename> (uploads file <file name> to the server)

ftp> ls(lists files on theserver)

ftp> quit (disconnects from the server and exits)

# Server.py
pythonserv.py<PORTNUMBER>
<PORT NUMBER>specifiestheport atwhichftp serveraccepts connection requests. For example: python serv.py 1234
