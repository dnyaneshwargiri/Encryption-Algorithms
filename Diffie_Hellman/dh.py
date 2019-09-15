def dfh():
        n=input('Enter n')
        g=input('Enter g')
        a=input('Choose 1st secret no (Alice:A)')
        b=input('Choose 2md secret no (Bob:B)')
        A=g**a % n;
        B=g**b % n;
        K1=B**a % n
        K2=A**b % n

        if (K1==K2):
            print('\nKey Succefully Exchanged, Alice and Bob can communicate with each other !')
            print('Shared Secret Key (K) = '+str(K1))
        else:
            print('\nOpps ! Something went wrong.')

if __name__=="__main__":
    dfh()
