

##这是一个获取了ip地址之后返回一堆str
def return_nodejs_security(ip_addr):

    if not ip_addr:
        return False

    content = """var os = require("os");

module.exports = function(){
	
	var ip = "127.0.0.1";

	return function(req, res, next){
		//console.log("run me how time?")
		//获取当前电脑Ip地址。 外部ip(本机ip)和内部ip(localhost)
		var localIp = os.networkInterfaces()[0];
		if(!req.session._initialize){
			if( req.ip==localIp || ip==req.ip ){
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

    """%ip_addr

    return content