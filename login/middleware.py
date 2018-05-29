from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self,request):
        
        ##假如是遇到这些url就不用验证session了。！
        ##首先检查session，
        #print(request.path)
        
        if request.path not in('/estimate/login/',"/estimate/check_login/","/estimate/exit/",'/estimate/verify_code/','/','/favicon.ico'):
            if request.session.get("uid",False):
                pass
            else:
                
                return redirect('/estimate/login/')