import string,random
def generate_activa_code():
    field=string.uppercase+string.digits
    alist=[]
    for i in range(4):
        alist.append(''.join(random.sample(field,4))+'-')
    return ''.join(alist).strip('-')

def write2file(number):
    f=open('acticoder.txt','wb')
    for i in range(number):
        f.write(generate_activa_code()+'\n')

if __name__=="__main__":
    write2file(200)