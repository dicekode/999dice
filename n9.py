import requests,json,time,sys,random,os
from random import randint
from datetime import datetime

with open('config.json', 'r') as myfile:
      data=myfile.read()
# parse file
obj = json.loads(data)

c = requests.session()
a=0
url = "https://www.999doge.com/api/web.aspx"
ua = {
 "Origin": "file://",
 "user-agent":  "okhttp/4.2.2",
 "Content-type": "application/x-www-form-urlencoded",
 "Accept": "*/*",
 "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
 "X-Requested-With": "com.reland.relandicebot"
}
def _lowercase(obj):
    if isinstance(obj, dict):
        return {k.lower():_lowercase(v) for k, v in obj.items()}
    elif isinstance(obj, (list, set, tuple)):
        t = type(obj)
        return t(_lowercase(o) for o in obj)
    elif isinstance(obj, str):
        return obj.lower()
    else:
        return obj

def konvert(persen,taruhan):
    global high
    global low
    c = str(999999 * float(persen) / 100)
    if taruhan == "h" or taruhan == "H":
       n = str(c.split(".")[1])
       pangkat = 6 - len(n)
       low = int(int(n) * (10 ** pangkat))
       high = 999999
    if taruhan == "l" or taruhan == "L":
       low = 0
       high = int(c.split(".")[0])


def rev(num):
    if (len(num) < 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        gg = num.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = ("0."+gg+a)
    if (len(num) == 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        gg = num.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = ("0."+gg+a)
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[:len_num-8]
        gg = end.rstrip('0')
        km  = int(8) - (len(gg))
        a = '0' * km
        result = (first+"."+gg+a)
    return (result)

def dice(ws,ls):
   limit_a = int(obj["Reset"]["If_Win"]) - 1
   seeded = 0
   payin = int(float(obj["Interface"]["Base Bet"])*(10 ** 8))
   konvert(obj["Interface"]["Chance"],obj["BetSet"]["Bet"])
   amount = payin
   chan = int(float(obj["Interface"]["Chance"]))
   chann = chan
   seed = randint(0,999999)
   data = {
      "a": "PlaceBet",
      "s": js["SessionCookie"],
      "PayIn": amount,
      "Low": low,
      "High": high,
      "ClientSeed": seed,
      "Currency": "doge",
      "ProtocolVersion": "2"
   }
   try:
     r1 = c.post(url,headers=ua,data=data)
     jsn = json.loads(r1.text)
     try:
        jumbl = jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount)
     except KeyError:
        print ("NO MORE BALANCE")
        sys.exit()
     jum = int(jsn["PayOut"]) - int(amount)
     prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
     n = 0
     burst = False
     stats_rolebet_lose = False
     stats_rolebet_win = False
     total_roll = 0
     no_win = 0
     k = 0
     send = 0
     no_lose = 0
     total_win=0
     total_lose=0
     no_rolebet = 0
     rolebet="L"
     seed_on_off="ON"
     while True:
     #try:
        if _lowercase(obj["Interface"]["Cl_Seed"]["Auto"]) == "on":
           seeded = seeded = int(obj["Interface"]["Cl_Seed"]["Every_Lose"])
           seed = 0
        else:
           seeded = 0
           seed = randint(0,999999)

        if _lowercase(obj["Interface"]["Max Bet"]) == "off":
            max_b = 0
        else:
           max_b = obj["Interface"]["Max Bet"]
           if amount > int(float(max_b))*(10 ** 8):
               amount = payin

        if _lowercase(obj["BetSet"]["H / L"]["Auto"]) == "on":
            no_rolebet +=1
            if stats_rolebet_win is True:
               if no_rolebet > int(obj["BetSet"]["H / L"]["On Win"]) - 1:
                  rolebet = "L"
               if no_rolebet > int(obj["BetSet"]["H / L"]["On Win"]) * 2 - 1:
                  rolebet = "H"
                  no_rolebet = 0
            if stats_rolebet_lose is True:
               if no_rolebet > int(obj["BetSet"]["H / L"]["On Lose"]) -1 :
                  rolebet = "L"
               if no_rolebet > int(obj["BetSet"]["H / L"]["On Lose"]) * 2 - 1:
                  rolebet = "H"
                  no_rolebet = 0
        else:
            rolebet = obj["BetSet"]["Bet"]
        
        if _lowercase(obj["Interface"]["Random"]["Auto"]) == "on":
           hasil_chance = round(random.uniform(float(obj["Interface"]["Random"]["Min"]),float(obj["Interface"]["Random"]["Max"])),2)
           cok = len(str(hasil_chance))
           if cok == 3:
              chance = str(hasil_chance)
           if cok == 4:
              chance = str(hasil_chance)
           if cok == 5:
              chance = str(hasil_chance)+" %"
           konvert(hasil_chance,str(_lowercase(rolebet)))
        else:
           chance = str(obj["Interface"]["Chance"])+" %"
           
           konvert(obj["Interface"]["Chance"],str(_lowercase(rolebet)))

        amount = int(amount)

        n+=1
        data = {
          "a": "PlaceBet",
          "s": js["SessionCookie"],
          "PayIn": amount,
          "Low": low,
          "High": high,
          "ClientSeed": seed,
          "Currency": "doge",
          "ProtocolVersion": "2"

        }
        if prof > float(obj["Stop"]["If_Prof"]):
           print ("\nProfit Reach Target.....!\n"+"Profit "+str(prof))
           sys.exit()
        
        r1 = c.post(url,headers=ua,data=data)
        jsn = json.loads(r1.text)
        try:
           prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
        except KeyError:
           print ("NO MORE BALANCE")
           sys.exit()
        profw = jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl
        profl = str(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl).replace("-","")
        jum = int(jsn["PayOut"]) - int(amount)
        blance = int(jsn["StartingBalance"]) + int(jum)

        if blance > ws:
           if _lowercase(obj["Interface"]["Random"]["Auto"]) == "on":
              print (" "+str(rolebet)+" " " "+str(rev(str(amount)))+"  Profit",+rev(str(profw)),+str(rev(str(blance)))+" "+chance)
              print ("STOP TARGET BALANCE")
           else:
              print (" "+str(rolebet)+" " " "+str(rev(str(amount)))+"  Profit",+rev(str(profw)),+str(rev(str(blance))))
              print ("STOP TARGET BALANCE")
           sys.exit()

        if blance < ls:
           print (" "+str(rolebet)+" " "-"+str(rev(str(amount)))+"  Lose   " "-"+rev(str(profl)),kn+str(rev(str(blance))))
           print ("STOP TARGET LOSE")
           sys.exit()

        if jsn["PayOut"] is not a:
           no_win +=1
           no_lose = 0
           bal = blance
           if prof > 0:
              if _lowercase(obj["Interface"]["Random"]["Auto"]) == "on":
                 print (" "+str(rolebet)+" " " "+str(rev(str(amount)))+"  Profit  "+rev(str(profw)),kn+str(rev(str(bal)))+" "+chance)
              else:
                 print (" "+str(rolebet)+" " " "+str(rev(str(amount)))+"  Profit  "+rev(str(profw))+"  "+str(rev(str(bal))))
           else:
             print (" "+str(rolebet)+" " " "+str(rev(str(amount)))+"  Lose   " "-"+rev(str(profl))+"  "+str(rev(str(bal))))
        else:
           no_win = 0
           no_lose +=1
           i = 0
           burst = True
           bal = blance
           if prof > 0:
              print (" "+str(rolebet)+" " "-"+str(rev(str(amount)))+"  Profit  "+rev(str(profw))+"  "+str(rev(str(bal))))
           else:
              print (" "+str(rolebet)+" " "-"+str(rev(str(amount)))+"  Lose   " "-"+rev(str(profl))+"  "+str(rev(str(bal))))
        total_roll+=1

        if _lowercase(obj["Withdraw"]["Auto"]) == "on":
           wallet = obj["Withdraw"]["Wallet"]
           initial = int(float(obj["Withdraw"]["Initial"])*(10 ** 8))
           triger = int(float(obj["Withdraw"]["Trigger"])*(10 ** 8))
           b = wallet.isnumeric()

           if blance > triger:
              send = int(blance) - int(initial)
              
              data = {"a": "Withdraw",
                      "s": js["SessionCookie"],
                      "Amount": send,
                      "Address": wallet,
                      "Currency": "doge"
                     }
              wd = c.post(url,headers=ua,data=data)
              if b is True:
                 status=" To ID"
              else:
                 status=" To Wallet"

              if wd.status_code == 200:
                 if _lowercase(obj["Interface"]["Random"]["Auto"]) == "on":
                    print ("Succes Withdraw "+str(rev(str(send)))+status)
                 else:
                    print ("Succes Withdraw "+str(rev(str(send)))+status)
              else:
                 if _lowercase(obj["Interface"]["Random"]["Auto"]) == "on":
                    print ("Failed Withdraw "+str(rev(str(send)))+status)
                 else:
                    print ("Failed Withdraw "+str(rev(str(send)))+status)
              bal = int(blance) - int(send)

        if burst is True:
           i+=1
           k+=1
           amount = int(amount) * float(obj["Increase"]["After Lose"])
           seed = randint(0,999999)
           seed_on_off = "ON"
           if k > seeded:
             k = 0
             seed = 0
             seed_on_off= "OFF"
             
           if i > limit_a:
             i = 0
             burst = False
        else:
           if n > limit_a:
             n = 0
             amount = payin
             seed = randint(0,999999)
           else:
             amount = int(amount) * float(obj["Increase"]["After Win"])
 

        if no_win > total_win:
           stats_rolebet_win = True
           stats_rolebet_lose = False
           total_win +=1
        if no_lose > total_lose:
           stats_rolebet_lose = True
           stats_rolebet_win = False
           total_lose +=1
        sys.stdout.write(seed_on_off+ '\033[0;0m'+'\033[1;93m'+" "+'\x1b[0;30;42m'+" "+str(total_win)+" "+ '\x1b[0m'+" "+ '\x1b[1;37;41m'+" "+str(total_lose)+" "+'\x1b[0m'+" "+chance+" Roll : "+str(total_roll)+"\r")


   except:
     print ("")
     sys.exit()
r = c.get(url,headers=ua,data={"a": "Login","Key": "3a66583569ba45419c1b8b5f9d72a95d","Username": obj["Account"]["Username"],"Password": obj["Account"]["Password"],"Totp": ""})
js = json.loads(r.text)
try:
  print ("Balance : "+str(float(js["Doge"]["Balance"])/(10 ** 8)))
except:
  print ("Check Your Username And Your Password")
  sys.exit()

dice(int(float(obj["Stop"]["Balance"])*(10 ** 8)),int(float(obj["Stop"]["If_Lose"])*(10 ** 8)))