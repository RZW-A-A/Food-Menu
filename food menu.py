bill=0
totbill=0
amt=0
gst=0
print("()()()()()()()()()()MENU()()()()()()()()()()()")
while True:
    print("(1) Enter V for veg")
    print("(2) Enter N for non veg")
    print("(3) Enter E for exit")
    q=str(input("enter your choice="))
    if q=='V':
        print("\n")
        print("()()()()()YOU CHOOSE FOR VEGETARIAN()()()()()")
        print("\n")
        while True:
            print("(1) Enter S for starters")
            print("(2) Enter G for gravy")
            print("(3) Enter DR for daal rice")
            print("(4) Enter E for exit")
            w=str(input("enter your choice="))
            if w=='S':
                print("\n")
                print("*****YOU CHOOSE FOR STARTERS*****")
                while True:
                    P=150
                    O=120
                    R=120
                    print("----------------------------------")
                    print("(1) Enter P for paneer chilli")
                    print("(2) Enter O for onion rings")
                    print("(3) Enter R for rajma kebab")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    e=str(input("enter your choice="))
                    if e=='P':
                        quant1=int(input("Quantity for PANEER CHILLI="))
                        amt=amt+P*quant1
                    elif e=='O':
                        quant2=int(input("Quantity for ONION RINGS="))
                        amt=amt+O*quant2
                    elif e=='R':
                        quant3=int(input("Quantity for RAJMA KEBAB="))
                        amt=amt+R*quant3
                    elif e=='E':
                        break
                    else:
                        print("invalid choice")
                    print("----------------------------------")
            elif w=='G':
                print("\n")
                print("*****YPU CHOOSE FOR GRAVY*****")
                while True:
                    M=180
                    K=180
                    VK=160
                    print("----------------------------------")
                    print("(1) Enter M for malai kofta")
                    print("(2) Enter K for kadai paneer")
                    print("(3) Enter VK for veg kurma")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    z=str(input("enter your choice="))
                    if z=='M':
                        quant4=int(input("Quantity for MALAI KOFTA="))
                        amt=amt+M*quant4
                    elif z=='K':
                        quant5=int(input("Quantity for KADAI PANEER="))
                        amt=amt+K*quant5
                    elif z=='VK':
                        quant6=int(input("Quantity for VEG KURMA="))
                        amt=amt+VK*quant6
                    elif z=='E':
                        break
                    else:
                        print("invalid choice")
                    print("----------------------------------")
            elif w=='DR':
                print("\n")
                print("*****YOU CHOOSE FOR DAAL RICE*****")
                while True:
                    JR=100
                    RD=120
                    DF=100
                    print("----------------------------------")
                    print("(1) Enter JR for jeera rice")
                    print("(2) Enter RD for daal rice")
                    print("(3) Enter DF for daal fry")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    v=str(input("enter your choice="))
                    if v=='JR':
                        quant7=int(input("Quantity for JEERA RICE="))
                        amt=amt+JR*quant7
                    elif v=='RD':
                        quant8=int(input("Quantity for DAAL RICE="))
                        amt=amt+RD*quant8
                    elif v=='DF':
                        quant9=int(input("Quantity for DAAL FRY="))
                        amt=amt+DF*quant9
                    elif v=='E':
                        break
                    else:
                        print("invalid choice")
                    print("----------------------------------")
            elif w=='E':
                break
            else:
                print("invalid choice")
                
    if q=='N':
        print("\n")
        print("()()()()()YPU CHOOSE FOR NON-VEGETARIAN()()()()()")
        print("\n")
        while True:
            print("(1) Enter S for starters")
            print("(2) Enter G for gravy")
            print("(3) Enter DR for daal rice")
            print("(4) Enter E for exit")
            u=str(input("enter your choice="))
            if u=='S':
                print("\n")
                print("*****YOU CHOOSE FOR STARTERS*****")
                while True:
                    B=250
                    DF=310
                    CK=200
                    print("----------------------------------")
                    print("(1) Enter B for banjara")
                    print("(2) Enter DF for dry food")
                    print("(3) Enter CK for chicken krispy")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    l=str(input("enter your choice="))
                    if l=='B':
                        quant10=int(input("Quantity for BANJARA="))
                        amt=amt+B*quant10
                    elif l=='DF':
                        quant11=int(input("Quantity for DRY FOOF="))
                        amt=amt+DF*quant11
                    elif l=='CK':
                        quant12=int(input("Quantity for CHICKEN KRISPY="))
                        amt=amt+CK*quant12
                    elif l=='E':
                        break
                    else:
                        print("invalid choice")
                        print("----------------------------------")
            elif u=='G':
                print("\n")
                print("*****YOU CHOOSE FOR GRAVY*****")
                while True:
                    BC=300
                    MM=390
                    SB=290
                    print("----------------------------------")
                    print("(1) Enter BC for butter chicken")
                    print("(2) Enter MM for murg mussallam")
                    print("(3) Enter SB for sanju baba")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    j=str(input("enter your choice="))
                    if j=='BC':
                        quant13=int(input("Quantity for BUTTER CHICKEN="))
                        amt=amt+BC*quant13
                    elif j=='MM':
                        quant14=int(input("Quantity for MURG MUSALLAM="))
                        amt=amt+MM*quant14
                    elif j=='SB':
                        quant15=int(input("Quantity for SANJU BABA="))
                        amt=amt+SB*quant15
                    elif j=='E':
                        break
                    else:
                        print("invalid choice")
                    print("----------------------------------")
            elif u=='DR':
                print("\n")
                print("*****YOU CHOOSE FOR DAAL RICE*****")
                while True:
                    FR=120
                    SR=140
                    KP=250
                    print("----------------------------------")
                    print("(1) Enter FR for fried rice")
                    print("(2) Enter SR for sherpa rice")
                    print("(3) Enter KR for khapsa rice")
                    print("(4) Enter E for exit")
                    print("----------------------------------")
                    f=str(input("enter your choice="))
                    if f=='FR':
                        quant16=int(input("Quantity for FRIED RICE="))
                        amt=amt+FR*quant16
                    elif f=='SR':
                        quant17=int(input("Quantity for SHERPA RICE="))
                        amt=amt+SR*quant17
                    elif f=='KR':
                        quant18=int(input("Quantity for KHEPSA RICE="))
                        amt=amt+KP*quant18
                    elif f=='E':
                        break
                    else:
                        print("invalid choice")
                        print("----------------------------------")
            elif u=='E':
                break
            else:
                print("invalid choice")
                    
    elif q=='E':
        break
    else:
        print("invalid choice")
print("************BILLING**************")
gst=(amt*18)/100
totbill=amt+gst
print("Prize of dishes\t\t:{}\nGST \t\t\t:{}\n----------------------------------\nTOTAL AMOUNT \t\t:{}\n----------------------------------".format(amt,gst,totbill))

print("\n\t()()()()THANK YOU FOR BEING HERE()()()()\n\t()()()()()()PLEASE VIST AGAIN()()()()()()")
