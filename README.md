# AlphaClientServer

This project containing three different images, one server and two clients.
Server use plain `json` file for storing logs. 

This project use Alpine Linux.

So, basically the client will watch every changes upon `/var/log/messages` file, because every login attempt using ssh in Alpine Linux 
will be stored in this file. Then, the client will count incoming ssh attempts (both accepted and failed) and construct json request with following format:

<pre>
{
    "server_name": "NodeABC",
    "total_login_attempts": 3
}
</pre>

then the client send the request to the server via http call.

The server built on top Flask (small Python web framework). The server has index method for showing the report, so you can open it using your favourite browser. In addition, the server has `create log endpoint` and save the request into plain `json` file using `tinydb` library.

