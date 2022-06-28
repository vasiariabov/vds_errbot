
import os 
import json
import requests

from errbot import BotPlugin, botcmd, Message, arg_botcmd, re_botcmd


class Vdsworker(BotPlugin):  

#Account
   
    @botcmd  
    def account(self, msg, base ):  
        return self.__account(msg, ) 
    @staticmethod 
    def __account(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/account',                        
                                        headers=newHeaders)
        json_data = response.json()        
        account_data = (json.dumps(json_data, indent=4))    
        return(account_data) 

#Servers 

    @botcmd  
    def servers(self, msg, base ):  
        return self.__servers(msg, ) 
    @staticmethod 
    def __servers(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/scalets',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     


#Background
 
    @botcmd  
    def locations(self, msg, base ):  
        return self.__locations(msg, ) 
    @staticmethod 
    def __locations(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/locations',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     

    @botcmd  
    def images(self, msg, base ):  
        return self.__images(msg, ) 
    @staticmethod 
    def __images(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/images',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)    

#SSHkeys

    @botcmd  
    def sshkeys(self, msg, base ):  
        return self.__sshkeys(msg, ) 
    @staticmethod 
    def __sshkeys(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/sshkeys',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)          
             

#Billing

    @botcmd  
    def balance(self, msg, base ):  
        return self.__balance(msg, ) 
    @staticmethod 
    def __balance(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/balance',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     
        
    @botcmd  
    def payments(self, msg, base ):  
        return self.__payments(msg, ) 
    @staticmethod 
    def __payments(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/payments',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     
        
    @botcmd  
    def consumption(self, msg, base ):  
        return self.__consumption(msg, ) 
    @staticmethod 
    def __consumption(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/consumption?start=&end=',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)      