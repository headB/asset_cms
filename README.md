# asset_cms
asset_cms powered by python3.6_django

## 这个站点的结构是   nginx->uwsgi(python)->nodejs.所以,关键就是配置好nginx和uwsgi就可以了.!


#### 1.重要!!.首先肯定先使用git更新代码,首先su python,然后cd ~ ,然后cd /home/python/asset_cms,然后更新最新代码git pull
#### 2.现在去填写你想为django项目监听的ip和端口,具体编辑文件在/home/python/asset_cms/uwsgi.ini,主要修改ip和端口就可以了,其他不用修改.
#### 然后cd 到/home/python/asset_cms,先修改一下文件权限,chmod +x uwsgi sta sto,然后开始运行脚本 ./sta,如果你想停止项目的话,运行停止运行脚本 ./sto
#### 3.手动去定义nginx配置位置,就是/etc/nginx/nginx.conf,定义好端口和ip,注意了,ip必须和上面第一个一一对应.不然就出错了.sudo vim /etc/nginx/nginx.conf
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
#### 4.记得使用uwsgi启动好django之后,去<管理员站点设置>设置好面向对于学生展示的IP地址和对应好的教学区域.
#### 但是有一个问题,就是你设置好了这个学生的展示的ip地址之后,是需要先使用上面说到的./sto停止脚本停止,然后再./sta启动的!!.
#### 5.然后记得去修改PortType的端口,前提是如果冲突的话,如果不冲突可以不用管.不过端口只能是80XX,4位数,前面固定是80
#### 6.可以的话,请记得去删除TM2015项目里面关于提交评价之后出现的二维码.
#### 暂时没有其他了.!?!

