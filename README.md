# asset_cms
asset_cms powered by python3.6_django

#### 1.重要!!.首先肯定先使用git更新代码,首先是进入项目目录然后git pull,项目是在python用户家目录下面的asset_cms(git pull更新到最新)
#### 2.首先定义好数据库里面的FrontEndShow里面的添加并且仅只需要一条数据.用于定义展示给学生的ip地址
#### 3.然后记得去修改PortType的端口,前提是如果冲突的话,如果不冲突可以不用管.
#### 4.现在去填写你想为django项目监听的ip和端口,具体编辑文件在/home/python/asset_cms/uwsgi.ini,主要修改ip和端口就可以了,其他不用修改.
#### 然后cd 到/home/python/asset_cms, 开始运行脚本 ./sta,如果你想停止项目的话,运行停止运行脚本 ./sto
#### 5.手动去定义nginx配置位置,就是/etc/nginx/nginx.conf,定义好端口和ip,注意了,ip必须和上面第一个一一对应.不然就出错了.
> 具体事例
```nginx
 server
{
        ##这里监听的ip是和/home/python/asset_cms/uwsgi.ini里面的ip是一致,端口的话,可以任意.
        listen x.x.x.x:xx;
        server_name localhost;


        location / {

        ##这里填写的ip和端口是对应在/home/python/asset_cms/uwsgi.ini里面的socket对应的ip和端口
        uwsgi_pass xxxxx:xx;
        include /etc/nginx/uwsgi_params;

        }


        location /student {
        root /home/python/asset_cms/static;
        #index index.html;
}

        location /static {

        alias /home/python/asset_cms/static/;

        }

}
``` 
#### 然后就可以启动nginx了,具体可以这样 sudo service nginx start
#### 暂时没有其他了.!
