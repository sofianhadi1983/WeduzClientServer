# AlphaClientServer

This project containing three different images, one server and two clients.
Server use plain `json` file for storing logs. 

This project use Alpine Linux.

So, basically the client will watch every changes upon `/var/log/messages` file, because every login attempt using ssh in Alpine Linux 
will be stored in this file. Then, the client will count incoming `SSH` attempts (both accepted and failed) and construct json request with following format:

<pre>
{
    "server_name": "NodeABC",
    "total_login_attempts": 3
}
</pre>

then the client send the request to the server via http call.

The server built on top Flask (small Python web framework). The server has index method for showing the report, so you can open it using your favourite browser. In addition, the server has `create log endpoint` and save the request into plain `json` file using `tinydb` library.

# How to run the project ?

First, run following command in root project directory
<pre>
docker-compose up --build
</pre>

Both clients are accessible through `SSH` on localhost via port 2222 and 2223. You need to edit `docker-compose.yml` if you want to use another port number.
Please do `SSH` commands using password `gopay` and open the browser pointing to `http://127.0.0.1`

<pre>
ssh root@localhost -p 2222
ssh root@localhost -p 2223
</pre>

