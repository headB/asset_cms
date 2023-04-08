##获取一个通用函数
common_ip = False
##获取通用ip来用来获取设置选项..
common_ip = False
##反正全局变量并没有被调用....所以,,,保险点还是做成函数算了.
def reflash_common_ip():
	from login.models import FrontEndShow
	common_ip_info = FrontEndShow.objects.all()

	if not common_ip_info:
		raise ValueError("请先配置数据库中FrontEndShow里面的详细数据,如果为空请填入数据,例如学生访问的页面是192.168.113.1,你就填写ip为192.168.113.1,端口为80就可以了.!")
	else:
		common_ip1 = str(common_ip_info[0].ip)
		global common_ip
		common_ip = common_ip1

##这是一个获取了ip地址之后返回一堆str
def return_nodejs_security(ip_addr):
	reflash_common_ip()
	if not ip_addr:
		return False

	content = """var os = require("os");

module.exports = function(){
	
	var ip = "%s";

	var act_ip = false

//for (x in os.networkInterfaces()){for ( x1 in os.networkInterfaces()[x]){if (ip == os.networkInterfaces()[x][x1]['address']){var act_ip = true};}}

	return function(req, res, next){
		//console.log("run me how time?")
		//获取当前电脑Ip地址。 外部ip(本机ip)和内部ip(localhost)
		var localIp = os.networkInterfaces()[0];
		var act_ip = false;
		for (x in os.networkInterfaces()){for ( x1 in os.networkInterfaces()[x]){if (req.ip == os.networkInterfaces()[x][x1]['address']){var act_ip = true;};}}

		if(!req.session._initialize){
			if( req.ip==localIp || ip==req.ip || act_ip || req.ip =="127.0.0.1" || req.ip =="172.17.0.1" ){
				req.session.teacher = true;
			}
			req.session._initialize = true;
		}

		var classIp = req.ip.match(/192.168.%s/);

		 if ( req.path == "/grade/sorry"){
			next();
			return 
		 } 
			
		 if (!classIp && !req.session.teacher){
			 res.redirect("/grade/sorry")
		 }
		
		
		if(req.session.teacher || req.path=="/grade" || req.path=="/grade/save"){
			next();	
		}else{
			
			res.redirect("/grade");
		}
		
	};
	
} 

    """%(common_ip,ip_addr)

	return content