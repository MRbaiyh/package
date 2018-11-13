from Crypto.Cipher import AES
from Crypto import Random

#定义一个类，包含加密和解密两个方法
class EpandDp:
    #方法encryption，对输入的text进行加密
    def encryption(self,text):
        self.key = '1234567890!@#$%^'
        self.iv = Random.new().read(16)
        
        self.str = AES.new(self.key,AES.MODE_CFB,self.iv)
        self.strn = self.iv + self.str.encrypt(text)
        print(self.strn)
    #方法decrypt，对文本进行解密
    def decrypt(self):
        cipher = AES.new(self.key,AES.MODE_CFB,self.iv)
        txt = cipher.decrypt(self.strn[16:])
        rtxt = txt.decode('utf8')
        print(rtxt)
A = EpandDp()
text = "阅尽天涯离别苦,不道归来,零落花如许。花底相看无一语,绿窗春与天俱莫。 待把相思灯下诉,一缕新欢,旧恨千千缕。最是人间留不住,朱颜辞镜花辞树。"
print("加密后：")
A.encryption(text)
print("解密后：")
A.decrypt()